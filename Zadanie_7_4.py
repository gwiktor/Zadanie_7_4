import sys
import random

class Movies:
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

    @property
    def number_of_plays(self):
        return self._number_of_plays

    @number_of_plays.setter
    def number_of_plays(self,value):
        self._number_of_plays = value
    
class Series(Movies):
    def __init__(self, series_number, episode_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.series_number = series_number
        self.episode_number = episode_number
        
        #Variables
        self.number_of_plays = 0

    def __str__(self):
        return "%s S%.2dE%.2d" % (self.title, self.series_number, self.episode_number)

movie_one = Movies(title = "Shrek", release_date = "2001", genre = "animated")
movie_two = Movies(title = "The Godfather", release_date = "1972", genre = "criminal")
movie_three = Movies(title = "Pulp Fiction", release_date = "1994", genre = "criminal")

series_one = Series(title = "South Park", release_date = "1997", genre = "animated", series_number = random.randint(1, 23), episode_number = random.randint(1, 14))
series_two = Series(title = "Stranger Things", release_date = "2016", genre = "science fiction", series_number = random.randint(1, 3), episode_number = random.randint(1, 10))
series_three = Series(title = "Rick & Morty", release_date = "2013", genre = "animated", series_number = random.randint(1, 4), episode_number = random.randint(1, 12))

base_list = []
base_list.append(movie_one)
base_list.append(movie_two)
base_list.append(movie_three)
base_list.append(series_one)
base_list.append(series_two)
base_list.append(series_three)

# Function to print objects from class only Movies
def get_movies(a):
    list_to_sort = [i for i in a if i.__class__.__name__ == 'Movies']
    list_to_sort = sorted(list_to_sort, key=lambda Movies: Movies.title)
    print("Biblioteka filmów")
    for i in list_to_sort:
        print(i)

# Function to print objects from class only Series       
def get_series(a):
    list_to_sort = [i for i in a if i.__class__.__name__ == 'Series']
    list_to_sort = sorted(list_to_sort, key=lambda Series: Series.title)
    for i in list_to_sort:
        print(i)

# Search function
def search(a, name):
    for i in a:
        if str(i.title) == name:
            print(i)



# decorator for generating views
def generate_multi(func):
    def wrap(*args):
        for i in range(11):
            func(*args)
            
    return wrap


# Generate random views
@generate_multi
def generate_views(a):
    i = random.choice(a)
    j = random.choice(range(101))
    i.play(j)
    print(i)
    print(i.number_of_plays)

generate_views(base_list)


# print out the top title by views
def top_titles(a, amount, content_type):
    top = [i for i in a if i.__class__.__name__ == content_type.__name__]
    top = sorted(top, key=lambda content_type: content_type.number_of_plays, reverse=True)
    n=0
    for i in top:
        print(f"{i}, views = {i.number_of_plays}")
        n=n+1
        if n == amount:
            break