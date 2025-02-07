import streamlit as st
import app  
import app1 
import app2 
import spam
import summarize
import sentiment
import translator
import spelling,speech,classification,content
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Multi-App Dashboard", page_icon="🚀", layout="wide")

# Custom CSS for better UI
st.markdown(
    """
    <style>
        /* Sidebar background */
        [data-testid="stSidebar"] {
            background-color: #050505;
        }

        /* Sidebar text color */
        [data-testid="stSidebar"] * {
            color: white;
        }

        /* Main title styling */
        h1 {
            color: #2C3E50;
            text-align: center;
        }

        /* Style for the option menu items */
        .menu-item {
            padding: 15px;
            font-size: 18px;
            text-align: center;
            background-color: #2E4053;
            border-radius: 10px;
            color: white;
        }

        /* Active menu item color */
        .menu-item.active {
            background-color: #D32F2F;
            color: white;
        }

        /* Hover effect */
        .menu-item:hover {
            background-color: #3b4f5b;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar navigation using option_menu
with st.sidebar:
    selected_app = option_menu(
        menu_title="Home",
        options=["📊Data Extraction", "🤖Chatbot", "💬Single file chatbot","📩⚠Spam Classifier","📝Text summarizer","🧠Sentiment Analysis","🌍Language Translator",
                 "✍️Spelling Correction","🗣️Speech Recognition","🏷️Text Classification","📝Content Creator"],

        icons = ["ABC","ABC","ABC","ABC","ABC","ABC","ABC","ABC","ABC","ABC","ABC"],

        menu_icon="cast",  # Sidebar icon
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#050505"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"font-size": "15px", "color": "white", "padding": "10px"},
            "nav-link-selected": {"background-color": "#f57fa8", "color": "white"},
            "menu-title": {"color": "white", "font-size": "22px", "font-weight": "bold"}
        }
    )

# Main content based on selected app
if selected_app == "📊Data Extraction":
    app.main()  

elif selected_app == "🤖Chatbot":
    app1.run() 

elif selected_app == "💬Single file chatbot":
    app2.run()  

elif selected_app == "📩⚠Spam Classifier":
    spam.run()

elif selected_app == '📝Text summarizer':
    summarize.run()

elif selected_app =="🧠Sentiment Analysis":
    sentiment.run()
elif selected_app == "🌍Language Translator":
    translator.run()

elif selected_app=="✍️Spelling Correction":
    spelling.run()

elif selected_app=="🗣️Speech Recognition":
    speech.run()

elif selected_app=="🏷️Text Classification":
    classification.run()
elif selected_app=="📝Content Creator":
    content.run()

