import streamlit as st
import google.generativeai as genai
import os

def run():
    genai.configure(api_key="AIzaSyAaZ16CjIRJ91Uu5x1G9aEGQS2a7qomQ4I")
    model=genai.GenerativeModel('gemini-1.5-flash')

    st.title("📝Text Summariztion")
    
    text_input = st.text_area("enter the text to be summarized")

    prompt=f'''You are an advanced text summarization AI. Your task is to generate a concise and meaningful summary of the given text while preserving key information.  
 
    **Instructions:**  
    - Keep the summary clear and coherent.  
    - Retain all important facts and main points.  
    - Avoid unnecessary details and redundancy.  
    - Use simple and precise language.  
    - Ensure the summary is grammatically correct.  
    -give summarized text with headings with bold text also

        
    **Text to summarize:**  
     {text_input}  


    **Output format:**  
    Provide a well-structured summary in clear sentences.

'''


    if st.button('Summarize'):
        if text_input=='':
            st.warning('Please enter text to summarize')
        else:
        
            response=model.generate_content(prompt)
            response=response.text.strip()
            st.write(response)



