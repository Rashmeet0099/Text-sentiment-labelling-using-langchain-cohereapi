# Text Classifier using LangChain + Gemini

## Features
- Classifies text based on:
  - Sentiment
  - Language
  - Style
  - Topics
  - Political Tendency

## Tech Stack
- Python
- LangChain
- Google Gemini API

## Setup
1. Clone repo and install requirements
2. Add your Gemini API Key to `.env`
3. Run `main.py`

## Run Example
```bash
python main.py

       +-----------------+
       |    app.py       |  <- Streamlit frontend
       +-----------------+
               |
               v
       +-----------------+
       |   utils.py      |  <- classify_text() function
       +-----------------+
               |
               v
       +------------------------+
       |  classifier_chain.py   |  <- LLM Chain definition
       +------------------------+
         |          |         |
         v          v         v
  .env (API)  prompt_templates.py  ChatCohere (LangChain)
     |               |                 |
     +---------------+-----------------+
                     |
                     v
            +------------------+
            | JSON classification |
            +------------------+

