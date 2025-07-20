# 🗺️ Roadmap - ChatMT

## 🎯 Overview

Sviluppo incrementale da MVP semplice a sistema multi-agente completo per preservare e insegnare il dialetto materano con **ChatMT** - il tuo assistente conversazionale materano!

---

## 📅 Fase 1: MVP - Dizionario Base (4-6 settimane)

### 🎯 Obiettivo
Creare un traduttore basico funzionante con il dizionario PDF.

### 📋 Task Principali

#### Week 1-2: Data Foundation
- [ ] **Setup progetto e ambiente**
  - Struttura repository
  - Configurazione .env per Ollama/OpenAI
  - Setup Redis vector database
  
- [ ] **Estrazione dati dizionario**
  - Script pdfplumber per parsing PDF
  - Pulizia e normalizzazione testo
  - Creazione dataset strutturato (JSON)

#### Week 3-4: Core Translation Engine
- [ ] **LangGraph workflow base**
  - Nodo: language detection (IT vs Materano)
  - Nodo: dictionary lookup
  - Nodo: response formatting
  - Gestione errori e fallback
  
- [ ] **Model integration**
  - Factory pattern per Ollama/OpenAI
  - Prompt engineering per traduzioni
  - Testing con esempi del dizionario

#### Week 5-6: MVP Interface
- [ ] **CLI interface**
  - Input/output gestione
  - Modalità interattiva
  - Logging e debug
  
- [ ] **Testing e validazione**
  - Unit tests core functions
  - Validation set from dictionary
  - Performance benchmarking

### 🎮 Deliverable Fase 1
```bash
python main.py --translate "come si dice casa?"
# Output: "'A cas" in materano significa "la casa"
```

---

## 📅 Fase 2: Enhanced Knowledge Base (6-8 settimane)

### 🎯 Obiettivo
Integrare tutte le risorse WikiMatera per arricchire il knowledge base.

### 📋 Task Principali

#### Week 1-3: Data Expansion
- [ ] **Web scraping WikiMatera**
  - Scraper per tutte le sezioni identificate
  - Parser per strutture diverse (liste, testi, poesie)
  - Categorizzazione automatica contenuti
  
- [ ] **Database enhancement**
  - Schema Redis per contenuti culturali
  - Vector embeddings per ricerca semantica
  - Indicizzazione per performance

#### Week 4-6: Advanced Translation Features
- [ ] **Regole fonetiche sistematiche**
  - Pattern matching per trasformazioni vocaliche
  - Generazione traduzioni per parole non nel dizionario
  - Gestione varianti ortografiche
  
- [ ] **Context-aware responses**
  - Integrazione proverbi pertinenti
  - Esempi d'uso da poesie/preghiere
  - Note culturali automatiche

#### Week 7-8: Enhanced Workflow
- [ ] **LangGraph workflow espanso**
  - Nodo: phonetic rules application
  - Nodo: cultural context enrichment
  - Nodo: example generation
  - Routing condizionale intelligente

### 🎮 Deliverable Fase 2
```bash
python main.py --translate "piove"
# Output: 
# 🔄 "piove" → "chiòv" / "fa l'acqua"
# 📜 Proverbio: "Quan chiòv, 'u cucul cant'"
# 🏛️ Note: Si usava anche "scatarr l'acqua dal ciel"
```

---

## 📅 Fase 3: Conversational AI (8-10 settimane)

### 🎯 Obiettivo
Trasformare il traduttore in un chatbot conversazionale con personalità.

### 📋 Task Principali

#### Week 1-3: Chat Foundation
- [ ] **Intent recognition system**
  - Classificazione tipi di richiesta
  - Entity extraction per termini chiave
  - Context management tra messaggi
  
- [ ] **Conversational memory**
  - Session state management
  - User preference learning
  - Conversation history per follow-up

#### Week 4-6: Personality Development
- [ ] **"Nonna Maria" persona**
  - Tone and style guidelines
  - Intercalari e espressioni tipiche
  - Mixing patterns italiano-materano
  
- [ ] **Response templates**
  - Template per diversi intent types
  - Variazioni stilistiche
  - Graceful degradation strategies

#### Week 7-10: Interface Development
- [ ] **Web interface (Streamlit/Gradio)**
  - Chat UI responsive
  - Voice input/output (futuro)
  - History e bookmarking
  
- [ ] **Advanced features**
  - Modalità quiz/insegnamento
  - Storytelling interattivo
  - Cultural context on-demand

### 🎮 Deliverable Fase 3
```
User: "Ciao nonna!"
Bot: "Egghia figghj bell! Com st? Abbinì a parlè 'n poc d'matarràs?"

User: "Insegnami i saluti"
Bot: "Alluòr... la matìn diciàm 'Bòn giùrn', la sèr 'Bòna sèr'..."
```

---

## 📅 Fase 4: Multi-Agent System (10-12 settimane)

### 🎯 Obiettivo
Sistema multi-agente specializzato per diversi aspetti della cultura materana.

### 📋 Task Principali

#### Week 1-4: Agent Architecture
- [ ] **Chat Manager Agent**
  - Intent routing intelligente
  - Agent coordination
  - Context sharing between agents
  
- [ ] **Specialized Agents**
  - **Traduttore**: LangGraph workflow esistente
  - **Storyteller**: Racconti e aneddoti Sassi
  - **Teacher**: Grammatica e esercizi
  - **Guide**: Info turistiche Matera

#### Week 5-8: Agent Implementation
- [ ] **CrewAI/AutoGen integration**
  - Multi-agent framework setup
  - Communication protocols
  - Conflict resolution strategies
  
- [ ] **Knowledge specialization**
  - Domain-specific knowledge per agent
  - Cross-agent knowledge sharing
  - Dynamic agent selection

#### Week 9-12: System Integration
- [ ] **Advanced orchestration**
  - Multi-turn conversations
  - Agent handoff seamless
  - Contextual memory sharing
  
- [ ] **Performance optimization**
  - Parallel processing where possible
  - Caching strategies
  - Response time optimization

### 🎮 Deliverable Fase 4
```
User: "Raccontami dei Sassi e insegnami le parole"
Chat Manager → Storyteller + Teacher

Storyteller: "I Sass èr 'na cummunità viva... [racconto]"
Teacher: "Le parole che hai sentito: 'cummunità' = comunità..."
```

---

## 📅 Fase 5: Advanced Features (12+ settimane)

### 🎯 Obiettivo
Features avanzate per completare l'esperienza utente.

### 📋 Task Principali

#### Production Features
- [ ] **Mobile App**
  - React Native / Flutter app
  - Offline mode capability
  - GPS-based contextual info
  
- [ ] **Advanced Web Features**
  - PWA (Progressive Web App)
  - Advanced search capabilities
  - Export/import user content
  
- [ ] **Gamification**
  - Dialect learning challenges
  - Progress tracking
  - Social features per community

#### Research Features
- [ ] **Advanced NLP**
  - Semantic search improvements
  - Context-aware translations
  - Dialect variation mapping
  
- [ ] **Community Contributions**
  - User-generated content validation
  - Crowdsourced translations
  - Regional variation documentation

---

## 📊 Milestone Tracking

| Fase | Durata | Completamento Target | Key Metrics |
|------|---------|----------------------|-------------|
| 1 - MVP | 6 settimane | Marzo 2025 | 80% accuracy su dizionario, Redis setup |
| 2 - Knowledge Base | 8 settimane | Maggio 2025 | 1000+ termini, Vector search |
| 3 - Conversational | 10 settimane | Agosto 2025 | Natural conversation flow |
| 4 - Multi-Agent | 12 settimane | Novembre 2025 | 4 agenti specializzati |
| 5 - Advanced | Ongoing | 2026+ | Production-ready app |

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