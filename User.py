class User:
    def __init__(self, username):
        self.username = username
        self.watchlist  = []
        self.groups = []

    def save_movie(self ,id,title, release_date, rating, genre, runtime, overview):
        if id not in self.watchlist:
            movie = {
                'id': id,
                'title': title,
                'release_date': release_date,
                'rating': rating,
                'genre': genre,
                'runtime': runtime,
                'overview': overview
            }
            self.watchlist.append(movie)
            with open(f"{self.username}.txt", "a") as f:
                f.write(f"{id} {title} - {release_date} - {rating} - {genre} - {runtime} - {overview}\n")
            print(f"{title} added to {self.username}'s watchlist.")
        else:
            print(f"{movie} is already in {self.username}'s watchlist.")

    def join_group(self, group):
        if group not in self.groups:
            self.groups.append(group)
            print(f"{self.username} joined the group {group.name}.")
        else:
            print(f"{self.username} is already a member of the group {group.name}.")
    def leave_group(self, group):       
        if group in self.groups:
            self.groups.remove(group)
            print(f"{self.username} left the group {group.name}.")
        else:
            print(f"{self.username} is not a member of the group {group.name}.")

    def display_watchlist(self):
        if self.watchlist:
            print(f"{self.username}'s Watchlist:")
            for movie in self.watchlist:
                print(f"- {movie['title']} ({movie['release_date']}) - {movie['rating']}/10 - {movie['genre']} - {movie['runtime']} mins - {movie['overview']}")
        else:
            print(f"{self.username}'s watchlist is empty.")

        
