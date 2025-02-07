import streamlit as st
import google.generativeai as genai
import fitz
import os

def run():

    genai.configure(api_key="AIzaSyAj3h8XABuMTvD5Eqmj77K0qYWv4bBMJf0")
    model = genai.GenerativeModel("gemini-1.5-flash")

    def extract_text_from_pdf(pdf_path):
        text=""
        reader = fitz.open(pdf_path)
        for page in reader:
            text+=page.get_text("text")
        return text


    pdf_files = ["Invoice_1.pdf", "Invoice_2.pdf", "Invoice_3.pdf","Invoice_4.pdf","Invoice_5.pdf"]  # Add all file paths here

    pdf_texts = {pdf: extract_text_from_pdf(pdf) for pdf in pdf_files}


    st.session_state.pdf_texts = pdf_texts

    st.markdown("<h1 style='text-align: center;'>📜 Multi-PDF Intelligent Chatbot</h1>", unsafe_allow_html=True)


    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    
    for role, text in st.session_state.chat_history:
        with st.chat_message("assistant" if role == "Bot" else "user"):
            st.write(text)

  
    user_query = st.chat_input("Ask something about the invoices...")

    if user_query:
        pdf_texts = st.session_state.pdf_texts 

       
        structured_prompt = "Use the following PDF contents to answer the user's question:\n\n"
        for file_name, content in pdf_texts.items():
            structured_prompt += f"### File: {file_name}\n\"\"\"{content}\"\"\"\n\n"
        
        chat_history = "\n".join([f"User: {q}\nBot: {a}" for q, a in st.session_state.chat_history[-5:]])  


        structured_prompt += f"""
        User question: {user_query}

        **Instructions:**
    - Consider the chat history and previous responses while answering.
    - If the previous response referred to a specific file, prioritize details from that file in the next answer.
    - If the user asks follow-up questions (e.g., "Give me its order number"), understand "its" based on the previous answer.
    - If the answer is found in a specific file, mention that file name in the response.
    - If the query is unrelated to the PDF content, reply: "I don't know, as this information is not in the uploaded documents."
    -if the query is not meaningfull ,reply:"please give valid query."
    - For greetings like "hi" or "hello," respond with a friendly greeting like "Hi! How can I assist you today?".
    Chat History:
    {chat_history}
    """

        response = model.generate_content(structured_prompt)
        answer = response.text.strip()

        with st.chat_message("assistant"):
            st.write(answer)

        # Store chat history
        st.session_state.chat_history.append(("You", user_query))
        st.session_state.chat_history.append(("Bot", answer))
        
if __name__ == "__main__":
    run()