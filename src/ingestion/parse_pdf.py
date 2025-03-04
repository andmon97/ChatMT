import pdfplumber
import re
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import requests
import logging
import os

def merge_splitted_words(lines):
    """
    Unisce righe che finiscono con '-' alla successiva,
    rimuovendo il trattino di sillabazione. Esempio:
    'abbatt-' + 'mento' -> 'abbattmento'.
    """
    merged = []
    skip = False
    for i in range(len(lines)):
        if skip:
            skip = False
            continue

        line = lines[i].rstrip()
        # Se la riga finisce con '-' e c'è una riga successiva
        if line.endswith('-') and (i + 1 < len(lines)):
            next_line = lines[i + 1].lstrip()
            new_line = line[:-1] + next_line
            merged.append(new_line)
            skip = True
        else:
            merged.append(line)
    return merged

def process_block(raw_text, vocab_list):
    """
    Elabora il testo di un singolo 'blocco' in cui ci si aspetta
    la forma <termine>: <definizione...> con possibili enumerazioni 1), 2), ecc.
    """
    # Individua <termine> fino al primo ':', e tutto il resto come definizione
    first_split = re.match(r"^([^:]+):\s*(.*)$", raw_text)
    if not first_split:
        return

    termine = first_split.group(1).strip()
    definizione_raw = first_split.group(2).strip()

    # Gestione enumerazioni 1) 2) ...
    parts = re.split(r"\d\)\s*", definizione_raw)
    significati = [p.strip() for p in parts if p.strip()]

    if not significati:
        significati = [definizione_raw]

    vocab_entry = {
        'termine_dialetto': termine,
        'significati': significati
    }
    vocab_list.append(vocab_entry)

def parse_page_text(page_text, vocab_list):
    """
    Applica la logica di parsing su un testo estratto da una singola colonna.
    - Splitta in righe
    - 'Unisce' eventuali linee con trattino
    - Accumula righe in blocchi <termine>: <definizione>
    """
    lines = page_text.split("\n")
    lines = merge_splitted_words(lines)

    # Pattern per riconoscere '<termine>: <definizione>'
    term_pattern = re.compile(r"^([^:]+):\s*(.*)$", re.UNICODE)
    
    current_block = ""
    for line in lines:
        line = line.strip()
        # Saltiamo righe vuote o possibili titoli
        if (not line or
            line.upper() == "DIZIONARIO MATERANO" or
            re.match(r'^[A-Z]$', line)):
            continue

        match = term_pattern.match(line)
        if match:
            # Abbiamo trovato un nuovo 'termine: definizione'
            # Processiamo il blocco accumulato finora
            if current_block:
                process_block(current_block, vocab_list)
                current_block = ""
            # Iniziamo il blocco con la riga corrente
            current_block = line
        else:
            # Altrimenti estendiamo il blocco con la riga attuale
            current_block += " " + line

    # A fine colonna, processiamo l'ultimo blocco se presente
    if current_block:
        process_block(current_block, vocab_list)

def parse_dizionario_pdf(pdf_path: str):
    """
    Legge un PDF strutturato a due colonne (sinistra, destra) per pagina.
    Usa bounding box per estrarre separatamente ciascuna colonna,
    quindi esegue la logica di parsing su entrambe.
    
    Restituisce una lista di dict con 'termine_dialetto' e 'significati'.
    """
    vocab_list = []
    with pdfplumber.open(pdf_path) as pdf_file:
        for page in pdf_file.pages:
            left_text = page.within_bbox((0, 0, page.width / 2, page.height)).extract_text()
            right_text = page.within_bbox((page.width / 2, 0, page.width, page.height)).extract_text()
            # Parse colonna sinistra
            parse_page_text(left_text, vocab_list)
            # Parse colonna destra
            parse_page_text(right_text, vocab_list)

    return vocab_list

def main():
    # voglio che scarichi il pdf da un link e continui con qiello che ho fatto
    link_file_download = "https://www.wikimatera.it/wp-content/uploads/2016/05/dizionario_dialetto_materano_matera.pdf"
    name_file = "dizionario_dialetto_materano_matera.pdf"
    # Carica il file .env (find_dotenv cerca il file a partire dalla cartella corrente verso l'alto)
    load_dotenv(find_dotenv())
    # Usa il percorso definito in .env, che è relativo alla posizione del file di esecuzione
    pdf_path = Path(os.getenv("PDF_DICTIONARY"))
    pdf_folder = os.getenv("PDF_FOLDER")
    
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)

    # Scarica il file
    response = requests.get(link_file_download)
    if response.status_code == 200:
        with open(pdf_path, "wb") as f:
            f.write(response.content)
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.info("Download completato!") 
    else:
        logging.basicConfig(level=logging.ERROR)
        logger = logging.getLogger(__name__)
        logger.error("Errore durante il download:", response.status_code)

    vocab = parse_dizionario_pdf(str(pdf_path))

    # Ordina la lista in ordine alfabetico per 'termine_dialetto'
    vocab.sort(key=lambda entry: entry['termine_dialetto'].lower())

    # Mostra alcune voci d'esempio
    for entry in vocab[:20]:
        print(entry)

if __name__ == "__main__":
    main()
