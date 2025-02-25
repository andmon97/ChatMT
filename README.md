# ChatMT – RAG sul Dialetto Materano

Benvenuti in **ChatMT**, un progetto di **Retrieval-Augmented Generation** dedicato alla cultura e al dialetto di Matera.

---

## Caratteristiche Principali

- **Proverbi e tradizioni**: suggerisce proverbi materani e ne spiega il significato.
- **Informazioni turistiche**: integra dati estratti da WikiMatera.
- **Dialetto**: (futuro) traduzione dall’italiano al dialetto materano con un motore dedicato.

---

## Installazione e Setup Rapido

1. **Clona la repo** (in SSH o HTTPS, come preferisci):
   ```bash
   git clone git@github.com:andmon97/ChatMT.git
   cd ChatMT
   ```

2. **Installa Ollama in locale** (macOS o Linux in base alle istruzioni ufficiali):
   - Metodo rapido su macOS:
     ```bash
     curl -fsSL https://ollama.com/install.sh | sh
     ```
   - Consulta [https://github.com/jmorganca/ollama](https://github.com/jmorganca/ollama) per altre piattaforme (build da sorgente).

3. **Scarica il modello DeepSeek-R1-Distill-Qwen-7B** con Ollama:
   ```bash
   ollama pull deepseek-r1:7b
   ```

4. **Esegui il modello in test rapido**:
   ```bash
   ollama run deepseek-r1:7b
   ```

5. **(Opzionale) Avvia Ollama in modalità server:
    ```bash
   ollama serve
   ```

   Ascolta di default su localhost:11411. Puoi inviare richieste REST dal tuo codice.