from langchain_core.prompts import PromptTemplate

classification_prompt = PromptTemplate.from_template("""
Classify the following text on these parameters:
1. Sentiment (Positive, Negative, Neutral)
2. Language
3. Style (Formal, Informal, Sarcastic, etc.)
4. Covered Topics (e.g., technology, health, politics)
5. Political Tendency (Left, Right, Neutral)

Text:
{text}

Respond in JSON format:
{{
  "sentiment": "...",
  "language": "...",
  "style": "...",
  "topics": ["..."],
  "political_tendency": "..."
}}
""")
