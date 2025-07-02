import streamlit as st
from utils import classify_text

st.set_page_config(page_title="Text Classifier", page_icon="🧠")

st.title("🧠 Text Classifier using LangChain + Cohere")

st.markdown("Classifies input text based on:")
st.markdown("""
- **Sentiment** (Positive, Negative, Neutral)  
- **Language** (English, Hindi, etc.)  
- **Style** (Formal, Informal, Sarcastic...)  
- **Covered Topics** (Tech, Politics, Health...)  
- **Political Tendency** (Left, Right, Neutral)
""")

user_input = st.text_area("✍️ Enter text here:")

if st.button("🔍 Classify"):
    if user_input.strip():
        with st.spinner("Classifying..."):
            result = classify_text(user_input)
        if result:
            st.success("✅ Classification Result:")
            st.write(f"**Sentiment**: {result.get('sentiment', 'N/A')}")
            st.write(f"**Language**: {result.get('language', 'N/A')}")
            st.write(f"**Style**: {result.get('style', 'N/A')}")
            st.write(f"**Topics**: {', '.join(result.get('topics', [])) if result.get('topics') else 'N/A'}")
            st.write(f"**Political Tendency**: {result.get('political_tendency', 'N/A')}")
        else:
            st.error("❌ Failed to classify the text. Check API key or try again.")
    else:
        st.warning("Please enter some text before clicking classify.")
