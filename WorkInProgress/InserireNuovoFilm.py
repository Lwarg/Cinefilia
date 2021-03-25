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
    count = 1

    # se sono stati trovati dei film stampali a video con un codice numerico
    if len(data['Search'])>0: 
        for movie in data['Search']:
            print(count,"-",movie['Title'],"-",movie['Year'])
            count +=1

        # L'utente seleziona il film desiderato tra quelli trovati inserendo il codice numerico corrispondente
        codice = int(input("Inserire il codice del film desiderato: "))
        titolo_film_scelto = data['Search'][codice-1]['Title']
        id_film_scelto = data['Search'][codice-1]['imdbID']

        # Verifica che il film non sia già presente in elenco
        ## USO UN FILE TXT COME DATABASE FITTIZIO, FINCHÈ NON C'È IL DATABASE SERIO
        elenco_film = open("elencoFilm.txt",'r')
        gia_presente = False
        for line in elenco_film:
            if id_film_scelto==line[:-1]:
                gia_presente = True
                print("Film già presente in elenco")
                break
        elenco_film.close()

        # Se non è già presente, il film viene aggiunto alla lista dei film 
        if not gia_presente:
            elenco_film = open("elencoFilm.txt",'a')
            elenco_film.write(id_film_scelto+"\n")
            elenco_film.close()

            # Messaggio di output all'utente (successo oppure errore) 
            print(titolo_film_scelto,'aggiunto correttamente')
    else:
        print('Film NON trovato')
except:
    print('API request error')