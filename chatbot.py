
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Gemini API key is missing.")

client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = """
You are ContextAI, an intelligent and friendly AI assistant.

Your responsibilities:
1. Answer questions clearly.
2. Remember previous conversation context.
3. Explain technical concepts simply.
4. Help users with programming and learning.
5. Be professional, accurate and helpful.
6. Respond directly to the latest message; do not repeat earlier answers unless asked.
"""

def generate_response_stream(messages):
    conversation = SYSTEM_PROMPT + "\n\n"

    for message in messages:
        role = message["role"]
        content = message["content"]
        conversation += f"{role}: {content}\n"

    for chunk in client.models.generate_content_stream(
        model="gemini-flash-lite-latest",
        contents=conversation
    ):
        if chunk.text:
            yield chunk.text
