import time

print("==================================")
print("     WELCOME TO AI CHATBOT       ")
print("==================================")
print("Type 'exit' or 'bye' to stop the chat.\n")
#response to chatbot
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! How are you?",
    "how are you": "I'm just a Python bot, but I'm doing great!",
    "what is your name": "I am a simple Python Chatbot built for my internship.",
    "python": "Python is a great programming language to learn!",
    "bye": "Goodbye! Have a great day ahead!",
    "what is your purpose": "I am here to assist you with basic queries and have a friendly chat.",
    "first law of thermodynamics": "The first law of thermodynamics states that energy cannot be created or destroyed, only transformed from one form to another.",
    "second law of thermodynamics": "The second law of thermodynamics states that the total entropy of an isolated system can never decrease over time, and is constant if and only if all processes are reversible.",
    "third law of thermodynamics": "The third law of thermodynamics states that the entropy of a perfect crystal approaches zero as the temperature approaches absolute zero.",
}

while True:
    user_input = input("You: ").strip().lower()
    
    if user_input in ["exit", "bye"]:
        print("Bot: Goodbye! Have a nice day!")
        break
        
    reply = responses.get(user_input, "Sorry, I don't understand that yet. Try asking 'hello' or 'how are you'!")
    time.sleep(0.5)
    print(f"Bot: {reply}\n")