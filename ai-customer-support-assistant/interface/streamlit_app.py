import streamlit as st
import openai

st.title("Customer Support Assistant Demo")

query = st.text_input("Ask a question (e.g., Where is my order?)")

if st.button("Submit"):
    if query:
        st.write("🤖 Simulated response:")
        st.write(f"Sure! Please share your order number so I can look it up for you.")

