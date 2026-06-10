# Basic Chat Application

print("=== Simple Chat Application ===")
print("Type 'exit' to end the chat.\n")

while True:
    user1 = input("User 1: ")

    if user1.lower() == "exit":
        print("Chat ended.")
        break

    user2 = input("User 2: ")

    if user2.lower() == "exit":
        print("Chat ended.")
        break