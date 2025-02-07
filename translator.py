import streamlit as st
import google.generativeai as genai
import os

def run():
    genai.configure(api_key="AIzaSyAaZ16CjIRJ91Uu5x1G9aEGQS2a7qomQ4I")
    model=genai.GenerativeModel('gemini-1.5-flash')

    st.title("🌍Language Detector and Language Translator")
    task=st.selectbox("Which task you want to perform",['🌐Language Detector','🔄Language Translator'])


    user_query = st.text_area("enter the text")

    if task=="🔄Language Translator":
        source=st.selectbox("enter the source language",['english','telugu','hindi','spanish'])
        destination=st.selectbox("enter the destination language",['english','telugu','hindi','spanish'])
 


    

    
    
    

    if st.button(f"{task}"):
        if user_query=='':
            st.warning("please enter text to generate or translate")
        else:
            if task=="🔄Language Translator":
                if source and destination:
                    prompt=f""" 
                    You are an AI language translator. Translate the following text from its {source} into {destination}. 
                    Provide the translation in plain text.
                    Text: "{user_query}"
                          """
    
                    response=model.generate_content(prompt)
                    response=response.text.strip()
                    st.write(response)
                else:
                    st.warning("please slect source and destination")
            else:
                prompt1=f"""
                You are an AI language detector. Given the following text, identify the language and return it in ISO 639-1 language code format.

                Text: "{user_query}"
                """

                response=model.generate_content(prompt1)
                response=response.text.strip()
                st.write(response)







if __name__=="__main__":
    run()