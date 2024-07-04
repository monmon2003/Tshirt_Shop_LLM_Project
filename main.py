from langchain_helper import *

import streamlit as st

st.title("T-Shirts: Database Q & A 👕")

question = st.text_input("Question:")
if question:
    chain = get_few_shot_db_chain()
    answer = chain.invoke(question)["result"]
    st.header("Answer: ")
    st.write(answer)