import requests
import operator
import json

# Prendo l'elenco dei film dell'utente specificato e ritorno un po' di statistiche

utente = "Insert user"
database = "Insert path"
apikey = "Insert valid APIkey"
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
durata = int(durata/60*100)/100
print("Tempo totale a guardare film:",durata,"ore")

# genere più visto
primoGenere = max(generi.items(), key=operator.itemgetter(1))[0]
film_primoGenere = generi[primoGenere]
generi.pop(primoGenere)

secondoGenere = max(generi.items(), key=operator.itemgetter(1))[0]
film_secondoGenere = generi[secondoGenere]
generi.pop(secondoGenere)

terzoGenere = max(generi.items(), key=operator.itemgetter(1))[0]
film_terzoGenere = generi[terzoGenere]
generi.pop(terzoGenere)

print(primoGenere,film_primoGenere)
print(secondoGenere,film_secondoGenere)
print(terzoGenere,film_terzoGenere)

# regista più seguito
primoRegista = max(registi.items(), key=operator.itemgetter(1))[0]
film_primoRegista = registi[primoRegista]
registi.pop(primoRegista)

secondoRegista = max(registi.items(), key=operator.itemgetter(1))[0]
film_secondoRegista = registi[secondoRegista]
registi.pop(secondoRegista)

terzoRegista = max(registi.items(), key=operator.itemgetter(1))[0]
film_terzoRegista = registi[terzoRegista]
registi.pop(terzoRegista)

print(primoRegista,film_primoRegista)
print(secondoRegista,film_secondoRegista)
print(terzoRegista,film_terzoRegista)

# attori più seguiti
primoAttore = max(attori.items(), key=operator.itemgetter(1))[0]
film_primoAttore = attori[primoAttore]
attori.pop(primoAttore)

secondoAttore = max(attori.items(), key=operator.itemgetter(1))[0]
film_secondoAttore = attori[secondoAttore]
attori.pop(secondoAttore)

terzoAttore = max(attori.items(), key=operator.itemgetter(1))[0]
film_terzoAttore = attori[terzoAttore]
attori.pop(terzoAttore)

print(primoAttore,film_primoAttore)
print(secondoAttore,film_secondoAttore)
print(terzoAttore,film_terzoAttore)


