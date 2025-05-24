from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os
def chatWithAiAgent(prompt):
    # Set the OpenRouter API key
    os.environ["OPENAI_API_KEY"] = "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"
    # Set OpenRouter as the endpoint
    chat = ChatOpenAI(base_url="https://openrouter.ai/api/v1",model="mistralai/mistral-7b-instruct")
    # Send a message
    messages = [HumanMessage(content=prompt)]
    response = chat.invoke(messages)
    return response.content

time = 1
#build chat agent
while True:
    if time > 1:
        choice = input('click (0) to exit :')
        if choice == '0':
            break
    time +=1
    prompt = input('Enter Your Question Here : ')
    try:
        response = chatWithAiAgent(prompt)
        print(response)
        print('='*100)
    except :
        print('Error to get response')