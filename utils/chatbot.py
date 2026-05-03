import os

from dotenv import load_dotenv
from openai import OpenAI

from utils.rag_pipeline import retrieve_context


# -----------------------------
# Load Environment Variables
# -----------------------------

load_dotenv()


# -----------------------------
# OpenRouter Client
# -----------------------------

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


# -----------------------------
# Model
# -----------------------------

MODEL_NAME = "openai/gpt-oss-120b:free"


# -----------------------------
# Generate AI Response
# -----------------------------

def get_ai_response(user_query, chat_history):

    # Retrieve relevant context
    retrieved_context = retrieve_context(user_query)

    conversation_history = ""

    for message in chat_history[-6:]:

        role = message["role"]

        content = message["content"]

        conversation_history += f"{role}: {content}\n"

    prompt = f"""
    You are a professional and friendly AI Enquiry Assistant for a modern AI training institute.

    Your job is to:
    - Answer naturally and conversationally
    - Use the provided context to generate accurate responses
    - Explain things clearly instead of copying raw text
    - Sound like a real student counsellor
    - Encourage users to continue the conversation
    - Be informative but not robotic

    If the answer is not available in the context, politely say:
    "I currently don't have that information, but I’d be happy to connect you with our team."

    -----------------------------
    INSTITUTE CONTEXT:
    -----------------------------

    {retrieved_context}

    -----------------------------
    RECENT CONVERSATION:
    -----------------------------

    {conversation_history}

    -----------------------------
    USER QUESTION:
    -----------------------------

    {user_query}

    Now generate a professional, detailed, conversational response.
    """

    response = client.chat.completions.create(

        model=MODEL_NAME,

        messages=[
            {
                "role": "system",
                "content": "You are a professional AI Enquiry Assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content