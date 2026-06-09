print("🤖 Chatbot: Hello! நான் ஒரு simple chatbot 😊")
print("Type 'exit' to stop")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hi! எப்படி இருக்கீங்க?")

    elif "how are you" in user:
        print("Bot: நான் நல்லா இருக்கேன் 😊 நீங்க எப்படி?")

    elif "your name" in user:
        print("Bot: என் பெயர் PyBot 🤖")

    elif "bye" in user:
        print("Bot: Bye! நல்ல நாள் வாழ்த்துக்கள் 👋")
        break

    elif user == "exit":
        print("Bot: Exit ஆகிறது...")
        break

    else:
        print("Bot: மன்னிக்கவும், எனக்கு அது புரியவில்லை 🤔")