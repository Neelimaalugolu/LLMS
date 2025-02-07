import streamlit as st
import google.generativeai as genai
import os

def run():
    genai.configure(api_key="AIzaSyAaZ16CjIRJ91Uu5x1G9aEGQS2a7qomQ4I")
    model=genai.GenerativeModel('gemini-1.5-flash')

    st.title("🧠Sentiment Analysis")

    review_type = st.selectbox("Which type of review would you like to analyze?", 
                           ["🍔 Food Review", "🎬 Film Review"])
    


    user_input=st.text_area(f"enter your {review_type} ")


            
    

    
    prompt1=f'''you are an advanced ai sentiment analyzer you analyze the food reviews your job is to analyze the review and tell it was positive or negative or neutral
    as it is a food review if user input was like good ,excellent ,tasty like positive words you may give positive review . 
    if the review was like bad ,faul smell,not tasty,bad cook means give negative  .
    if the review contains both good and bad sentences then give them as neutral review  
    i want output in strictly json format l
    user input : {user_input}  '''

    prompt=f'''you are an advanced ai sentiment analyzer you analyze the film reviews your job is to analyze the review and tell it was positive or negative or neutral
    as it is a film review if user input was like good ,excellent ,fine , nice,hit,superhit like positive words you may give positive review . 
    if the review was like bad ,worst film,no comedy,bad direction means give negative  .
    if the review contains both good and bad sentences then give them as neutral review .
    give me output as neutral if you cannot distinguish the review either good or bad. 
    i want output in strictly json format 
      
    user input :{user_input}  '''

   
    if st.button('Analyze'):

   
        if review_type=="🍔 Food Review":
        
            response=model.generate_content(prompt1)
            response=response.text.strip()
            st.write(response)
        else:

            response=model.generate_content(prompt)
            response=response.text.strip()
            st.write(response)


    # if st.button('Analyze'):
    #     if user_input1=='' or user_input=='':
    #         st.warning('Please enter text to analyze')
    
                

    



