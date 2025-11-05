from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file
model = ChatAnthropic(model="claude-sonnet-4-5-20250929")

response = model.invoke("What is the capital of India?")

print("Response from Anthropic", response.content)




