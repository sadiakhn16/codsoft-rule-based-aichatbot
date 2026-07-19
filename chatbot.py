from responses import get_response

print("=" * 50)
print(" Welcome to SmartBot")
print("Type 'bye' or 'exit' to quit.")
print("=" * 50)

while True:
    user = input("\nYou: ")

    response = get_response(user)

    print("Bot:", response)

    if any(word in user.lower() for word in ["bye", "exit", "quit", "goodbye"]):
        break