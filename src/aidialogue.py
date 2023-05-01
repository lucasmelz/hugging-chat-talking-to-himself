import asyncio
from hugchat import hugchat
chatbot = hugchat.ChatBot()

async def firstResponse(text):
    return chatbot.chat(text)

async def fetchResponse(text, conversation_id):
    chatbot.change_conversation(conversation_id)
    return chatbot.chat(text)

async def main():
    # Start the first conversation
    conv_id1 = chatbot.new_conversation()
    temp = await fetchResponse("Hi, how are you?", conv_id1)
    print("----------------------------------------------------------------")
    print(f"Bot 1: {temp}")
    # Start the second conversation
    conv_id2 = chatbot.new_conversation()
    temp2 = await fetchResponse("Hello, what's up?", conv_id2)
    print("----------------------------------------------------------------")
    print(f"Bot 2: {temp2}")

    while True:
       temp = await fetchResponse(temp2, conv_id1)
       print("-------------------------------------------------------------")
       print(f"Bot 1: {temp}")
       temp2 = await fetchResponse(temp, conv_id2)
       print("-------------------------------------------------------------")
       print(f"Bot 2: {temp2}")

asyncio.run(main())

