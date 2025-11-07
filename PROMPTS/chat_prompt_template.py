from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages([
    ('system', "You are a helful {domain} expert assistant."),
    ('human', "Explain in simple terms, what is {topic}.")])

response = chat_template.invoke({'domain': 'cricket', 'topic': 'LBW'})

print(response)