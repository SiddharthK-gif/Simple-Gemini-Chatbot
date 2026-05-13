# Simple-Gemini-Chatbot
from langchain.agents import create_agent
from google import genai

client = genai.Client(api_key="your_api_key")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=input("Enter your prompt:  ")
)
print(response.text)
