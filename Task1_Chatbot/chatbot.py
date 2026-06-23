print("AI Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How are you?")
    elif "your name" in user:
        print("Bot: I am a simple AI Chatbot.")
    elif "ai" in user:
        print("Bot: AI stands for Artificial Intelligence.")
    elif "how are you" in user:
        print("Bot: I am doing great!")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")
