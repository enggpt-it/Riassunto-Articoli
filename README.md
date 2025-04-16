# 📝 Articoli in Pillole con GPT-4.1

Questa applicazione web permette di generare automaticamente punti salienti (bullet points) dai testi di articoli utilizzando il modello GPT-4.1 di OpenAI. L'applicazione estrae i concetti chiave e li presenta in un formato di lista puntata facilmente leggibile.

![Esempio dell'applicazione](https://picsum.photos/seed/summarizer/600/400)

## Caratteristiche

- Estrazione automatica dei punti salienti da qualsiasi testo
- Interfaccia utente intuitiva sviluppata con Streamlit
- Possibilità di selezionare il numero di punti da generare
- Utilizzo dell'API di OpenAI con il modello GPT-4.1
- Supporto per API key salvate come variabili d'ambiente o secrets di Streamlit

## Requisiti

- Python 3.8 o versioni successive
- Una API key di OpenAI (ottenibile registrandosi su [platform.openai.com](https://platform.openai.com))
- Accesso alle API GPT-4.1 (richiede un account OpenAI Developer con credito disponibile)

## Installazione

1. Clona questo repository:
   ```bash
   git clone https://github.com/enggpt-it/Riassunto-Articoli.git
   cd Riassunto-Articoli
   ```

2. Installa le dipendenze necessarie:
   ```bash
   pip install -r requirements.txt
   ```

## Configurazione

Ci sono due modi per configurare la tua API key di OpenAI:

### Opzione 1: 
Crea un file `.env` nella root del progetto con il seguente contenuto:

```bash
OPENAI_API_KEY=sk-your-api-key-here
```

### Opzione 2: Streamlit Secrets
Crea un file `.streamlit/secrets.toml` nella root del progetto con il seguente contenuto:

```toml
openai_api_key = "sk-your-api-key-here"
```

**Nota**: Assicurati di non condividere o committare la tua API key nel repository.

## Utilizzo

1. Avvia l'applicazione Streamlit:
   ```bash
   streamlit run article_summarize.py
   ```

2. Apri il browser all'indirizzo indicato (di solito http://localhost:8501)

3. Incolla il testo dell'articolo da riassumere

4. Seleziona il numero di punti salienti desiderati

5. Fai clic su "Genera Riassunto"

## Personalizzazioni possibili

- Modificare il prompt nel file per adattarlo a esigenze specifiche
- Cambiare il modello utilizzato (ad esempio passando da GPT-4.1 a GPT-4.1-mini per ridurre i costi)
- Aggiungere opzioni per altri formati di output (markdown, JSON, ecc.)

## Licenza

Questo progetto è rilasciato sotto licenza MIT. Consulta il file [LICENSE](./LICENSE) per maggiori dettagli.