import streamlit as st
import google.generativeai as genai
import os

def run():
    genai.configure(api_key="AIzaSyAaZ16CjIRJ91Uu5x1G9aEGQS2a7qomQ4I")
    model=genai.GenerativeModel('gemini-1.5-flash')

    st.title("✍️Spelling Correction")

    user_query=st.text_area("enter the text to be corrected")

    prompt=f""" Please review the following text for spelling and grammar errors and provide corrections.
      Ensure the text maintains its intended meaning and flow while improving clarity, sentence structure, and correctness."
      text:{user_query}
output_format: greetings first and the following sentence has mistake and also what are the mistakes are also should be displayed and then the corrected sentence will be given
"""

    if st.button("Correct"):
        if user_query=='':
            st.warning("enter the text to be corrected")
        else:
            response=model.generate_content(prompt)
            response=response.text.strip()
            st.write(response)