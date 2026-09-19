
def chatbot():
    print("=== Basic Chatbot ===")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hello! How can I help you?")

        elif user_input == "how are you":
            print("Bot: I am fine! Thank you.")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()