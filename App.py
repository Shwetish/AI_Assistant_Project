import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Streamlit Page
st.set_page_config(page_title="AI Productivity Assistant", page_icon="🤖")
st.title("🤖 AI-Powered Productivity Assistant")

# Check for API key
if not api_key:
    st.error("API Key not found! Please check that your .env file exists in the project folder.")
    st.stop()

# Initialize Gemini Client
client = genai.Client(api_key=api_key)

# Sidebar for Task Selection
task = st.sidebar.selectbox(
    "Choose a Task:",
    ["Summarize Text", "Answer Questions", "Generate Content", "Analyze Text"]
)

st.subheader(f"Task: {task}")
user_input = st.text_area("Enter your text or prompt here:", height=150)

# Process User Request
if st.button("Generate Response"):
    if not user_input.strip():
        st.warning("Please enter some text before clicking Generate.")
    else:
        if task == "Summarize Text":
            prompt = f"Please provide a concise summary of the following text:\n\n{user_input}"
        elif task == "Generate Content":
            prompt = f"Write professional content based on this topic/instructions:\n\n{user_input}"
        elif task == "Analyze Text":
            prompt = f"Analyze the following text and list key insights, action items, or bullet points:\n\n{user_input}"
        else:
            prompt = user_input

        with st.spinner("AI is thinking..."):
            try:
               response = client.models.generate_content(
                  model="gemini-3.6-flash",
                  contents=prompt
)
               st.success("Completed!")
               st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")