
import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colored terminal output
colorama.init()

print(f"{Fore.CYAN}🐍 Welcome to Sentiment Spy! 🐍{Style.RESET_ALL}")

user_name = input(
    f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}"
).strip()

if not user_name:
    user_name = "Mystery Agent"

# Store text, polarity, and sentiment
conversation_history = []

print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print("Type a sentence for sentiment analysis.")
print(
    f"Type {Fore.YELLOW}reset{Fore.CYAN}, "
    f"{Fore.YELLOW}history{Fore.CYAN}, "
    f"or {Fore.YELLOW}exit{Fore.CYAN} to quit."
    f"{Style.RESET_ALL}\n"
)

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    command = user_input.lower()

    if command == "exit":
        print(
            f"\n{Fore.BLUE}Exiting Sentiment Spy. "
            f"Farewell, Agent {user_name}! 😊{Style.RESET_ALL}"
        )
        break

    elif command == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}All conversation history cleared!{Style.RESET_ALL}")
        continue

    elif command == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")

            for idx, (text, polarity, sentiment_type) in enumerate(
                conversation_history, start=1
            ):
                if sentiment_type == "Positive":
                    color, emoji = Fore.GREEN, "😊"
                elif sentiment_type == "Negative":
                    color, emoji = Fore.RED, "😞"
                else:
                    color, emoji = Fore.YELLOW, "😐"

                print(
                    f"{idx}. {color}{emoji} {text} "
                    f"Polarity: {polarity:.2f}, "
                    f"{sentiment_type}{Style.RESET_ALL}"
                )
        continue

    # Analyze sentiment
    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0.25:
        sentiment_type = "Positive"
        color, emoji = Fore.GREEN, "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color, emoji = Fore.RED, "😞"
    else:
        sentiment_type = "Neutral"
        color, emoji = Fore.YELLOW, "😐"

    conversation_history.append(
        (user_input, polarity, sentiment_type)
    )

    print(
        f"{color}{emoji} {sentiment_type} sentiment detected! "
        f"Polarity: {polarity:.2f}{Style.RESET_ALL}"
    )
