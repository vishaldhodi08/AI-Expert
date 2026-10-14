
# Activity 1: Hello AI

# Greet the user
print("Hello! I am AI Bot. What's your name? : ")
name = input()

# Respond to the user's name
print(f"Nice to meet you, {name}!")

# Ask a question
print("How are you feeling today? (good/bad) : ")
mood = input().lower()

# Respond based on the user's mood
if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon.")
else:
    print("I see. Sometimes it's hard to put feelings into words.")

# End the conversation
print(f"It was nice chatting with you {name}. Goodbye!")
