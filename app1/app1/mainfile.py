import streamlit as st
import os
from langchain_openai import OpenAI

os.environ["OPENAI_API_KEY"] = "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"

def load_answer(question):
    llm = OpenAI(
        model_name="gpt-3.5-turbo-instruct",
        temperature=0  # Ensure temperature is positive
    )
    response = llm.invoke(question)
    return response

st.set_page_config(page_title="Langchain-Q/A App", page_icon=":robot:")
st.header("Langchain-Q/A App")

def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text

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
