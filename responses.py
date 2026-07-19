import random

# Dictionary of intents with keywords and responses
BOT_RESPONSES = {

    "greeting": {
        "keywords": [
            "hi", "hello", "hey", "good morning",
            "good afternoon", "good evening", "hola"
        ],
        "responses": [
            "Hello! How can I help you today?",
            "Hi there! Nice to meet you.",
            "Hey! What can I do for you?",
            "Greetings! How may I assist you?"
        ]
    },

    "how_are_you": {
        "keywords": [
            "how are you",
            "how are things",
            "how do you do",
            "are you fine"
        ],
        "responses": [
            "I'm doing great. Thanks for asking!",
            "I'm always ready to help.",
            "I'm functioning perfectly!",
            "Doing well! What about you?"
        ]
    },

    "name": {
        "keywords": [
            "your name",
            "who are you",
            "what is your name",
            "introduce yourself"
        ],
        "responses": [
            "My name is SmartBot.",
            "I'm SmartBot, your AI assistant.",
            "You can call me SmartBot."
        ]
    },

    "creator": {
        "keywords": [
            "who created you",
            "who made you",
            "developer",
            "creator"
        ],
        "responses": [
            "I was created using Python by my developer.",
            "I was developed as a rule-based AI chatbot.",
            "A Python developer created me for learning AI concepts."
        ]
    },

    "python": {
        "keywords": [
            "python",
            "what is python"
        ],
        "responses": [
            "Python is a popular programming language used for AI, web development, automation, and data science.",
            "Python is known for its simple syntax and powerful libraries."
        ]
    },

    "ai": {
        "keywords": [
            "artificial intelligence",
            "ai",
            "what is ai"
        ],
        "responses": [
            "Artificial Intelligence enables machines to perform tasks that normally require human intelligence.",
            "AI includes machine learning, deep learning, NLP, computer vision, and robotics."
        ]
    },

    "machine_learning": {
        "keywords": [
            "machine learning",
            "ml"
        ],
        "responses": [
            "Machine Learning allows computers to learn patterns from data.",
            "Machine Learning is a subset of Artificial Intelligence."
        ]
    },

    "chatbot": {
        "keywords": [
            "chatbot",
            "what is chatbot"
        ],
        "responses": [
            "A chatbot is software that communicates with users through text or voice.",
            "Chatbots can be rule-based or AI-powered."
        ]
    },

    "time": {
        "keywords": [
            "time",
            "current time",
            "what time"
        ],
        "responses": [
            "I can tell the time if the developer connects me with Python's datetime module."
        ]
    },

    "date": {
        "keywords": [
            "date",
            "today",
            "today's date"
        ],
        "responses": [
            "I can tell today's date using Python's datetime module."
        ]
    },

    "college": {
        "keywords": [
            "college",
            "university",
            "student"
        ],
        "responses": [
            "I hope you're enjoying your studies!",
            "Learning programming is a great skill for students."
        ]
    },

    "programming": {
        "keywords": [
            "coding",
            "programming",
            "developer"
        ],
        "responses": [
            "Programming is the process of writing instructions for computers.",
            "Practice coding daily to improve your programming skills."
        ]
    },

    "joke": {
        "keywords": [
            "joke",
            "funny",
            "make me laugh"
        ],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the computer get cold? It forgot to close Windows!",
            "Debugging: Being the detective in a crime movie where you're also the culprit."
        ]
    },

    "motivation": {
        "keywords": [
            "motivate me",
            "motivation",
            "inspire me"
        ],
        "responses": [
            "Success comes from consistent effort.",
            "Every expert was once a beginner.",
            "Keep learning—you'll improve every day!"
        ]
    },

    "thanks": {
        "keywords": [
            "thanks",
            "thank you",
            "thankyou",
            "thx"
        ],
        "responses": [
            "You're welcome!",
            "Happy to help!",
            "My pleasure.",
            "Anytime!"
        ]
    },

    "help": {
        "keywords": [
            "help",
            "commands",
            "options"
        ],
        "responses": [
            """You can ask me about:

• AI
• Python
• Machine Learning
• Programming
• My creator
• My name
• Tell me a joke
• Motivation
• Greetings
• Thanks
• Exit"""
        ]
    },

    "bye": {
        "keywords": [
            "bye",
            "goodbye",
            "exit",
            "quit",
            "see you"
        ],
        "responses": [
            "Goodbye! Have a wonderful day!",
            "See you next time!",
            "Take care!",
            "Bye! Keep learning."
        ]
    }
}


# Default responses for unknown questions
UNKNOWN_RESPONSES = [
    "I'm sorry, I didn't understand that.",
    "Could you please rephrase your question?",
    "I don't have an answer for that yet.",
    "Interesting question! I'm still learning.",
    "Can you ask that in a different way?",
    "I'm not sure about that. Try asking something related to AI, Python, or programming.",
    "Sorry, that's outside my current knowledge.",
    "I couldn't find a matching response."
]


def get_response(user_input):
    """
    Returns an appropriate chatbot response.
    """

    user_input = user_input.lower()

    for intent in BOT_RESPONSES.values():

        for keyword in intent["keywords"]:

            if keyword in user_input:
                return random.choice(intent["responses"])

    return random.choice(UNKNOWN_RESPONSES)