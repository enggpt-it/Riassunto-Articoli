from decouple import config
import openai
import streamlit as st
from typing import List, Optional

# Funzione per generare punti salienti usando l'API OpenAI
def generate_bullet_points(article_text: str, openai_api_key: str, model: str = "gpt-4.1") -> Optional[List[str]]:
    """
    Usa la OpenAI API per generare una lista di punti salienti dall'articolo.
    Parametri:
        article_text (str): Il testo dell'articolo da riassumere.
        openai_api_key (str): La chiave API OpenAI da usare.
        model (str): Il modello OpenAI da utilizzare.
    Restituisce:
        lista di punti salienti, oppure None in caso di errore.
    """
    openai.api_key = openai_api_key

    prompt = (
        "Leggi attentamente il seguente articolo e fornisci un elenco puntato "
        "dei punti salienti, ciascuno in una sola frase chiara. "
        "Rispondi in lingua italiana, solo con i punti salienti, senza altri commenti.\n\n"
        f"Articolo:\n{article_text}\n\nPunti salienti:"
    )

    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Sei un assistente che crea riassunti chiari e concisi."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,
            max_tokens=512,
        )
        content = response.choices[0].message.content.strip()
        # Cerca di estrarre i punti come una lista
        bullets = []
        for line in content.split('\n'):
            line = line.strip('-•* \n\t')
            if line:
                bullets.append(line)
        # Alcune volte il modello può restituire tutto su una riga
        if len(bullets) <= 1:
            # Prova a splittare su numeri o punti
            import re
            rough_points = re.split(r'\d+\.\s+|- |\• |\* ', content)
            bullets = [p.strip() for p in rough_points if p.strip()]
        return bullets
    except Exception as e:
        st.error(f"Errore durante la richiesta a OpenAI: {str(e)}")
        return None

# ----------- FRONTEND STREAMLIT -----------

def main():
    st.set_page_config(page_title="Articoli in Pillole con GPT-4.1", page_icon="📝")
    st.title("📝 Articoli in Pillole")
    st.markdown("""
        Inserisci qui sotto il testo di un articolo: otterrai una lista di punti salienti generata dall'Intelligenza Artificiale (GPT-4.1 via API OpenAI).
    """)

    # Gestione API Key
    openai_api_key = config("OPENAI_KEY")
    use_env_key = openai_api_key is not None

    if not use_env_key:
        openai_api_key = st.text_input(
            "Inserisci la tua OpenAI API key (non verrà salvata):",
            type="password",
            help="La tua API Key non viene memorizzata."
        )

    # Input testo articolo
    article_text = st.text_area(
        "Testo dell'articolo",
        height=300,
        placeholder="Incolla qui il testo dell'articolo da riassumere..."
    )

    # Parametri opzionali
    num_points = st.slider("Numero massimo di punti salienti", 3, 10, 5)

    if st.button("Genera Riassunto") and article_text.strip():
        if not openai_api_key or not openai_api_key.startswith("sk-"):
            st.warning("Devi fornire una OpenAI API key valida.")
            st.stop()

        with st.spinner('Sto generando i punti salienti...'):
            bullets = generate_bullet_points(article_text, openai_api_key)
            if bullets:
                # Mostra i punti
                st.success("Punti salienti generati:")
                for idx, point in enumerate(bullets[:num_points], 1):
                    st.markdown(f"- **{point}**")
            else:
                st.warning("Non sono stati trovati punti salienti, riprova con un testo più lungo o controlla la API key.")

    st.markdown("---")
    st.markdown(
        """
        <sub>
        App realizzata con ❤️ usando OpenAI e Streamlit.
        </sub>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
