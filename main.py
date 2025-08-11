
#from WeatherFetcher import WeatherFetcher
#result = WeatherFetcher("cairo").format_weather()
#print(result)
from MovieRecommender import MovieRecommender
import requests

"""
# basic function to compare the temperature of two cities
def two_cities_weather(city1, city2):
    city1_temp = WeatherFetcher(city1).temperature()
    city2_temp = WeatherFetcher(city2).temperature()
    if city1_temp is None or city2_temp is None:
        print("Failed to fetch weather data for one or both cities.")
        return
    elif int(city1_temp) > int(city2_temp):
        print(f"{city1} is hotter than {city2}  by {city1_temp - city2_temp} degrees Celsius")
    else:
        print(f"{city2} is hotter than {city1} by {city2_temp - city1_temp} degrees Celsius")
    
two_cities_weather('doha',"cairo")


# copmare the temperature of multiple cities
def compare_weather():
    number_of_cities = int(input("Enter the number of cities you want to compare: "))
    cities = {}
    for i in range(number_of_cities):
        city = input("Enter the name of city")
        temp = WeatherFetcher(city).temperature()
        if temp is not None:
            cities[city] = temp
        else:
            print(f"Failed to fetch weather data for {city}.")

    sorted_cities = sorted(cities.items(),key = lambda x:x[1])
    print("Cities sorted by temperature:")
    for city, temp in sorted_cities:
        print(f"{city}: {temp} Celsius")
      

compare_weather()

"""""



# Example usage of MovieRecommender
recommender = MovieRecommender("bf55a79c9e812b518d529cb5a1ca1599")
#movie = recommender.get_recommendation("action",7.0, 2020 )
#print(movie)



def user_input_recommendation():
    print(recommender.genre_list())
    genre = int (input("Enter the genre id of the movie: "))
    if genre not in recommender.genre_list().values():
        raise ValueError(f"Invalid genre: {genre}. Available genres are: {', '.join([f'{k}: {v}' for k, v in recommender.genre_list().items()])}")
    if genre.is_integer():
        genre = int(genre)
    else:
        raise ValueError("Invalid genre id. Please enter a number.")
    min_rating = float(input("Enter the minimum rating (0-10): "))
    release_year = int(input("Enter the release year: "))
    name = input("Enter your name: ")
    print(f"Hello {name}, fetching a movie recommendation for you...")
    try:
        movie = recommender.get_recommendation(genre, min_rating, release_year)
        print(f"do you want to save this movie to your watchlist? (yes/no)")
        save_choice = input().strip().lower()
        if save_choice == 'yes':
            file_name = f"{name}_watchlist.txt"
            with open(file_name, "a") as file:
                file.write(f"{movie['title']} ({movie['release_date']}) - {movie['vote_average']}/10\n")
            print("Movie saved to watchlist.")
    except Exception as e:
        print(f"An error occurred: {e}")

user_input_recommendation()