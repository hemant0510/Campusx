from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)


documents = ["Delhi is the capital of India.",
             "Paris is the capital of France.",
             "Kolkata is the capital of West Bengal."]

reponse = embeddings.embed_documents(documents)

print("Embedding from OpenAI Model", str(reponse))