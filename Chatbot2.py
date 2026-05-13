# in the powershell, enter your API Key in the environment
import os
from langchain.agents import create_agent

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise EnvironmentError("GOOGLE_API_KEY is not set in the environment.")

agent = create_agent(
    model="google_genai:gemini-2.5-flash-lite",
    system_prompt="You are a helpful assistant",
)

prompt = input("Enter your prompt: ")

try:
    result = agent.invoke(
        {"messages": [{"role": "user", "content": prompt}]}
    )
    message = result["messages"][-1]
    output = getattr(message, "content_blocks", None) or getattr(message, "content", None) or message
    print(output)
except Exception as exc:
    print("Error invoking the agent:", exc)
