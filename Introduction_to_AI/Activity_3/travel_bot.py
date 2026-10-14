
import re
import random
from colorama import Fore, init

# Initialize colored terminal output
init(autoreset=True)

# Travel destinations
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

# Random jokes
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]


def normalize_input(text):
    """Remove extra spaces and convert text to lowercase."""
    return re.sub(r"\s+", " ", text.strip().lower())


def recommend():
    """Recommend destinations based on user preference."""
    while True:
        print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
        preference = normalize_input(input("You: "))

        if preference not in destinations:
            print(Fore.RED + "Please choose beaches, mountains, or cities.")
            continue

        while True:
            suggestion = random.choice(destinations[preference])
            print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
            print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
            answer = normalize_input(input("You: "))

            if answer == "yes":
                print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
                return
            elif answer == "no":
                print(Fore.YELLOW + "TravelBot: Let's try another.")
                break
            else:
                print(Fore.RED + "Please answer yes or no.")


def packing_tips():
    """Give basic packing advice."""
    location = input("TravelBot: Where are you going? ").strip()
    days = input("TravelBot: How many days? ").strip()

    print(Fore.GREEN + f"\nPacking tips for {days} days in {location}:")
    print("- Pack versatile clothes.")
    print("- Bring chargers and adapters.")
    print("- Check the weather forecast.")


def tell_joke():
    """Tell a random joke."""
    print(Fore.YELLOW + "TravelBot: " + random.choice(jokes))


def show_help():
    """Display available commands."""
    print(Fore.MAGENTA + "\nI can help you with:")
    print(Fore.GREEN + "- recommendation: suggest travel destinations")
    print(Fore.GREEN + "- packing: get packing tips")
    print(Fore.GREEN + "- joke: hear a joke")
    print(Fore.GREEN + "- help: show this menu")
    print(Fore.CYAN + "- exit or bye: end the chat\n")


def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input("What's your name? ").strip()

    if not name:
        name = "Traveler"

    print(Fore.GREEN + f"Nice to meet you, {name}!")
    show_help()

    while True:
        user_input = normalize_input(input(f"{name}: "))

        if not user_input:
            print(Fore.RED + "Please enter a command.")
        elif "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif user_input in ("exit", "bye"):
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")


if __name__ == "__main__":
    chat()
