import streamlit as st
import google.generativeai as genai
import json
import re
import fitz
import os

genai.configure(api_key="AIzaSyAaZ16CjIRJ91Uu5x1G9aEGQS2a7qomQ4I")
model=genai.GenerativeModel('gemini-1.5-flash')
 
def pdf_to_text(file_name):
    doc=fitz.open(stream=file_name.read(), filetype="pdf")
    text='\n'.join(page.get_text() for page in doc)
    return text
 
 
def gemini_response(model,prompt,content):
    full_prompt=f"{prompt}\n\nHere is the invoice text:\n{content}"
    response=model.generate_content(full_prompt)
    return response.text
def main():

    st.title("📊Data Extraction")
    
    uploaded_files = st.file_uploader("Upload PDF", type=["pdf"],accept_multiple_files=True)
    
    if uploaded_files:
    
        prompt = """By using the invoice text, provide me the JSON format with the following keys:
                    
                    invoice_details with nested keys as follows: invoice_number, order_number, invoice_date, due_date, total_due
                    sender_details with nested keys as follows: name, address, email
                    recipient_details with nested keys as follows: name, address, email
                    items with nested keys as follows: quantity, service, rate, adjustment, sub_total
                    tax_details with nested keys as follows: tax_amount
                    bank_details with nested keys as follows: bank_name, account_number, bsb_number.
                """
        for uploaded_file in uploaded_files:
    
            file_name=uploaded_file.name
            st.subheader(f"Processing:{file_name}")
    
        
            content=pdf_to_text(uploaded_file)
            st.text_area("Extracted Text from PDF", content, height=250)
            response=gemini_response(model,prompt,content)
    
            match=re.search(r'\{.*\}',response,re.DOTALL)
    
            if match:
                json_content=match.group(0)
    
                try:
                    invoice_data=json.loads(json_content)
                    st.json(invoice_data)
    
                    json_file_name=f"{os.path.splitext(file_name)[0]}.json"
                    with open(json_file_name,'w') as file:
                        json.dump(invoice_data,file,indent=4)
    
                    with open(json_file_name,"r") as json_file:
                        st.download_button(
                            label=f'Download {json_file_name}',
                            data=json_file,
                            file_name=json_file_name,
                            mime='application/json'
                        )
                except json.JSONDecodeError:
                        st.error(f"Error: Could not parse valid JSON from {file_name}.")
    
            else:
                st.error("No valid JSON content found.")
    

if __name__ == "__main__":
    main()