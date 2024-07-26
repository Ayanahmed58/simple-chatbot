
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('SimpleBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the English corpus data
trainer.train('chatterbot.corpus.english')

print("Chatbot is ready to talk!")

# Function to interact with the chatbot
def chat():
    print("You can start chatting with the bot now. Type 'exit' to stop.")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

# Start chatting with the bot
chat()
