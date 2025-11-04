from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = "Delhi is the capital of India."

vector = embedding.embed_query(text)

# FOR DOCUMENTS USE THIS
# documents = ["Delhi is the capital of India.",
#              "Paris is the capital of France.",
#              "Kolkata is the capital of West Bengal."]

# reponse = embeddings.embed_documents(documents)

print("Embedding from HuggingFace Local Model", str(vector))