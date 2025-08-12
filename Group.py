class Group:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.watchlist = []

    def add_member(self, member):
        if member not in self.members:
            self.members.append(member)
        else:
            print(f"{member} is already a member of the group {self.name}.")

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
        else:
            print(f"{member} is not a member of the group {self.name}.")

    def get_members(self):
        return self.members

    def add_movie_to_watchlist(self, id, title, release_date, rating, genre, runtime, overview ):
        if id not in [movie['id'] for movie in self.watchlist]:
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
            print(f"{title} added to the watchlist of group {self.name}.")
        else:
            pass

    def display_watchlist(self):
        if self.watchlist:
            print(f"Watchlist of group {self.name}:")
            for movie in self.watchlist:
                print(f"- {movie['title']} ({movie['release_date']}) - {movie['rating']}/10 - {movie['genre']} - {movie['runtime']} mins - {movie['overview']}")
        else:
            print(f"The watchlist of group {self.name} is empty.")


