from MovieFetcher import MovieFetcher   
import random 
import requests
class MovieRecommender:
    def __init__(self , api_key):
        self.api_key = api_key
    def get_movies (self, genre, min_rating, release_year):
        return MovieFetcher(genre, min_rating, release_year,self.api_key).fetch_movies()
    def get_recommendation (self, genre, min_rating, release_year):
        data = self.get_movies(genre, min_rating, release_year)
        random_movie = random.choice(data['results'])
        url = f"https://api.themoviedb.org/3/movie/{random_movie['id']}?api_key={self.api_key}"
        movie_details = requests.get(url)
        if movie_details.status_code == 200:
            random_movie = movie_details.json()
            year = random_movie['release_date'].split('-')[0]
            print(f"🎬 MOVIE SUGGESTION 🎬\nTitle: {random_movie['title']} ({year})\nRating: {random_movie['vote_average']}/10⭐ \nGenre: {random_movie['genres'][0]['name']}\nRuntime: {random_movie['runtime']}\nPlot: {random_movie['overview']}")
        else:
            raise Exception("Failed to fetch movie details")
        return random_movie
     
    def genre_list(self):
        url = f"https://api.themoviedb.org/3/genre/movie/list?api_key=bf55a79c9e812b518d529cb5a1ca1599"
        response = requests.get(url)
        if response.status_code == 200:
            response_data = response.json()
            genres = response_data['genres']
            return {genre['name']: genre['id'] for genre in genres}
        else:
            raise Exception("Error fetching genres")

        