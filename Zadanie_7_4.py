# sekcja importów
import sys
import random

base_list = []

# definicje klas
class Movies:
    def __init__(self, title, release_date, genre):
        self.title = title
        self.release_date = release_date
        self.genre = genre

        # Variables
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
        
        # Variables
        self.number_of_plays = 0

    def __str__(self):
        return "%s S%.2dE%.2d" % (self.title, self.series_number, self.episode_number)

# definicje funkcji
# function to print objects from class only Movies
def get_movies():
    list_to_sort = [film for film in base_list if film.__class__.__name__ == 'Movies']
    list_to_sort = sorted(list_to_sort, key=lambda Movies: Movies.title)
    print("Biblioteka filmów:")
    for i in list_to_sort:
        print(i)

# function to print objects from class only Series       
def get_series():
    list_to_sort = [series for series in base_list if series.__class__.__name__ == 'Series']
    list_to_sort = sorted(list_to_sort, key=lambda Series: Series.title)
    print("Biblioteka seriali:")
    for i in list_to_sort:
        print(i)

# search function
def search(name):
    for film_series in base_list:
        if str(film_series.title) == name:
            print(film_series)
        else:
            print("Niestety nie ma takiego tytułu w naszej bazie")

# decorator for generating views
def generate_multi(func):
    def wrap(*args):
        for i in range(11):
            func(*args)           
    return wrap

# generate random views
@generate_multi
def generate_views():
    i = random.choice(base_list)
    j = random.choice(range(101))
    i.play(j)
    print(i)
    print(i.number_of_plays)


# print out the top title by views
def top_titles(top_n, klass):
    films_selected_by_class = [film for film in base_list if film.__class__.__name__ == klass.__name__]
    films_sorted_by_number_of_plays = sorted(films_selected_by_class, key=lambda film: film.number_of_plays, reverse=True)
    n=0
    for i, film in enumerate(films_sorted_by_number_of_plays, start = 1):
        print(f"{film}, views = {film.number_of_plays}")
        if i == top_n:
            break

# function that shows possible actions
def print_help():
    print("""Poniżej lista czynności, które możesz wykonać wpisując odpowiednią komendę:
    lista filmów - wydruk całej listy filmów
    lista seriali - wydruk całej listy seriali
    generuj wyświetlenia - wygenerowanie losowej liczby wyświetleń
    szukaj - wyszukanie filmu lub serialu
    najlepsze tytuły - wydruk najlepszych tytułów filmów lub seriali
    zamknij - zamknięcie programu""")

# biblioteka filmów
movie_one = Movies(title = "Shrek", release_date = "2001", genre = "animated")
movie_two = Movies(title = "The Godfather", release_date = "1972", genre = "criminal")
movie_three = Movies(title = "Pulp Fiction", release_date = "1994", genre = "criminal")

# biblioteka seriali
series_one = Series(title = "South Park", release_date = "1997", genre = "animated", series_number = random.randint(1, 23), episode_number = random.randint(1, 14))
series_two = Series(title = "Stranger Things", release_date = "2016", genre = "science fiction", series_number = random.randint(1, 3), episode_number = random.randint(1, 10))
series_three = Series(title = "Rick & Morty", release_date = "2013", genre = "animated", series_number = random.randint(1, 4), episode_number = random.randint(1, 12))

# zawarcie wszystkich filmów i seriali w jednej liście base_list
base_list.append(movie_one)
base_list.append(movie_two)
base_list.append(movie_three)
base_list.append(series_one)
base_list.append(series_two)
base_list.append(series_three)


# dostępne komendy do wywołania
def task():
    while True:
        task1 = input("Co chcesz wykonać?")
        if task1 == "pomoc":
            print_help()

        elif task1 == "lista filmów":
            get_movies()

        elif task1 == "lista seriali":
            get_series()

        elif task1 == "generuj wyświetlenia":
            generate_views()

        elif task1 == "szukaj":
            name_movie_series = input("Podaj nazwę filmu lub serialu, którego szukasz: ")
            search(name_movie_series)

        elif task1 == "najlepsze tytuły":
            movie_series = input("Najlepsze tytuły: 'film' czy 'serial': ")
            list_length = input("Ile pozycji ma się znalezć w top liście: ") 
            if movie_series == "film":
                top_titles(list_length, Movies)
            elif movie_series == "serial":
                top_titles(list_length, Series)

        elif task1 == "zamknij":
            print("Narazie")
            break
        
        else:
            print("Nie ma takiego polecenia. Sprawdz za pomocą komendy 'pomoc' co możesz zrobić")

# uruchomienie programu
if __name__ == "__main__":
    print("Witam w programie do pobierania danych na temat filmów! \n Wpisz 'pomoc' aby dowiedzieć się więcej")
    task()        