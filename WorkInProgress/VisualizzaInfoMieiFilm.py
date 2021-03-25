import requests
import json
# visualizzo la lista dei film e ne scelgo uno da cui ricavo le informazioni

#########################
# accedo al database
elencoFilm = open("elencoFIlm.txt")

# accedo al database
elencoFilm = open("elencoFIlm.txt")

# richiesta titolo film tramite API
apikey = "Inserire API valida" # 1000 requests al giorno

# restituisco in output i film visti dall'ultimo al primo
listaFilm = []
count = 1
for film in reversed(list(elencoFilm)):
    url = "http://www.omdbapi.com/?i="+film[:-1]+"&apikey="+apikey
    response = requests.request("GET", url)
    # print(response)
    data = json.loads(response.text)
    listaFilm.append(data)
    print(count,"-",data['Title'])
    count +=1

# L'utente inserisce inserisce il codice per selezionare il film di cui vuole le info
codice = int(input("Inserire il numero del film: "))


# restituisco il titolo
print("Titolo:",listaFilm[codice-1]['Title'])

# restituisco l'anno
print("Anno:",listaFilm[codice-1]['Year'])

# durata
print("Durata:",listaFilm[codice-1]['Runtime'])

# genere
print("Genere:",listaFilm[codice-1]['Genre'])

# restituisco il regista
print("Regia:",listaFilm[codice-1]['Director'])

# restituisco il cast
print("Cast:",listaFilm[codice-1]['Actors'])

# restituisco la trama
print("Trama:",listaFilm[codice-1]['Plot'])




