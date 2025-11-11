from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI()

class ResponseModel(TypedDict):
    name: str
    color: str
    number: int

structured_model = model.with_structured_output(ResponseModel)

response = structured_model.invoke("The best fruit to eat in summers is Mango which is a national food of India. We should eat atleast 2 mango's a day in summer to stay healthy.")

print(response)