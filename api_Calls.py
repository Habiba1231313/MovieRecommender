import requests
from WeatherFetcher import WeatherFetcher
import random 
"""
api_key = "b3b48187861891a3c3d52c306ca5b7ee"
city = "doha"
url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response =requests.get(url)
if response.status_code == 200:
    response_data = response.json()
else:
            response.raise_for_status()

print("weather in " + city)
print("Temprature: " + str(response_data['main']['temp']- 273.15) + ' celcius')
print(response_data["weather"][0]["description"])
print("Humidity: "+str(response_data["main"]["humidity"]))


"""
#getting the list of available genres from the movie database API
url = f"https://api.themoviedb.org/3/genre/movie/list?api_key=bf55a79c9e812b518d529cb5a1ca1599"
response = requests.get(url)
if response.status_code == 200:
    response_data = response.json()
    genres = response_data['genres']
    print(genres)
    #for genre in genres:
        #print(f"{genre['id']}: {genre['name']}")
else:
    response.raise_for_status()

""""""
genres = {
    "action": 28,
    "adventure": 12,
    "animation": 16,
    "comedy": 35,
    "crime": 80,
    "documentary": 99,
    "crama": 18,
    "family": 10751,
    "fantasy": 14,
    "history": 36,
    "horror": 27,
    "music": 10402,
    "mystery": 9648,
    "romance": 10749,
    "science Fiction": 878,
    "tv Movie": 10770,
    "thriller": 53,
    "war": 10752,
    "western": 37
}
genre = "action"
if genre not in genres:
            raise ValueError(f"Invalid genre: {genre}. Available genres are: {', '.join([f'{k}: {v}' for k, v in genres.items()])}")
else:
    genre = genres[genre]  # getting the genre id from the dictionary
    Api_endpoint = "https://api.themoviedb.org/3/"
    api_key = "bf55a79c9e812b518d529cb5a1ca1599"
    min_rating = 7
    release_year = 2022    
url = f"{Api_endpoint}discover/movie?with_genres={genre}&primary_release_date.gte={release_year}-01-01&vote_average.gte=7&api_key={api_key}"
response = requests.get(url)
if response.status_code == 200:
        data=  response.json()
else:
    print("Error fetching data")
random_movie = random.choice(data['results'])
print(f"rating: {random_movie['vote_average']} out of 10 title: {random_movie['title']} release date: {random_movie['release_date']}")
print(random_movie['id'])

url = f"https://api.themoviedb.org/3/movie/{random_movie['id']}?api_key={api_key}"
response = requests.get(url)
if response.status_code == 200:
    movie_data = response.json()
print(f"🎬 MOVIE SUGGESTION 🎬\nTitle: {movie_data['title']} ({movie_data['release_date']})\nRating: {movie_data['vote_average']}/10⭐ \nGenre: {movie_data['genres'][0]['name']}\nRuntime: {movie_data['runtime']}\nPlot: {movie_data['overview']}")
