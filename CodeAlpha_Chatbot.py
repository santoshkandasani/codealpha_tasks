while True:


    user = input("You: ").lower()
    if user == "hello":
        print("Bot: Hi!")
    elif user == "how are you":
        print("Bot: I'm fine, thanks!")
    elif user == "what is your name":
        print("Bot: I'm a simple chatbot.")
    elif user == "who created you":
        print("Bot: A programmer created me.")
    elif user == "what are you doing":
        print("Bot: Just chatting with you.")
    elif user == "thank you":
        print("Bot: You're welcome!")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand.")
