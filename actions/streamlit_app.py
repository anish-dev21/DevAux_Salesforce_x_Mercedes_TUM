import streamlit as st
import requests
import json

# Title of the web app
st.title('Chatbot with Rasa')

# Text box for user input
user_input = st.text_input("Talk to the chatbot:")

# Function to send the user message to Rasa and get the response
def send_message(sender, message):
    url = 'http://localhost:5005/webhooks/rest/webhook'
    payload = {
        "sender": sender,
        "message": message
    }
    response = requests.post(url, json=payload)
    return response.json()

# Display user input and bot response in Streamlit
if user_input:
    # Send message
    responses = send_message("user", user_input)
    # Display bot response
    if responses:
        for response in responses:
            if 'text' in response:
                st.text_area("Bot says:", value=response['text'], height=200, max_chars=None, key=None)