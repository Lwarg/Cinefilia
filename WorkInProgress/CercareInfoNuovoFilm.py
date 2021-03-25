import requests
import json



# L'utente inserisce il titolo del film
film = input("Inserire il titolo del film: ")  # diventa casella di inserimento testo nella GUI


# ricerca film tramite API
apikey = "Inserire API valida" # 1000 requests al giorno
url = "http://www.omdbapi.com/?s="+film+"&apikey="+apikey
response = requests.request("GET", url)
# print(response)
data = json.loads(response.text)


try: # se la ricerca tramite API ha funzionato senza errori

    # Elenco film con il titolo inserito
    possibili_film = []
    count = 1

    # se sono stati trovati dei film stampali a video con un codice numerico
    if len(data['Search'])>0: 
        for movie in data['Search']:
            possibili_film.append(movie['Title'])
            print(count,"-",movie['Title'],"-",movie['Year'])
            count +=1

        # L'utente seleziona il film desiderato tra quelli trovati inserendo il codice numerico corrispondente
        codice = int(input("Inserire il codice del film desiderato: "))
        film_scelto = data['Search'][codice-1]['imdbID']

        # ricerca film tramite API usando l'ID del film
        url = "http://www.omdbapi.com/?i="+film_scelto+"&apikey="+apikey
        response = requests.request("GET", url)
        data = json.loads(response.text)

        # restituisco il titolo
        print("Titolo:",data['Title'])

        # restituisco l'anno
        print("Anno:",data['Year'])

        # durata
        print("Durata:",data['Runtime'])

        # genere
        print("Genere:",data['Genre'])

        # restituisco il regista
        print("Regia:",data['Director'])

        # restituisco il cast
        print("Cast:",data['Actors'])

        # restituisco la trama
        print("Trama:",data['Plot'])
    else:
        print('Film NON trovato')
except:
    print('API request error')