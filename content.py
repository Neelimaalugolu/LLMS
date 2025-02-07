import streamlit as st
import google.generativeai as genai
import os

def run():
    genai.configure(api_key="AIzaSyAaZ16CjIRJ91Uu5x1G9aEGQS2a7qomQ4I")
    model=genai.GenerativeModel('gemini-1.5-flash')

    st.title("📝Content Generation")


    user_query=st.text_input("Enter the Topic")
    user_query1=st.text_area("Enter Any Specifications")

    prompt=f"""
            you are an smart AI content creator or generator you work is to create content based on the given  context:{user_query} and also
            based on the specifications:{user_query1} entered by the user.the conetent sholud be more precise
            and meaningful and relevant content
    """

    if st.button("Generate"):
        if user_query and user_query1 =='':
            st.warning("enter the text to create content")
        else:
            response=model.generate_content(prompt)
            response=response.text.strip()
            st.write(response)