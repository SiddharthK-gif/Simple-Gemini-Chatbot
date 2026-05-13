# Simple-Gemini-Chatbot
from langchain.agents import create_agent

agent = create_agent(
    model="google_genai:gemini-2.5-flash-lite",
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": input("Enter your prompt:")}]}
)
print(result["messages"][-1].content_blocks)
