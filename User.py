class user:
    def __init__(self, name):
        self.name = name
        self.file_name = f"{name}_watchlist.txt"

    def save_movie(self, movie):
        with open(self.file_name, 'a') as file:
            file.write(f"{movie['title']} ({movie['release_date']}) - {movie['overview']}\n")
        print(f"Movie '{movie['title']}' saved to {self.file_name}.")
