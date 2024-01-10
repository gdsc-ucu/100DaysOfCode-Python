def chatbot(user_input):
    responses = {
        'hello': 'Hi there! How can I assist you?',
        'goodbye': 'Goodbye! Have a great day.',
        'weather': 'My apologize, i am unable to provide real time weather information',
        'default': 'I am not sure how to respond to that. Can you ask me something else?',
    }

    user_input_lower = user_input.lower()
    if 'hello' in user_input_lower:
        return responses['hello']
    elif 'goodbye' in user_input_lower:
        return responses['goodbye']
    elif 'weather' in user_input_lower:
        return responses['weather']
    else:
        return responses['default']

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    bot_response = chatbot(user_input)
    print("Chatbot:", bot_response)


