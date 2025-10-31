### NO NEED TO RUN THIS FILE ###

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(model_id='MiniMaxAI/MiniMax-M2',
                                    task='text-generation',
                                    pipeline_kwargs={
                                        'max_new_tokens': 100, 
                                        'temperature': 0.5
                                        }
                                    )


model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of India?")    
print("Response from HuggingFace Local Model", response.content)