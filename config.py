import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
OPENAI_KEY = os.environ.get("API_KEY")
PINECONE_KEY = os.environ.get("PINECONE_KEY")