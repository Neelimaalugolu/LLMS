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

# List of PDFs - PASSED DIRECTLY IN CODE
    pdf_files = "Invoice_1.pdf" # Add all file paths here

    pdf_content = extract_text_from_pdf(pdf_files)
 

  
    st.markdown(
    """
    <style>
        .stChatMessage { padding: 10px; border-radius: 10px; }
        .stChatMessageUser { background-color: #ffebeb; }
        .stChatMessageBot { background-color: #fff4d6; }
        .stTextInput input { border-radius: 20px; padding: 10px; }
    </style>
    """,
    unsafe_allow_html=True
)
    st.markdown("<h1 style='text-align: center;'>📜 ChatGPT-like PDF Chatbot</h1>", unsafe_allow_html=True)

    if "chat_history1" not in st.session_state:
        st.session_state.chat_history1 = []

    for role, text in st.session_state.chat_history1:
        with st.chat_message("assistant" if role == "Bot" else "user"):
            st.write(text)

    # User input for queries
    user_query = st.chat_input("Ask something about the invoices...")

    if user_query:
          
        structured_prompt = "Use the following PDF content to answer the user's question: {pdf_content}"
      
        chat_history1 = "\n".join([f"User: {q}\nBot: {a}" for q, a in st.session_state.chat_history1[-5:]]) 


        structured_prompt += f"""
        User question: {user_query}

       ### PDF Content:
\"\"\"{pdf_content}\"\"\"

**Instructions:**
- Consider the chat history and previous responses while answering.
- If the previous response referred to specific content in the PDF, prioritize details from that PDF in the next answer.
- If the user asks follow-up questions (e.g., "Give me its order number"), understand "its" based on the previous answer.
- If the answer is found in the PDF content, mention that the information was found in the uploaded document.
- If the query is unrelated to the PDF content, reply: "I don't know, as this information is not in the uploaded document."
- If the query is not meaningful, reply: "Please give a valid query."
- For greetings like "hi" or "hello," respond with a friendly greeting like "Hi! How can I assist you today?"

Chat History:
{chat_history1}
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