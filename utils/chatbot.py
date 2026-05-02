import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

MODEL_NAME = "openai/gpt-oss-120b:free"

def get_ai_response(user_query):

    prompt = f"""
    You are an AI Enquiry Assistant for a professional training institute.

    Your responsibilities:
    - Answer student queries professionally
    - Be concise and helpful
    - Encourage further interaction
    - Sound natural and conversational

    User Query:
    {user_query}
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