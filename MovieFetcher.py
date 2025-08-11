import requests
class MovieFetcher:
    def __init__(self,genre, min_rating , release_year , api_key):
        self.Api_endpoint = "https://api.themoviedb.org/3/"
        self.api_key = api_key
        self.min_rating = min_rating
        self.release_year = release_year    
        self.genre = genre

    def fetch_movies(self):
        url = f"{ self.Api_endpoint}discover/movie?with_genres={self.genre}&primary_release_date.gte={self.release_year}-01-01&vote_average.gte={self.min_rating}&api_key={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error fetching data")
            
        
   