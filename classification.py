import streamlit as st
import google.generativeai as genai
import os


def run():
    genai.configure(api_key="AIzaSyAaZ16CjIRJ91Uu5x1G9aEGQS2a7qomQ4I")
    model=genai.GenerativeModel('gemini-1.5-flash')

    st.title("🏷️Text Classification")
    user_query=st.text_area("enter the text")

    prompt=f"""" you are an smart ai text classifier your job is to classify the {user_query} based on the content in the text you need to label the text
    based on the {user_query} .and the output format sholud be in the table format that one table header contains text and the other sholud contain the label
    """
    if st.button("classify"):
        if user_query=='':
            st.warning("Enter the Text to Classify")
        else:
            response=model.generate_content(prompt)
            response=response.text.strip()
            st.write(response)