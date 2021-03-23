# Funzione per visualizzare la lista dei film

# accedo al database
elencoFilm = open("elencoFIlm.txt")

# restituisco in output i film visti dall'ultimo al primo
count = 1
for film in reversed(list(elencoFilm)):
    print(count,"-",film[:-1])
    count +=1
