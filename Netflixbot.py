import random

# Netflix sample database (genre, actors, mood tags)
netflix_db = [
    {"title": "Extraction", "genre": "action", "actors": ["Chris Hemsworth"], "mood": ["thrilling", "intense"]},
    {"title": "The Old Guard", "genre": "action", "actors": ["Charlize Theron"], "mood": ["exciting", "thrilling"]},
    {"title": "Yes Day", "genre": "comedy", "actors": ["Jennifer Garner"], "mood": ["funny", "family"]},
    {"title": "Eurovision Song Contest", "genre": "comedy", "actors": ["Will Ferrell", "Rachel McAdams"], "mood": ["musical", "funny"]},
    {"title": "The Crown", "genre": "drama", "actors": ["Olivia Colman"], "mood": ["serious", "historical"]},
    {"title": "Ozark", "genre": "drama", "actors": ["Jason Bateman"], "mood": ["dark", "intense"]},
    {"title": "Stranger Things", "genre": "sci-fi", "actors": ["Millie Bobby Brown"], "mood": ["thrilling", "mysterious"]},
    {"title": "Dark", "genre": "sci-fi", "actors": ["Louis Hofmann"], "mood": ["mysterious", "serious"]},
    {"title": "Bird Box", "genre": "horror", "actors": ["Sandra Bullock"], "mood": ["scary", "thrilling"]},
    {"title": "Fear Street", "genre": "horror", "actors": ["Kiana Madeira"], "mood": ["scary", "dark"]}
]

# Function to display main menu
def main_menu():
    print("\n===============================")
    print("   🎬 Welcome to Netflix Bot 🎬")
    print("===============================")
    print("1️⃣  Suggest by Genre")
    print("2️⃣  Search by Actor/Keyword")
    print("3️⃣  Suggest by Mood")
    print("4️⃣  Random Pick")
    print("5️⃣  Exit")
    print("===============================")

# Function to suggest by genre
def suggest_by_genre():
    genres = set(movie["genre"] for movie in netflix_db)
    print(f"\nAvailable Genres: {', '.join(genres)}")
    choice = input("👉 Enter a genre: ").lower()

    matches = [m["title"] for m in netflix_db if m["genre"] == choice]

    if matches:
        print(f"🍿 You could watch: {random.choice(matches)}")
    else:
        print("⚠️ Sorry, no matches found for that genre.")

# Function to search by actor or keyword
def search_by_actor():
    keyword = input("\n🔎 Enter an actor's name or keyword: ").lower()
    matches = [m["title"] for m in netflix_db if keyword in ' '.join(m["actors"]).lower() or keyword in m["title"].lower()]

    if matches:
        print("✨ Here are some options:")
        for movie in matches:
            print(f" - {movie}")
    else:
        print("⚠️ No results found.")

# Function to suggest by mood
def suggest_by_mood():
    moods = set(tag for movie in netflix_db for tag in movie["mood"])
    print(f"\nAvailable Moods: {', '.join(moods)}")
    choice = input("👉 What mood are you in?: ").lower()

    matches = [m["title"] for m in netflix_db if choice in m["mood"]]

    if matches:
        print(f"🎭 Based on your mood, try: {random.choice(matches)}")
    else:
        print("⚠️ No movies match that mood.")

# Function to pick random movie/show
def random_pick():
    movie = random.choice(netflix_db)
    print(f"🎲 Random Pick: {movie['title']} ({movie['genre'].title()})")

# Main chatbot loop
def netflix_bot():
    print("👋 Hi Sunshine! I’m your Netflix Bot, here to help you decide what to watch 🍿")
    
    while True:
        main_menu()
        choice = input("👉 Choose an option (1-5): ")

        if choice == "1":
            suggest_by_genre()
        elif choice == "2":
            search_by_actor()
        elif choice == "3":
            suggest_by_mood()
        elif choice == "4":
            random_pick()
        elif choice == "5":
            print("😊 Enjoy your Netflix time! Bye 👋")
            break
        else:
            print("⚠️ Invalid choice, please try again.")

# Run the chatbot
if __name__ == "__main__":
    netflix_bot()
