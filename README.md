# 🏛️ ChatMT - Chatbot Dialetto Materano

Un chatbot intelligente per tradurre e insegnare il dialetto materano, preservando il patrimonio linguistico e culturale di Matera.

> **ChatMT** = Chat + MT (provincia di Matera) - Il tuo assistente personale per il dialetto materano!

## 📋 Descrizione

Il progetto mira a creare un assistente conversazionale che:
- Traduce tra italiano e dialetto materano
- Insegna grammatica e pronuncia del dialetto
- Fornisce contesto culturale e storico
- Racconta tradizioni e aneddoti dei Sassi

## 🏗️ Architettura

### Fase 1 - MVP (Dizionario Base)
```
User Input → LangGraph Workflow → Response
    ↓
[Preprocessing] → [Dictionary Lookup] → [Response Formatting]
```

### Fase 2 - Sistema Multi-Agente (Futuro)
```
User Input → Chat Manager → Specialized Agents → Coordinated Response
                   ↓
    ┌─ Traduttore Materano (LangGraph)
    ├─ Storyteller Culturale  
    ├─ Guida Turistica Matera
    └─ Insegnante Dialetto
```

## 📚 Risorse

### 📖 Risorse Primarie (Fase 1)
- **Dizionario Materano** (Antonio D'Ercole - "Voci di Sassi")
  - 80 pagine in PDF
  - Formato: Materano → Italiano
  - Esempi d'uso e contesto

### 🌐 Risorse WikiMatera (Fasi 2-3)

#### Risorse Lessicali
- [Dizionario del dialetto materano](https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/dizionario-del-dialetto-materano/)
- [Parole materane antiche](https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/parole-materane-antiche/)
- [I soprannomi più diffusi](https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/soprannomi-piu-diffusi/)

#### Risorse Grammaticali
- [Grammatica di base](https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/grammatica-di-base/)
- [I numeri - 'U nimm'r](https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/numeri-u-nimmr/)

#### Risorse Culturali
- [I proverbi materani](https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/i-proverbi-materani/)
- [Preghiere in dialetto](https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/preghiere-dialetto-materano/)
- [Poesie in materano](https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/poesie-in-materano/)

#### Pagina Principale
- [Il dialetto materano](https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/) (caratteristiche fonetiche)

### 📚 Risorse Aggiuntive (Fase 4)
- SassiTour: articoli su espressioni tipiche
- Wikipedia: analisi linguistica dettagliata
- Angelo Sarra: "Dizionario 'Na chedd' di parole in disuso" (con CD audio)

## 🛠️ Stack Tecnologico

### Core Technologies
- **Python 3.12+**
- **LangGraph** - Workflow orchestration
- **LangChain** - LLM integration
- **Ollama** - Local LLM models
- **OpenAI API** - Cloud LLM models

### Data Processing
- **pdfplumber** - PDF text extraction
- **BeautifulSoup4** - Web scraping WikiMatera
- **pandas** - Data manipulation
- **Redis** - Vector database and caching
- **redis-py** - Redis Python client

### Web Framework (Futuro)
- **Streamlit** or **Gradio** - Chat interface
- **FastAPI** - Backend API

## 🗄️ Data Storage Strategy

### Redis Vector Database
```python
# Struttura dati Redis per termini dialetto
KEY: "term:materano:{term_id}"
VALUE: {
    "materano_term": "abbinì",
    "italian_translation": "hai da venire, devi venire", 
    "category": "verbi",
    "examples": ["abbinì appess a miéì"],
    "cultural_notes": "formula di invito tipica",
    "source": "dizionario_dercole",
    "embedding": [0.1, 0.2, ...],  # Vector for semantic search
    "created_at": "2025-01-01T00:00:00Z"
}

# Indici per ricerca
SET: "terms:by_category:{category}" → {term_id1, term_id2, ...}
SET: "terms:by_source:{source}" → {term_id1, term_id2, ...}
ZSET: "terms:by_popularity" → term_id (score = usage_count)
```

## ⚙️ Setup

### 1. Installazione
```bash
git clone [repository-url]
cd ChatMT

# Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync
```

### 2. Configurazione Modelli
```bash
# Copy and edit environment file
cp .env.example .env

# .env file
OPENAI_API_KEY=your_openai_key
OLLAMA_MODEL=llama3.1  # or preferred local model
USE_LOCAL_MODEL=true   # or false for OpenAI

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD=  # if required

LOG_LEVEL=INFO
```

### 3. Preparazione Dati
```bash
# Install Redis (if not already installed)
# macOS: brew install redis
# Ubuntu: sudo apt install redis-server
# Start Redis: redis-server

# Data processing (development-driven approach)
uv run src/data/pdf_extractor.py
uv run src/data/web_scraper.py

# Note: Database setup and schema will be implemented during development
```

### 4. Avvio
```bash
# CLI version
uv run main.py

# Web interface (Fase 3+)
uv run streamlit run src/interface/streamlit_app.py
```

## 📁 Struttura Repository

```
ChatMT/
├── 📄 pyproject.toml              # UV dependency management
├── 📄 uv.lock                     # UV lockfile
├── 📄 README.md
├── 📄 ROADMAP.md
├── 📄 .env.example
├── 📄 .gitignore
├── 📄 main.py                     # Entry point CLI
│
├── 📁 data/                       # All data resources
│   ├── 📁 raw/                    # Original, immutable resources
│   │   ├── 📄 dizionario_materano.pdf
│   │   └── 📁 images/             # Dialect-related images from WikiMatera
│   │
│   ├── 📁 scraped/                # Web-scraped content
│   │   ├── 📄 wikimatera_pages.json
│   │   ├── 📄 proverbi.json
│   │   ├── 📄 grammatica.json
│   │   ├── 📄 numeri.json
│   │   ├── 📄 poesie.json
│   │   ├── 📄 preghiere.json
│   │   ├── 📄 soprannomi.json
│   │   └── 📄 parole_antiche.json
│   │
│   ├── 📁 processed/              # Cleaned, structured data
│   │   ├── 📄 dictionary_terms.json
│   │   ├── 📄 phonetic_rules.json
│   │   ├── 📄 cultural_content.json
│   │   └── 📄 training_examples.json
│   │
│   └── 📁 exports/                # Generated datasets for training
│       ├── 📄 translation_pairs.csv
│       ├── 📄 conversation_examples.json
│       └── 📄 validation_set.json
│
├── 📁 src/                        # Source code
│   ├── 📄 __init__.py
│   │
│   ├── 📁 core/                   # Core application logic
│   │   ├── 📄 __init__.py
│   │   ├── 📄 config.py           # Configuration management
│   │   ├── 📄 exceptions.py       # Custom exceptions
│   │   └── 📄 constants.py        # Application constants
│   │
│   ├── 📁 models/                 # LLM and data models
│   │   ├── 📄 __init__.py
│   │   ├── 📄 model_factory.py    # Ollama/OpenAI factory
│   │   ├── 📄 schemas.py          # Pydantic models
│   │   └── 📄 prompts.py          # Prompt templates
│   │
│   ├── 📁 data/                   # Data processing and management
│   │   ├── 📄 __init__.py
│   │   ├── 📄 pdf_extractor.py    # PDF dictionary processing
│   │   ├── 📄 web_scraper.py      # WikiMatera scraping
│   │   ├── 📄 redis_manager.py    # Redis operations and vector search
│   │   ├── 📄 text_processor.py   # Text cleaning and normalization
│   │   └── 📄 knowledge_builder.py # Knowledge base construction
│   │
│   ├── 📁 workflows/              # LangGraph workflows
│   │   ├── 📄 __init__.py
│   │   ├── 📄 translation_workflow.py  # Core translation logic
│   │   ├── 📄 chat_workflow.py         # Conversational flow
│   │   ├── 📄 teaching_workflow.py     # Educational interactions
│   │   └── 📄 nodes/                   # Workflow nodes
│   │       ├── 📄 __init__.py
│   │       ├── 📄 language_detection.py
│   │       ├── 📄 dictionary_lookup.py
│   │       ├── 📄 phonetic_rules.py
│   │       ├── 📄 cultural_context.py
│   │       └── 📄 response_formatter.py
│   │
│   ├── 📁 agents/                 # Multi-agent system (Fase 4)
│   │   ├── 📄 __init__.py
│   │   ├── 📄 base_agent.py       # Abstract base agent
│   │   ├── 📄 chat_manager.py     # Main orchestrator
│   │   ├── 📄 translator.py       # Translation specialist
│   │   ├── 📄 storyteller.py      # Cultural narratives
│   │   ├── 📄 teacher.py          # Grammar and lessons
│   │   └── 📄 guide.py            # Matera tourism info
│   │
│   ├── 📁 interface/              # User interfaces
│   │   ├── 📄 __init__.py
│   │   ├── 📄 cli.py              # Command line interface
│   │   ├── 📄 streamlit_app.py    # Web chat interface
│   │   └── 📄 gradio_app.py       # Alternative web interface
│   │
│   ├── 📁 services/               # External service integrations
│   │   ├── 📄 __init__.py
│   │   ├── 📄 ollama_service.py   # Ollama integration
│   │   └── 📄 openai_service.py   # OpenAI integration
│   │
│   └── 📁 utils/                  # Utility functions
│       ├── 📄 __init__.py
│       ├── 📄 logging_config.py   # Logging setup
│       ├── 📄 validation.py       # Data validation
│       ├── 📄 text_utils.py       # Text processing utilities
│       └── 📄 performance.py      # Performance monitoring
│
├── 📁 scripts/                    # Development utilities (as needed)
│   └── 📄 __init__.py
│
├── 📁 tests/                      # Test suite
│   ├── 📄 __init__.py
│   ├── 📄 conftest.py            # Pytest configuration
│   ├── 📁 unit/                  # Unit tests
│   │   ├── 📄 test_data_processing.py
│   │   ├── 📄 test_workflows.py
│   │   ├── 📄 test_models.py
│   │   └── 📄 test_utils.py
│   ├── 📁 integration/           # Integration tests
│   │   ├── 📄 test_translation_flow.py
│   │   ├── 📄 test_redis_operations.py
│   │   └── 📄 test_agents.py
│   └── 📁 fixtures/              # Test data
│       ├── 📄 sample_dictionary.json
│       ├── 📄 test_conversations.json
│       └── 📄 validation_cases.json
│
├── 📁 config/                     # Configuration files
│   ├── 📄 logging.yaml           # Logging configuration
│   ├── 📄 redis.yaml             # Redis connection and schema config
│   └── 📄 agents.yaml            # Agent configurations
│
├── 📁 notebooks/                  # Jupyter notebooks for analysis
│   ├── 📄 01_dictionary_analysis.ipynb
│   ├── 📄 02_phonetic_patterns.ipynb
│   ├── 📄 03_cultural_content_exploration.ipynb
│   └── 📄 04_model_evaluation.ipynb
│
├── 📁 docs/                       # Documentation
│   ├── 📄 architecture.md        # System architecture
│   ├── 📄 data_sources.md        # Data documentation
│   ├── 📄 api_reference.md       # API documentation
│   ├── 📄 deployment.md          # Deployment guide
│   └── 📁 examples/              # Usage examples
│       ├── 📄 basic_translation.py
│       ├── 📄 chat_examples.py
│       └── 📄 agent_workflows.py
│
└── 📁 deployment/                 # Deployment configurations
    ├── 📄 Dockerfile
    ├── 📄 docker-compose.yml
    ├── 📄 requirements-prod.txt   # Production dependencies
    └── 📁 k8s/                   # Kubernetes configs (future)
        ├── 📄 deployment.yaml
        └── 📄 service.yaml
```

## 🎯 Obiettivi del Progetto

### Educativi
- Preservare il dialetto materano per le future generazioni
- Fornire uno strumento di apprendimento interattivo
- Documentare varianti e sfumature linguistiche

### Tecnologici
- Sperimentare con LangGraph per workflow complessi
- Implementare sistemi multi-agente conversazionali
- Integrare risorse testuali eterogenee

### Culturali
- Promuovere il patrimonio culturale di Matera
- Creare ponte tra tradizione e innovazione tecnologica
- Sviluppare strumento turistico culturale

## 🤝 Contributi

Il progetto è aperto a contributi di:
- Madrelingua materani per validazione linguistica
- Sviluppatori interessati a dialetti regionali
- Esperti di NLP e sistemi conversazionali
- Appassionati di cultura materana

## 📄 Licenza

[Da definire - considerare licenza open source per la parte tecnica]

## 🙏 Riconoscimenti

- Antonio D'Ercole per il "Dizionario Materano"
- WikiMatera.it per le risorse culturali
- Comunità materana per la preservazione del dialetto