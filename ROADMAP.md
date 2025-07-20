# 🗺️ Roadmap - ChatMT

## 🎯 Overview

Sviluppo incrementale da MVP semplice a sistema multi-agente completo per preservare e insegnare il dialetto materano con **ChatMT** - il tuo assistente conversazionale materano!

# 🗺️ Roadmap - ChatMT

## 🎯 Overview

Sviluppo incrementale da MVP semplice a sistema multi-agente completo per preservare e insegnare il dialetto materano con **ChatMT** - il tuo assistente conversazionale materano!

## 📚 Risorse Complete del Progetto

### 📖 **Dizionario Materano** (Antonio D'Ercole - "Voci di Sassi")
- **PDF principale**: 80 pagine, materano→italiano, con esempi d'uso e contesto
- **Download link**: [WikiMatera - Dizionario del dialetto materano](https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/dizionario-del-dialetto-materano/)

### 🌐 **Risorse WikiMatera** (contenuti web)
- [**Pagina principale dialetto**](https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/) - caratteristiche fonetiche, regole base
- [**Grammatica di base**](https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/grammatica-di-base/) - articoli, pronomi, plurali
- [**I numeri - 'U nimm'r**](https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/numeri-u-nimmr/) - sistema numerico + operazioni
- [**Proverbi materani**](https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/i-proverbi-materani/) - saggezza popolare
- [**Parole antiche**](https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/parole-materane-antiche/) - vocabolario in disuso
- [**Preghiere in dialetto**](https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/preghiere-dialetto-materano/) - testi religiosi
- [**Poesie in materano**](https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/poesie-in-materano/) - letteratura dialettale
- [**Soprannomi più diffusi**](https://www.wikimatera.it/cose-da-sapere-su-matera/il-dialetto-materano/soprannomi-piu-diffusi/) - onomastica popolare

### 📰 **Risorse Aggiuntive**
- [**SassiTour - Parole belle**](https://www.sassitour.it/compro-una-vocale-le-10-parole-piu-belle-del-dialetto-materano/) - articoli specializzati
- [**SassiTour - Espressioni**](https://www.sassitour.it/egghia-le-10-espressioni-piu-belle-del-dialetto-materano/) - modi di dire tipici
- [**Wikipedia - Dialetti area apulo-lucana**](https://it.wikipedia.org/wiki/Dialetti_dell'area_apulo-lucana) - analisi linguistica

## 🌿 **Strategia Git Branching**

```
main (stable releases)
├── develop (integration branch)
├── feature/phase-1-mvp
│   ├── feature/pdf-extraction
│   ├── feature/redis-setup
│   ├── feature/langgraph-basic
│   └── feature/cli-interface
├── feature/phase-2-knowledge
│   ├── feature/wikimatera-scraper
│   ├── feature/phonetic-rules
│   ├── feature/cultural-context
│   └── feature/vector-search
├── feature/phase-3-conversational
│   ├── feature/intent-recognition
│   ├── feature/persona-development
│   ├── feature/web-interface
│   └── feature/conversation-memory
├── feature/phase-4-multi-agent
    ├── feature/agent-architecture
    ├── feature/specialized-agents
    ├── feature/langgraph-multi-agent
    └── feature/advanced-orchestration
```

---

## 📅 Fase 1: MVP - Dizionario Base (4-6 settimane)

### 🎯 Obiettivo
Traduttore funzionante con dizionario PDF + Redis + LangGraph base.

### 📋 Dettaglio Task con Branching

#### Week 1-2: Infrastructure & Data Foundation

**Branch: `feature/pdf-extraction`**
- [ ] **Setup pdfplumber extraction**
  - Parser per struttura a due colonne
  - Regex per separare termini e definizioni
  - Handling delle pagine con immagini
  - Output JSON strutturato
  - Unit tests per parsing accuracy

**Branch: `feature/redis-setup`**  
- [ ] **Redis infrastructure**
  - Docker setup per Redis locale
  - Schema design per termini dialetto
  - Vector embeddings preparation
  - Indexing strategies (by category, source)
  - Connection pooling e error handling

**Branch: `feature/project-structure`**
- [ ] **Base project setup**
  - UV dependency management
  - Logging configuration
  - Environment variables setup
  - Basic CLI structure
  - Testing framework setup

#### Week 3-4: Core Translation Engine

**Branch: `feature/langgraph-basic`**
- [ ] **LangGraph workflow implementation**
  - Node: language_detection (IT vs Materano)
  - Node: dictionary_lookup (Redis queries)  
  - Node: response_formatter (structured output)
  - Conditional edges per routing
  - State management between nodes
  - Error handling e fallback strategies

**Branch: `feature/model-integration`**
- [ ] **LLM model factory**
  - Ollama service integration
  - OpenAI service integration  
  - Dynamic model switching via env
  - Prompt templates for translation
  - Response validation e parsing

#### Week 5-6: Interface & Testing

**Branch: `feature/cli-interface`**
- [ ] **Command line interface**
  - Interactive translation mode
  - Batch processing capability
  - History e session management
  - Output formatting options
  - Help e documentation

**Branch: `feature/testing-validation`**
- [ ] **Testing e validation**
  - Unit tests per ogni componente
  - Integration tests workflow completo
  - Validation set from dictionary
  - Performance benchmarking
  - Documentation e examples

### 🎮 Deliverable Fase 1
```bash
uv run chatmt --translate "come si dice casa?"
# Output: "'A cas" (la casa) - Termine di uso quotidiano nei Sassi
```

---

## 📅 Fase 2: Enhanced Knowledge Base (6-8 settimane)

### 🎯 Obiettivo
Sistema ricco con tutte le risorse WikiMatera + ricerca semantica.

### 📋 Dettaglio Task con Branching

#### Week 1-3: Data Expansion

**Branch: `feature/wikimatera-scraper`**
- [ ] **Web scraping completo WikiMatera**
  - Scraper specifico per ogni sezione
  - Parser per grammatica rules
  - Extraction proverbi + contesto
  - Poesie e preghiere processing
  - Rate limiting e respectful scraping
  - Data validation e cleaning

**Branch: `feature/external-sources`**
- [ ] **Integration fonti aggiuntive**
  - SassiTour articles scraping
  - Wikipedia dialect analysis extraction
  - Cross-referencing tra fonti
  - Duplicate detection e merging
  - Source attribution tracking

#### Week 4-6: Advanced Features

**Branch: `feature/phonetic-rules`**
- [ ] **Regole fonetiche sistematiche**
  - Pattern matching per trasformazioni vocaliche
  - Rule engine per generazione traduzioni
  - Varianti ortografiche handling
  - Confidence scoring per regole
  - Interactive rule testing

**Branch: `feature/vector-search`**
- [ ] **Semantic search implementation**
  - Embeddings generation per tutti i termini
  - Vector similarity search
  - Semantic clustering di contenuti simili
  - Multi-language embeddings (IT+Materano)
  - Performance optimization

#### Week 7-8: Context Enhancement

**Branch: `feature/cultural-context`**
- [ ] **Context-aware responses**
  - Proverbi matching per context
  - Cultural notes automatic injection
  - Historical context association
  - Usage examples from poetry/prayers
  - Smart content recommendation

**Branch: `feature/enhanced-workflow`**
- [ ] **LangGraph workflow espanso**
  - Node: phonetic_rules_application
  - Node: cultural_context_enrichment  
  - Node: semantic_search
  - Advanced routing logic
  - Multi-source result aggregation

### 🎮 Deliverable Fase 2
```bash
uv run chatmt --translate "piove" --context
# Output:
# 🔄 "piove" → "chiòv" / "fa l'acqua" / "scatarr l'acqua dal ciel"
# 📜 Proverbio: "Quan chiòv, 'u cucul cant" (Quando piove, il cuculo canta)
# 🏛️ Contesto: Espressione usata nei Sassi quando si prevedeva maltempo
# 🎭 Da una poesia: "Chiòv sempr quann 'u cuer è trist..."
```

---

## 📅 Fase 3: Conversational AI (8-10 settimane)

### 🎯 Obiettivo
Chatbot conversazionale con personalità "Nonna Maria" e memoria.

### 📋 Dettaglio Task con Branching

#### Week 1-3: Conversation Foundation

**Branch: `feature/intent-recognition`**
- [ ] **Sistema riconoscimento intenti**
  - Classification traduzioni vs insegnamento vs cultura
  - Entity extraction per termini chiave
  - Context detection (formal vs informal)
  - Multi-intent handling
  - Confidence thresholds

**Branch: `feature/conversation-memory`**
- [ ] **Gestione memoria conversazionale**
  - Session state in Redis
  - User preference learning
  - Conversation history management  
  - Context persistence tra messaggi
  - Smart context retrieval

#### Week 4-6: Personality Development

**Branch: `feature/persona-development`**
- [ ] **"Nonna Maria" personality**
  - Tone e style guidelines implementation
  - Intercalari e espressioni database
  - Mixing patterns italiano-materano
  - Emotional response system
  - Storytelling capabilities

**Branch: `feature/response-generation`**
- [ ] **Advanced response system**
  - Template system per diversi intent
  - Natural language generation
  - Variazioni stilistiche
  - Graceful degradation strategies
  - Response quality scoring

#### Week 7-10: Interface Development

**Branch: `feature/web-interface`**
- [ ] **Web interface (Streamlit)**
  - Chat UI responsive design
  - Real-time conversation flow
  - History e bookmarking features
  - Export conversation capability
  - Mobile-friendly design

**Branch: `feature/advanced-interactions`**
- [ ] **Advanced conversational features**
  - Quiz mode implementation
  - Interactive storytelling
  - Cultural context on-demand
  - Learning progress tracking
  - Personalized recommendations

### 🎮 Deliverable Fase 3
```
User: "Ciao nonna!"
Nonna Maria: "Egghia figghj bell! Com st? Abbinì a parlè 'n poc d'matarràs ins'm?"

User: "Sì, insegnami i saluti"
Nonna Maria: "Alluòr, sént a miéì... la matìn diciàm 'Bòn giùrn', 
la sèr 'Bòna sèr'... e sai che una volta i piccirídd dic'van sempre 
'Basamàn' ai grand? Ièra 'na bell tradizion..."
```

---

## 📅 Fase 4: Multi-Agent System (10-12 settimane)

### 🎯 Obiettivo
Sistema multi-agente specializzato con agenti per traduzione, cultura, insegnamento, turismo.

### 📋 Dettaglio Task con Branching

#### Week 1-4: Agent Architecture

**Branch: `feature/agent-architecture`**
- [ ] **Base agent framework**
  - Abstract base agent class
  - Communication protocols definition
  - Shared memory system
  - Agent lifecycle management
  - Error handling e recovery

**Branch: `feature/chat-manager`**
- [ ] **Chat Manager Agent**
  - Intent routing intelligente
  - Agent selection algorithm
  - Context sharing mechanisms
  - Conversation flow orchestration
  - Conflict resolution strategies

#### Week 5-8: Specialized Agents

**Branch: `feature/translator-agent`**
- [ ] **Traduttore Agent**
  - Existing LangGraph workflow integration
  - Specialized translation prompts
  - Historical translation tracking
  - Quality assessment
  - User feedback learning

**Branch: `feature/storyteller-agent`**
- [ ] **Storyteller Agent**
  - Sassi stories database creation
  - Dynamic story selection
  - Interactive storytelling
  - Cultural context weaving
  - Story customization

**Branch: `feature/teacher-agent`** 
- [ ] **Teacher Agent**
  - Grammatica lesson planning
  - Progressive difficulty system
  - Exercise generation
  - Progress assessment
  - Personalized curriculum

**Branch: `feature/guide-agent`**
- [ ] **Tourist Guide Agent**
  - Matera places database
  - Location-based recommendations
  - Cultural event integration
  - Itinerary planning
  - Historical context provision

#### Week 9-12: System Integration

**Branch: `feature/langgraph-multi-agent`**
- [ ] **LangGraph multi-agent patterns**
  - Multi-agent workflow design
  - Agent-as-node implementation
  - State sharing between agent nodes
  - Conditional routing between agents
  - Parallel agent execution

**Branch: `feature/advanced-orchestration`**
- [ ] **Advanced coordination**
  - Multi-turn conversation handling
  - Seamless agent handoff via LangGraph edges
  - Context preservation in shared state
  - Collaborative responses aggregation
  - Dynamic agent selection logic

### 🎮 Deliverable Fase 4
```
User: "Raccontami dei Sassi e insegnami le parole che usi"

Chat Manager → Storyteller + Teacher

Storyteller: "I Sass èr 'na cummunità che campàva com 'na gran famiglij... 
[racconto dei vicinati]"

Teacher: "Le parole che hai sentito:
- 'cummunità' = comunità (dal latino communitas)
- 'campàva' = viveva (da 'campare', vivere)
- 'famiglij' = famiglia (plurale materano di famiglia)"

Guide: "Vuoi visitare un antico vicinato? Ti consiglio il Sasso Caveoso..."
```

---

## 📅 Fase 5: Advanced Features (12+ settimane)

### 🎯 Obiettivo
Production-ready system con features avanzate.

### 📋 Dettaglio Task con Branching

#### Production Features

**Branch: `feature/mobile-app`**
- [ ] **Mobile application**
  - React Native/Flutter development
  - Offline mode with local storage
  - GPS-based contextual information
  - Camera integration for text recognition
  - Push notifications for learning

**Branch: `feature/pwa-development`**
- [ ] **Progressive Web App**
  - Service worker implementation
  - Offline functionality
  - App-like experience
  - Fast loading optimization
  - Cross-platform compatibility

#### Advanced Features

**Branch: `feature/gamification`**
- [ ] **Learning gamification**
  - Achievement system
  - Progress tracking
  - Daily challenges
  - Leaderboards
  - Social features

**Branch: `feature/community-features`**
- [ ] **Community integration**
  - User-generated content validation
  - Crowdsourced translations
  - Regional variation documentation
  - Expert validation system
  - Community moderation

---

## 📊 Milestone Tracking

| Fase | Durata | Target | Key Deliverables | Main Branches |
|------|---------|---------|------------------|---------------|
| 1 - MVP | 6 settimane | Marzo 2025 | CLI translator, Redis setup | `feature/pdf-extraction`, `feature/redis-setup`, `feature/langgraph-basic` |
| 2 - Knowledge Base | 8 settimane | Maggio 2025 | WikiMatera integration, vector search | `feature/wikimatera-scraper`, `feature/vector-search` |
| 3 - Conversational | 10 settimane | Agosto 2025 | Web chat, Nonna Maria persona | `feature/web-interface`, `feature/persona-development` |
| 4 - Multi-Agent | 12 settimane | Novembre 2025 | 4 specialized agents | `feature/agent-architecture`, `feature/langgraph-multi-agent` |
| 5 - Advanced | Ongoing | 2026+ | Mobile app, gamification | `feature/mobile-app`, `feature/gamification` |

---

## 🎯 Success Criteria per Fase

### Technical KPIs
- **Fase 1**: 80% accuracy su dizionario, <2s response time
- **Fase 2**: 1000+ termini, vector search <500ms
- **Fase 3**: Natural conversation flow, session persistence
- **Fase 4**: 4 agenti coordinati, <3s multi-agent response
- **Fase 5**: Mobile app 4.5+ rating, 10k+ active users

### Cultural Impact KPIs
- **Community validation** da madrelingua materani
- **Educational adoption** in scuole/università
- **Tourist engagement** in percorsi Matera 2025+
- **Media coverage** locale e nazionale
- **Academic research** citations e collaborations

---

## 🎯 Success Criteria

### Technical KPIs
- **Translation Accuracy**: >85% per termini nel dizionario
- **Response Time**: <2 secondi per query semplici
- **User Retention**: Misurazione engagement in Fase 3+

### Cultural Impact KPIs
- **Community Adoption**: Feedback positivo da madrelingua
- **Educational Value**: Utilizzo in scuole/università
- **Tourist Engagement**: Integrazione in percorsi turistici Matera

---

## 🚨 Risk Mitigation

### Technical Risks
- **LLM Hallucination**: Validation rigorosa con esperti
- **Data Quality**: Multiple sources cross-validation
- **Performance**: Early testing e optimization

### Cultural Risks
- **Linguistic Accuracy**: Collaboration con madrelingua
- **Cultural Sensitivity**: Review by cultural experts
- **Preservation Balance**: Authentic vs accessible content

---

## 🤝 Collaboration Opportunities

### Academic Partnerships
- Università della Basilicata
- Centri studi dialettologici
- Archivio tradizioni orali

### Community Engagement
- Associazioni culturali materane
- Anziani madrelingua per validation
- Turismo culturale Matera

### Tech Community
- Open source contributors
- NLP researchers
- Dialect preservation projects