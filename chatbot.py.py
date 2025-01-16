import nltk
from nltk.chat.util import Chat, reflections

# Define a set of conversation patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello! How can I assist you today?", "Hey there! How can I help?"]),
    (r"what is your name?", ["I am a chatbot created to help you with any questions you have.", "I'm your friendly chatbot."]),
    (r"how are you?", ["I'm just a bot, but I'm doing great! How about you?", "I'm doing well, thanks for asking!"]),
    (r"what can you do?", ["I can have a conversation, answer simple questions, and assist you with basic tasks.", "I can chat with you and help answer questions!"]),
    (r"bye|goodbye", ["Goodbye! It was nice talking to you.", "Bye! Have a great day!"]),
    (r"my name is (.*)", ["Hello %1, nice to meet you!", "Hi %1! How can I assist you today?"]),
    (r"(.*) (location|city)", ["I don't have a specific location, but I'm available to chat from anywhere!", "I can chat with you no matter where you are."]),
    (r"(.*) (your|you) (like|love) (.*)", ["I'm just a bot, but I guess I 'love' helping people!"]),
    (r"what (.*) your favorite (.*)", ["I don't have preferences, but I enjoy helping you with any question!"]),
    (r"(.*)", ["Sorry, I didn't quite get that. Could you rephrase?", "I didn't understand that. Could you try again?"])
]

# Create the chatbot instance
chatbot = Chat(pairs, reflections)

# Start the conversation
def start_chat():
    print("Hello! I'm your chatbot. Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Goodbye! It was nice talking to you.")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    start_chat()
