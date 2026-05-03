import streamlit as st
from utils.chatbot import get_ai_response
from utils.lead_scoring import detect_lead_intent
from utils.database import insert_lead

def load_css():

    with open("assets/styles.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# Page configuration
st.set_page_config(
    page_title="AI Enquiry Assistant",
    page_icon="🤖",
    layout="wide"
)

with st.sidebar:

    st.title("🤖 AI Enquiry Assistant")

    st.markdown("""
    ### Features
    - AI Chatbot
    - RAG Retrieval
    - Lead Capture
    - Analytics Dashboard
    - Conversational Memory
    """)

    st.divider()

    st.info(
        "Built using Streamlit, OpenRouter, and Retrieval-Augmented Generation."
    )

# Title
st.title("🤖 AI-Powered Enquiry Assistant")

st.markdown("""
Welcome to the intelligent student enquiry platform.

This assistant can:
- Answer course-related questions
- Recommend learning paths
- Provide placement and curriculum information
- Help students explore AI programs
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Courses Offered", 6)

with col2:
    st.metric("Placement Support", "Yes")

with col3:
    st.metric("AI Assistance", "24/7")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "show_lead_form" not in st.session_state:
    st.session_state.show_lead_form = False

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

    if detect_lead_intent(user_input):
        st.session_state.show_lead_form = True

    # Generate AI response
    chat_history = st.session_state.messages

    ai_response = get_ai_response(
        user_input,
        chat_history
    )

    # Store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(ai_response)

# -----------------------------
# Lead Capture Form
# -----------------------------

if st.session_state.show_lead_form:

    st.divider()

    st.subheader("📩 Interested in Learning More?")

    with st.form("lead_form"):

        name = st.text_input("Full Name")

        email = st.text_input("Email Address")

        phone = st.text_input("Phone Number")

        interested_course = st.selectbox(

            "Interested Course",

            [
                "AI Foundations",
                "Machine Learning Bootcamp",
                "Data Science Professional",
                "NLP Specialization",
                "Python for AI",
                "Generative AI Engineering"
            ]
        )

        submit_button = st.form_submit_button("Submit")

        if submit_button:

            lead_score = 50

            insert_lead(
                name,
                email,
                phone,
                interested_course,
                lead_score
            )

            st.success(
                "Your details have been submitted successfully!"
            )

            st.session_state.show_lead_form = False