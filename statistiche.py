import requests
import json

# Prendo l'elenco dei film dell'utente specificato e ritorno un po' di statistiche

utente = "Insert User"
database = "Insert valid path"
apikey = "Insert valid API"
elencoFilm = open(database +'/elencoFilmdi' + utente +'.txt','r')

schede_tecniche = []
for film in elencoFilm:
    idFilm = film.strip()
    # ricerca film tramite API usando l'ID del film
    url = "http://www.omdbapi.com/?i="+idFilm+"&apikey="+apikey
    response = requests.request("GET", url)
    schede_tecniche.append(json.loads(response.text))

print(schede_tecniche)

# numero film visti
numero_film_visti = len(schede_tecniche)
print("Numero di film visti:",numero_film_visti)


durata = 0
generi = dict()
registi = dict()
attori = dict()

for film in schede_tecniche:

    # somma durata totale 
    durata = durata + int(film['Runtime'].split(" ")[0])

    # conteggio generi
    tipologie = film['Genre'].split(", ")
    for genere in tipologie:
        if genere in generi:
            generi[genere] += 1
        else:
            generi[genere] = 1
    
    # conteggio registi
    if film['Director'] in registi:
        registi[film['Director']] += 1
    else:
        registi[film['Director']] = 1
    
    # conteggio attori
    cast = film['Actors'].split(", ")
    for actor in cast:
        if actor in attori:
            attori[actor] += 1
        else:
            attori[actor] = 1

    

# durata
durata = durata/60
print("Tempo totale a guardare film:",durata,"ore")

# genere più visto
print(generi)

# regista più seguito
print(registi)

# attori più seguiti
print(attori)


