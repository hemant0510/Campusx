from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

load_dotenv()

st.header("Research Tool")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


template = load_prompt('template.json')



# #user_input = st.text_input("Enter your prompt")

model = ChatOpenAI(model='gpt-4')

if st.button('Summarize'):
    chain = template | model
    response = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })
    # prompt = template.invoke({cd P    
    #     "paper_input": paper_input,
    #     "style_input": style_input,
    #     "length_input": length_input
    # })
    # response = model.invoke(prompt)
    st.write(response.content)

# model = ChatOpenAI(model='gpt-4')

# response = model.invoke("Write a 5 line poem on cricket")
