from openai import OpenAI

# 🔑 Your API Key here
client = OpenAI(api_key="YOUR_API_KEY")

print("🤖 AI Chatbot started (type 'exit' to stop)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Bye 👋")
        break

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    bot_reply = response.choices[0].message.content
    print("Bot:", bot_reply)