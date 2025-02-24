# ChatMT – RAG sul Dialetto Materano

Benvenuti in **ChatMT**, un progetto di **Retrieval-Augmented Generation** dedicato alla cultura e al dialetto di Matera. L’obiettivo è creare un assistente virtuale in grado di:
- Suggerire proverbi materani e tradurne il significato.  
- Fornire informazioni turistiche e culturali su Matera.  
- (In futuro) Tradurre frasi dall’italiano al dialetto materano con un motore dedicato.

> **Nota**: Per una panoramica architetturale più approfondita, verrà pubblicato un file separato, **report.md**, che descriverà in dettaglio la struttura del progetto e le scelte tecniche adottate.

---

## Struttura Principale

- `data/`: conterrà i PDF e i dati scaricati (proverbi da WikiMatera, dizionario dialettale, etc.).
- `src/`: codice principale, suddiviso in moduli per ingestion, embeddings, LLM, indexing, pipeline, etc.
- `tests/`: test automatici per convalidare il funzionamento delle varie parti del sistema.
- `.github/workflows/`: pipeline CI (ad es. test e linting su GitHub).

---

## Requisiti

- **Python 3.9+** (consigliato).
- Librerie: `pdfplumber`, `requests`, `beautifulsoup4`, `llama-index` o simili, e un modulo/SDK per *DeepSeek*.

Installa i pacchetti necessari con:
```bash
pip install -r requirements.txt
