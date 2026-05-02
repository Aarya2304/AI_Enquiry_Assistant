import streamlit as st
from utils.chatbot import get_ai_response

# Page configuration
st.set_page_config(
    page_title="AI Enquiry Assistant",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 AI Enquiry Assistant")
st.markdown("Ask me anything about our courses and programs!")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your question here...")

if user_input:

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    ai_response = get_ai_response(user_input)

    # Store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(ai_response)