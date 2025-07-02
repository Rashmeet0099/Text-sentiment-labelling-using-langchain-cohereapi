import os
from dotenv import load_dotenv
from langchain_core.runnables import Runnable
from langchain_core.output_parsers import JsonOutputParser
from langchain_cohere import ChatCohere
from prompt_templates import classification_prompt

load_dotenv()

llm = ChatCohere(
    cohere_api_key=os.getenv("COHERE_API_KEY"),
    model="command-r-plus"
)

parser = JsonOutputParser()

# Chain: Prompt → LLM → JSON Parser
chain = classification_prompt | llm | parser
