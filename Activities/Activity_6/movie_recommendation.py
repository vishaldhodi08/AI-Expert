
import time
import random
import pandas as pd
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

# Load the IMDb dataset
try:
    df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: imdb_top_1000.csv was not found.")
    raise SystemExit

# Check required columns
required_columns = [
    "Series_Title", "Genre", "IMDB_Rating", "Overview"
]

if not all(column in df.columns for column in required_columns):
    print(Fore.RED + "Error: The CSV has different column names.")
    print("Available columns:", df.columns.tolist())
    raise SystemExit

# Extract all unique genres
genres = sorted({
    genre.strip()
    for value in df["Genre"].dropna()
    for genre in value.split(",")
})


def loading_dots():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)


def sentiment_label(polarity):
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😞"
    return "Neutral 😐"


def get_genre():
    print(Fore.GREEN + "\nAvailable Genres:")

    for number, genre in enumerate(genres, start=1):
        print(Fore.CYAN + f"{number}. {genre}")

    while True:
        choice = input(
            Fore.YELLOW + "\nEnter genre number or name: "
        ).strip()

        if choice.isdigit():
            number = int(choice)
            if 1 <= number <= len(genres):
                return genres[number - 1]

        for genre in genres:
            if choice.casefold() == genre.casefold():
                return genre

        print(Fore.RED + "Invalid genre. Please try again.")


def get_rating():
    while True:
        value = input(
            Fore.YELLOW
            + "Enter minimum IMDb rating (7.6-9.3) or 'skip': "
        ).strip()

        if value.lower() == "skip":
            return None

        try:
            rating = float(value)

            if 7.6 <= rating <= 9.3:
                return rating

            print(Fore.RED + "Enter a rating between 7.6 and 9.3.")

        except ValueError:
            print(Fore.RED + "Please enter a valid rating or skip.")


def recommend(genre, mood_polarity, rating=None, n=5):
    movies = df.copy()

    # Filter movies by selected genre
    movies = movies[
        movies["Genre"].str.contains(
            genre, case=False, na=False, regex=False
        )
    ]

    # Filter by minimum IMDb rating
    if rating is not None:
        movies = movies[movies["IMDB_Rating"] >= rating]

    if movies.empty:
        return []

    recommendations = []

    for _, movie in movies.iterrows():
        overview = movie["Overview"]

        if pd.isna(overview):
            continue

        # Analyze the movie overview
        polarity = TextBlob(str(overview)).sentiment.polarity

        # Use mood sentiment as a simple polarity filter
        if mood_polarity > 0 and polarity < 0:
            continue
        elif mood_polarity < 0 and polarity > 0:
            continue

        recommendations.append(
            (movie["Series_Title"], polarity)
        )

    # Randomize results for variety
    random.shuffle(recommendations)

    return recommendations[:n]


def show_recommendations(recommendations, name):
    print(
        Fore.YELLOW
        + f"\n🍿 Movie Recommendations for {name}:"
    )

    for number, (title, polarity) in enumerate(
        recommendations, start=1
    ):
        print(
            Fore.CYAN
            + f"{number}. 🎬 {title} "
            + f"(Polarity: {polarity:.2f}, "
            + f"{sentiment_label(polarity)})"
        )


# Main program
print(
    Fore.BLUE
    + "\n🎥 Welcome to Your AI Movie Recommendation Assistant! 🎥"
)

name = input(Fore.YELLOW + "\nWhat's your name? ").strip()

if not name:
    name = "Movie Lover"

print(Fore.GREEN + f"\nNice to meet you, {name}!")

# Get user preferences
genre = get_genre()

mood = input(
    Fore.YELLOW
    + "\nHow are you feeling today? Describe your mood: "
).strip()

# Analyze user's mood
mood_polarity = TextBlob(mood).sentiment.polarity

print(Fore.BLUE + "\nAnalyzing your mood", end="", flush=True)
loading_dots()

print(
    Fore.GREEN
    + f"\nYour mood is {sentiment_label(mood_polarity)} "
    + f"(Polarity: {mood_polarity:.2f})"
)

rating = get_rating()

# Recommendation loop
while True:
    print(Fore.BLUE + "\nFinding movies", end="", flush=True)
    loading_dots()

    recommendations = recommend(
        genre=genre,
        mood_polarity=mood_polarity,
        rating=rating,
        n=5
    )

    if recommendations:
        show_recommendations(recommendations, name)
    else:
        print(
            Fore.RED
            + "\nNo suitable movies found. Try another genre "
            + "or skip the minimum rating."
        )

    answer = input(
        Fore.YELLOW
        + "\nWould you like more recommendations? (yes/no): "
    ).strip().lower()

    if answer == "no":
        print(
            Fore.GREEN
            + f"\nEnjoy your movie picks, {name}! 🎬🍿"
        )
        break

    elif answer != "yes":
        print(Fore.RED + "Please enter yes or no.")
