from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os

# Set the OpenRouter API key
os.environ["OPENAI_API_KEY"] = "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"

# Set OpenRouter as the endpoint
chat = ChatOpenAI(base_url="https://openrouter.ai/api/v1",model="mistralai/mistral-7b-instruct")
prompt = input('Enter Your Question Here : ')
# Send a message
messages = [HumanMessage(content=prompt)]
response = chat.invoke(messages)

# Print the output
print(response.content)
