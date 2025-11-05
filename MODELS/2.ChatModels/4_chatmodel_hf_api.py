from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id='MiniMaxAI/MiniMax-M2',
                          task='text-generation')

model = ChatHuggingFace(llm=llm)

repsonse = model.invoke("What is the capital of India?")

print("Response from HuggingFace", repsonse.content)