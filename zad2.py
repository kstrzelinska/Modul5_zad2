import random

class Film:
    def __init__(self, tytul, rok_wydania, gatunek, liczba_odtworzen=0):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen

    def play(self):
        self.liczba_odtworzen += 1

    def __str__(self):
        return f'{self.tytul} ({self.rok_wydania})'

class Serial(Film):
    def __init__(self, tytul, rok_wydania, gatunek, numer_odcinka, numer_sezonu, liczba_odtworzen=0):
        super().__init__(tytul, rok_wydania, gatunek, liczba_odtworzen)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu

    def __str__(self):
        return f'{self.tytul} S{self.numer_sezonu:02}E{self.numer_odcinka:02}'


#pokazuje tylko filmy alfabetycznie
def get_movies(lista):
    movies = [item for item in lista if isinstance(item, Film) and not isinstance(item, Serial)]
    return sorted(movies, key=lambda film: film.tytul)

#pokazuje tylko seriale alfabetycznie
def get_series(lista):
    series = [item for item in lista if isinstance(item, Serial)]
    return sorted(series, key=lambda serial: serial.tytul)

#wyszukuje film lub serial po jego tytule
def search(lista, tytul):
    results = [item for item in lista if tytul.lower() in item.tytul.lower()]
    if results:
        return results
    else:
        return f"Brak wyników dla tytułu: {tytul}"


# losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń
def generate_views(lista):
    # Wybierz losowy element z listy
    selected_item = random.choice(lista)
    # Wygeneruj losową liczbę odtworzeń w zakresie od 1 do 100
    random_views = random.randint(1, 100)
    # Dodaj odtworzenia do wybranego elementu
    selected_item.liczba_odtworzen += random_views
    print(f'Dodano {random_views} odtworzeń do: {selected_item}')

#uruchomienie generatr_view 10 raz => pętla
def run_generate_views_multiple_times(lista, times=10):
    for _ in range(times):
        generate_views(lista)

#napopularniejsze tytuły + content_type (wybór czy film czy serial)
def top_titles(lista, count=5, content_type=None):
    filtered_titles = []
    
    # Filtrowanie według typu treści
    if content_type == 'film':
        filtered_titles = [item for item in lista if isinstance(item, Film) and not isinstance(item, Serial)]
    elif content_type == 'serial':
        filtered_titles = [item for item in lista if isinstance(item, Serial)]
    else:
        filtered_titles = lista

    # Sortowanie według liczby odtworzeń
    sorted_titles = sorted(filtered_titles, key=lambda x: x.liczba_odtworzen, reverse=True)
    
    return sorted_titles[:count]


#Wyświetli na konsoli komunikat Biblioteka filmów.
print("Biblioteka filmów")  
    
#Wypełni bibliotekę treścią.
#jedna lista dla filmów i seriali
lista = []
#dodanie przykładowych filmów do listy
lista.append(Film("Pulp Fiction", 1994, "Crime"))
lista.append(Film("Inception", 2010, "Sci-Fi"))
lista.append(Serial("The Simpsons", 1989, "Animation", 5, 1))  # S01E05
lista.append(Serial("Friends", 1994, "Comedy", 12, 5))  # S05E12

for item in lista:
    item.play()  # Zwiększenie liczby odtworzeń o 1
    print(item)  # Wyświetlenie informacji o filmie lub serialu

#Wygeneruje odtworzenia treści za pomocą funkcji generate_views
print("\nWywołanie funkcji generate_views 10 razy, aby przetestować działanie:")
for _ in range(10):
    generate_views(lista)  

#Wyświetli na konsoli komunikat Najpopularniejsze filmy i seriale dnia <data>, gdzie <data> to bieżąca data w formacie DD.MM.RRRR
from datetime import datetime
today_date = datetime.today()
formatted_date = today_date.strftime('%d.%m.%Y')
print("\nNajpopularniejsze filmy i seriale dnia", formatted_date, ":")
top_items = top_titles(lista, count=3)  # Najpopularniejsze 3 filmy
for item in top_items:
    print(item)

""" SPRAWDZENIE PRZYKŁADY

# Odtwarzanie i wyświetlanie filmów oraz seriali
print("Lista filmów i seriali")
for item in lista:
    item.play()  # Zwiększenie liczby odtworzeń o 1
    print(item)  # Wyświetlenie informacji o filmie lub serialu


# Pobieranie i wyświetlanie filmów
print("\nLista filmów")
movies = get_movies(lista)
print("Filmy:")
for movie in movies:
    print(movie)

# Pobieranie i wyświetlanie seriali
print("\nLista seriali")
series = get_series(lista)
print("Seriale:")
for serie in series:
    print(serie)

#sprawdzenie search
print("\nWyszukiwanie po tytule")
szukana = input("Podaj tytuł filmu lub serialu: ")
wyniki = search(lista, szukana)
if isinstance(wyniki, list):
    for wynik in wyniki:
        print(wynik)  # Wyświetlenie każdego wyniku
else:
    print(wyniki)  # Wyświetlenie komunikatu o braku wyników


# czy działa 10 raz
print("\nTest na generewanie odtworzeń x10")
run_generate_views_multiple_times(lista, times=10)

print("\nFinalna liczba odtworzeń:")
for item in lista:
    print(f'{item.tytul} - {item.liczba_odtworzen} odtworzeń') 

#top title np. dla filmów
print("\nNajpopularniejsze:")
top_items = top_titles(lista, count=2)  # Na przykład zwróć top 2 tytuły
for item in top_items:
    print(item)

print("\nLista top filmów")
print("Najpopularniejsze filmy:")
top_films = top_titles(lista, count=2, content_type='film')  # Najpopularniejsze 2 filmy
for film in top_films:
    print(film)
"""
