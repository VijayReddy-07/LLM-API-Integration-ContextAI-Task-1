🤖 ContextAI – Intelligent Multi-Turn AI Chatbot

An intelligent AI-powered chatbot built using Python, Google Gemini API, and Streamlit. ContextAI supports multi-turn conversations, maintains conversation history, and generates real-time streaming responses using a Large Language Model (LLM).

🚀 Project Overview

ContextAI is designed to provide an interactive conversational experience using Google's Gemini API. Unlike a basic chatbot, it maintains previous conversation context, allowing users to ask follow-up questions without repeating information.

The application also implements context window management, system instructions, streaming responses, and error handling.

✨ Features

LLM API Integration: Connects to Google's Gemini API for intelligent response generation.

Multi-Turn Conversations: Maintains conversation history throughout the session.

Context Window Management: Retains the last 10 messages to manage conversation context.

Custom System Prompt: Defines the chatbot's role, personality, and response behaviour.

Streaming Responses: Displays AI-generated responses in real time.

Error Handling: Handles API failures and displays user-friendly error messages.

Secure API Key Management: Stores API credentials in environment variables using .env.

Clear Conversation: Allows users to reset their conversation history.

Interactive Interface: Provides a simple and user-friendly Streamlit interface.

🛠️ Technology Stack

Technology

Purpose

Python

Backend programming

Google Gemini API

AI response generation

Google Gen AI SDK

Gemini API integration

Streamlit

Frontend interface

Python-dotenv

Environment variable management

Git & GitHub

Version control

📁 Project Structure

ContextAI/
│
├── app.py              # Streamlit application
├── chatbot.py          # Gemini API integration
├── .env                # API key configuration
├── .gitignore          # Excluded files
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation

⚙️ Installation and Setup

1. Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL

Navigate to the project directory:

cd ContextAI

2. Create a Virtual Environment (Recommended)

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

3. Install Dependencies

python -m pip install -r requirements.txt

4. Configure Gemini API Key

Get your Gemini API key from:

https://aistudio.google.com/apikey

Create a .env file in the project root directory.

Add the following configuration:

GEMINI_API_KEY="YOUR_GEMINI_API_KEY"

Important: Never share or upload your actual API key to GitHub.

5. Run the Application

Execute the following command:

python -m streamlit run app.py

The application will open in your browser:

http://localhost:8501

🧠 How It Works

The user enters a message through the Streamlit chat interface.

The application retrieves the previous conversation history.

The latest user message is added to the conversation context.

Context management retains the last 10 messages.

The conversation and custom system prompt are sent to the Gemini API.

Gemini generates a response using streaming.

The generated response is displayed in the chat interface.

The conversation is saved in Streamlit session state for subsequent messages.

💬 Example Conversation

User:
My name is Vijay. I am learning Python.

ContextAI:
Hello Vijay! Great to meet you. Python is an excellent programming language for beginners.

User:
What is a Python variable?

ContextAI:
A variable is a named storage location used to store information in Python.

User:
What is my name, and which programming language am I learning?

ContextAI:
Your name is Vijay, and you are learning Python!

This demonstrates how ContextAI uses previous conversation messages to answer follow-up questions.

🔐 Security

API keys are stored in environment variables.

The .env file is excluded from Git tracking.

API credentials are never hardcoded into application source files.

📌 Internship Task Details

Task: AI-1 – LLM API Integration

Project: ContextAI – Intelligent Multi-Turn AI Chatbot

Objective: Build a chatbot integrated with a real LLM API that maintains multi-turn conversation history and implements context window management.

LLM Provider: Google Gemini API