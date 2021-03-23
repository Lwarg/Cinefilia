import requests
import json
# visualizzo la lista dei film e ne scelgo uno da cui ricavo le informazioni

#########################
# accedo al database
elencoFilm = open("elencoFIlm.txt")

# restituisco in output i film visti dall'ultimo al primo
listaFilm = []
count = 1
for film in reversed(list(elencoFilm)):
    listaFilm.append(film[:-1])
    print(count,"-",film[:-1])
    count +=1

# L'utente inserisce inserisce il codice per selezionare il film di cui vuole le info
codice = int(input("Inserire il numero del film: "))
film = listaFilm[codice-1]

# ricerca film tramite API
apikey = "Insert a valid API" # 1000 requests al giorno
url = "http://www.omdbapi.com/?t="+film+"&apikey="+apikey
response = requests.request("GET", url)
# print(response)
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




