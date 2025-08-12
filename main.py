from MovieRecommender import MovieRecommender
import pickle
from User import User
from Group import Group

recommender = MovieRecommender("bf55a79c9e812b518d529cb5a1ca1599")
users = []
groups = []

def menu():
    print("Main Menu:") 
    print("1. Get a movie recommendation")  # done
    print("2. View your personal watchlist")  # done
    print("3. Manage groups")
    print("4. View group watchlists")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice

def main_menu():
    print("Welcome to Movie Recommender!!")
    loading_users_from_file()
    loading_groups_from_file()
    print("Loading previous user data...")
    print("Loading previous group data...")
    print("Please enter your username to continue.")
    print("If you are a new user, please enter a new username.")
    user_name = input("Please enter your username: ").strip()
    if username_exists(user_name):
        print(f"Welcome back, {user_name}!")
        user = get_user_by_username(user_name)
    else:
        print(f"Hello {user_name}, it seems you are a new user. Let's create your profile.")
        user = create_user(user_name)
    
    choice = menu()
    while choice != '5':
        if choice == '1':
            user = get_user_by_username(user_name)
            print("Fetching a movie recommendation...")
            min_rating = float(input("Enter the minimum rating (0-10): "))
            release_year = int(input("Enter the release year: "))
            print("Available genres:")
            print(recommender.genre_list())
            genre = int(input("Enter the genre id of the movie: "))
            if genre not in recommender.genre_list().values():
                raise ValueError(f"Invalid genre: {genre}. Available genres are: {', '.join([f'{k}: {v}' for k, v in recommender.genre_list().items()])}")      
            else:
                print(f"Fetching a movie recommendation for {user_name}...")
                movie = recommender.get_recommendation(genre, min_rating, release_year)
                print("Do you want to save this movie to your watchlist? (yes/no)")
                if input().strip().lower() == 'yes':
                    user.save_movie(movie['id'], movie['title'], movie['release_date'],
                                    movie['vote_average'], movie['genres'][0]['name'],
                                    movie['runtime'], movie['overview'])
                else:
                    print("Movie not saved to watchlist.")
        elif choice == '2':
            watchList_username = input("Enter your username please: ")
            if username_exists(watchList_username):
                user = get_user_by_username(watchList_username)
                user.display_watchlist()
            else:
                print(f"User {watchList_username} does not exist.")
        elif choice == '3':
            group_menu(user)
        elif choice == '4':
            group_name = input("Enter the group name: ")
            if group_exists(group_name):
                group = get_group_by_name(group_name)
                group.display_watchlist()
            else:
                print(f"Group {group_name} does not exist.")
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            writing_users_to_file()
            writing_groups_to_file()
            break
        else:
            print("Invalid choice. Please try again.")
        choice = menu()

# Functions for group management
def create_group(group_name):
    return Group(group_name)

def group_exists(group_name):
    for group in groups:
        if group.name == group_name:
            return True
    return False

def group_menu(user):
    print("Group Management:")
    print("1. Create a new group")
    print("2. Join an existing group")
    print("3. View groups you belong to")
    print("4. Get recommendation for group")
    print("5. Back to main menu")
    sub_choice = input("Enter your choice (1-5): ")
    if sub_choice == '1':
        group_name = input("Enter the name of the new group: ")
        if group_exists(group_name):
            print(f"Group {group_name} already exists.")
        else:
            group = create_group(group_name)
            groups.append(group)
            print(f"Group {group_name} created successfully.")
    elif sub_choice == '2':
        user_name = input("Enter the username that is to join the group: ")
        user = get_user_by_username(user_name)
        group_name = input("Enter the name of the group you want to join: ")
        if group_exists(group_name):
            user.join_group(get_group_by_name(group_name))
        else:
            print(f"Group {group_name} does not exist.")
    elif sub_choice == '3':
        user_name = input("Enter your username to view your groups: ")
        user = get_user_by_username(user_name)
        if user.groups:
            print(f"{user.username} belongs to the following groups:")
            for group in user.groups:
                print(f"- {group.name}")
        else:
            print(f"{user.username} does not belong to any groups.")
    elif sub_choice == '4':
        group_name = input("Enter the name of the group for which you want a recommendation: ")
        group = get_group_by_name(group_name)
        if group:
            print(f"Fetching a movie recommendation for group {group.name}...")
            min_rating = float(input("Enter the minimum rating (0-10): "))
            release_year = int(input("Enter the release year: "))
            print("Available genres:")
            print(recommender.genre_list())
            genre = int(input("Enter the genre id of the movie: "))
            if genre not in recommender.genre_list().values():
                raise ValueError(f"Invalid genre: {genre}. Available genres are: {', '.join([f'{k}: {v}' for k, v in recommender.genre_list().items()])}")
            else:
                movie = recommender.get_recommendation(genre, min_rating, release_year)
                group.add_movie_to_watchlist(movie['id'], movie['title'], movie['release_date'],
                                             movie['vote_average'], movie['genres'][0]['name'],
                                             movie['runtime'], movie['overview'])
    elif sub_choice == '5':
        return
    else:
        print("Invalid choice. Please try again.")

def get_group_by_name(group_name):
    for group in groups:
        if group.name == group_name:
            return group
    return None

def writing_groups_to_file():
    with open("groups.pkl", "wb") as f:
        for group in groups:
            pickle.dump(group, f)

def loading_groups_from_file():
    try:
        with open("groups.pkl", "rb") as f:
            while True:
                try:
                    group = pickle.load(f)
                    groups.append(group)
                except EOFError:
                    break
    except FileNotFoundError:
        print("No previous group data found. Starting fresh.")

# Trial function
def user_input_recommendation():
    print(recommender.genre_list())
    genre = int(input("Enter the genre id of the movie: "))
    if genre not in recommender.genre_list().values():
        raise ValueError(f"Invalid genre: {genre}. Available genres are: {', '.join([f'{k}: {v}' for k, v in recommender.genre_list().items()])}")
    min_rating = float(input("Enter the minimum rating (0-10): "))
    release_year = int(input("Enter the release year: "))
    name = input("Enter your name: ")
    print(f"Hello {name}, fetching a movie recommendation for you...")
    try:
        movie = recommender.get_recommendation(genre, min_rating, release_year)
        print("Do you want to save this movie to your watchlist? (yes/no)")
        save_choice = input().strip().lower()
        if save_choice == 'yes':
            file_name = f"{name}_watchlist.txt"
            with open(file_name, "a") as file:
                file.write(f"{movie['title']} ({movie['release_date']}) - {movie['vote_average']}/10\n")
            print("Movie saved to watchlist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Functions for user management
def username_exists(username):
    for user in users:
        if user.username == username:
            return True
    return False

def get_user_by_username(username):
    for user in users:
        if user.username == username:
            return user
    return None

def create_user(username):
    user = User(username)
    users.append(user)
    return user

# Functions for saving and loading users
def writing_users_to_file():
    with open("users.pkl", "wb") as f:
        for user in users:
            pickle.dump(user, f)

def loading_users_from_file():
    try:
        with open("users.pkl", "rb") as f:
            while True:
                try:
                    user = pickle.load(f)
                    users.append(user)
                except EOFError:
                    break
    except FileNotFoundError:
        print("No previous user data found. Starting fresh.")

main_menu()
