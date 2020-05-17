import sys
import random

class Films:
    def __init__(self, title, release_date, genre):
        self.title = title
        self.release_date = release_date
        self.genre = genre

        #Variables
        self.number_of_plays = 0

    def play(self, step = 1):
        self.number_of_plays += step

    def __str__(self):
        return f"{self.title} ({self.release_date})"
    
class Series:
    def __init__(self, title, release_date, genre, series_number, episode_number):
        self.title = title
        self.release_date = release_date
        self.genre = genre
        self.series_number = series_number
        self.episode_number = episode_number
        
        #Variables
        self.number_of_plays = 0

    def play(self,step = 1):
        self.number_of_plays += step

    def __str__(self):
        return "%s S%.2dE%.2d" % (self.title, self.series_number, self.episode_number)

film_one = Films(title = "Shrek", release_date = "2001", genre = "animated")
film_two = Films(title = "The Godfather", release_date = "1972", genre = "criminal")
film_three = Films(title = "Pulp Fiction", release_date = "1994", genre = "criminal")

series_one = Series(title = "South Park", release_date = "1997", genre = "animated", series_number = random.randint(1, 23), episode_number = random.randint(1, 14))
series_two = Series(title = "Stranger Things", release_date = "2016", genre = "science fiction", series_number = random.randint(1, 3), episode_number = random.randint(1, 10))
series_three = Series(title = "Rick & Morty", release_date = "2013", genre = "animated", series_number = random.randint(1, 4), episode_number = random.randint(1, 12))

print(film_one)
print(series_two)