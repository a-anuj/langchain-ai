import streamlit as st
import os
from langchain_huggingface import HuggingFaceEndpoint

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

def load_answer(question):
    llm = HuggingFaceEndpoint(
        model="mistralai/Mistral-7B-Instruct-v0.3",
        temperature=0.7  # Ensure temperature is positive
    )
    response = llm.invoke(question)
    return response

st.set_page_config(page_title="Langchain-Q/A App", page_icon=":robot:")
st.header("Langchain-Q/A App")

def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text.strip()  # Remove unnecessary spaces

user_input = get_text()
submit = st.button("Generate")

if submit:
    if user_input:  # Ensure input is non-empty
        try:
            response = load_answer(user_input)
            st.subheader("Answer : ")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a valid question.")
