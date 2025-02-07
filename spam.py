import streamlit as st
import google.generativeai as genai
import os

def run():

    genai.configure(api_key="AIzaSyAaZ16CjIRJ91Uu5x1G9aEGQS2a7qomQ4I")
    model=genai.GenerativeModel('gemini-1.5-flash')

    st.title("📩Email-Spam Classifier")
    
    user_query = st.text_area("enter the email content")

    prompt=f'''
    you are a smart email spam classifier. you need to analyze the email body and classify the email as either it is spam or not spam.
    if it contains any words like free,reward,cashprize,urgent,claim now free webinar classify them as spam mails
    if it contains regular,proffesional without spam characteristics classify it as not spam.
    return the response in a json format 
    here is the email body {user_query}
'''
    if st.button('Detect'):
        if user_query=='':
            st.warning('Please enter email body')
        else:
            response=model.generate_content(prompt)
            response=response.text.strip()
            st.write(response)

