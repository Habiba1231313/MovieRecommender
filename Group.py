class user:
    def __init__(self, name):
        self.name = name
        self.file_name = f"{name}_watchlist.txt"

    def save_movie(self, movie):
        with open(self.file_name, 'a') as file:
            file.write(f"{movie['title']} ({movie['release_date']}) - {movie['overview']}\n")
        print(f"Movie '{movie['title']}' saved to {self.file_name}.")

    def view_watchlist(self):
        try:
            with open(self.file_name, 'r') as file:
                watchlist = file.readlines()
                if watchlist:
                    print(f"Watchlist for {self.name}:")
                    for movie in watchlist:
                        print(movie.strip())
                else:
                    print("Your watchlist is empty.")
        except FileNotFoundError:
            print("Watchlist file not found. Please save a movie first.") 
