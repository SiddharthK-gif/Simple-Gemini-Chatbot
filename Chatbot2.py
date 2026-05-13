from langchain.agents import create_agent
from google import genai

client = genai.Client(api_key="AIzaSyBQub2quBscuXJ1CIjEyu88nZ_cFhpze7A")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=input("Enter your prompt:  ")
)
print(response.text)
