#  Rule-Based Chatbot

## Project Overview

This project is a simple Rule-Based Chatbot developed using Python. The chatbot responds to user queries based on predefined rules and keyword matching instead of machine learning.

The chatbot can answer common questions related to Artificial Intelligence, Python, Programming, greetings, jokes, motivation, and more.

---

## Features

- Greeting messages
- Responds to common questions
- Keyword-based pattern matching
- Multiple responses for each question
- Randomized replies
- Handles unknown questions gracefully
- Exit command
- Beginner-friendly implementation

---

## Technologies Used

- Python 3
- Random Module

---

## Project Structure

```
RuleBasedChatbot/
│── chatbot.py
│── responses.py
│── README.md
│── requirements.txt
```

---

## How It Works

1. User enters a message.
2. The chatbot converts the message to lowercase.
3. The chatbot searches for matching keywords.
4. If a keyword is found, an appropriate response is returned.
5. If no keyword matches, the chatbot gives a default response.
6. The conversation continues until the user types **bye** or **exit**.

---

## Sample Conversation

```
Welcome to SmartBot

You: Hi
Bot: Hello! How can I help you today?

You: What is AI?
Bot: Artificial Intelligence enables machines to perform tasks that normally require human intelligence.

You: Tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs!

You: Bye
Bot: Goodbye! Have a wonderful day!
```

---

## Concepts Used

- Python Functions
- Dictionaries
- Lists
- Loops
- Conditional Statements
- String Matching
- Pattern Matching
- Random Response Selection

---

## Advantages

- Easy to understand
- Fast response time
- Lightweight
- Beginner-friendly
- Easy to customize

---

## Limitations

- Cannot learn from users.
- Cannot understand complex sentences.
- Limited to predefined responses.
- Does not use Machine Learning or Deep Learning.

---

## Future Improvements

- Add GUI using Tkinter
- Add Speech Recognition
- Add Text-to-Speech
- Use NLP with NLTK or spaCy
- Store chat history
- Load responses from JSON
- Connect with OpenAI API

---

## Sadia Khan

Developed as an AI Internship Project using Python.
