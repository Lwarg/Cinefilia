import requests
import json
# Funzione per visualizzare la lista dei film

# accedo al database
elencoFilm = open("elencoFIlm.txt")

# richiesta titolo film tramite API
apikey = "Inserire API valida" # 1000 requests al giorno


# restituisco in output i film visti dall'ultimo al primo
count = 1
for film in reversed(list(elencoFilm)):
    url = "http://www.omdbapi.com/?i="+film[:-1]+"&apikey="+apikey
    response = requests.request("GET", url)
    # print(response)
    data = json.loads(response.text)
    print(count,"-",data['Title'])
    count +=1
