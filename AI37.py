print("🤖 AI Chatbot (type 'bye' to exit)")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! How are you?")
    elif user == "how are you":
        print("Bot: I am fine.")
    elif user == "what is your name":
        print("Bot: My name is AI Bot.")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand.")