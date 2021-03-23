import tkinter as tk
import requests
import json



### funzione corrispondente al bottone searchFilmbtn (per cercare un nuovo film)
def stampaPossibiliFilm(film):
    global txtbox_possibiliFilm
    global apikey
    global data

    # rendo scrivibile il textbox e la pulisco se già scritta
    txtbox_possibiliFilm.configure(state='normal')
    txtbox_possibiliFilm.insert(tk.END, "cercando film...")
    txtbox_possibiliFilm.delete("1.0","end")

    # ricerco il film tramite API
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
                testo = str(count)+" - "+movie['Title']+" - "+movie['Year']+"\n"
                txtbox_possibiliFilm.insert(tk.END, testo)
                count +=1
        
        else:
            txtbox_possibiliFilm.insert(tk.END,'Film NON trovato')
    except:
        txtbox_possibiliFilm.insert(tk.END,'API request error')

    # l'username viene appeso nel file users.txt che si trova nella cartella sincronizzata con google drive
    
    # riblocco la scrivibilità del textbox
    txtbox_possibiliFilm.configure(state='disabled')


### funzione corrispondente al bottone schedaTecnicabtn (per visualizzare la scheda tecnica di un film )
def mostraSchedaTecnica(codice):
    global username
    global txtbox_schedaTec
    global apikey
    global data

    # rendo scrivibile il textbox e la pulisco se già scritta
    txtbox_schedaTec.configure(state='normal')
    txtbox_schedaTec.insert(tk.END, "caricamento...")
    txtbox_schedaTec.delete("1.0","end")

    # prendo l'id del film corrispondente al codice inserito nell'apposito campo
    film_scelto = data['Search'][int(codice)-1]['imdbID']

    # ricerca film tramite API usando l'ID del film
    url = "http://www.omdbapi.com/?i="+film_scelto+"&apikey="+apikey
    response = requests.request("GET", url)
    schedaTecnica = json.loads(response.text)

    # stampa la scheda tecnica
    txtbox_schedaTec.insert(tk.END, "Titolo: "+schedaTecnica['Title']+"\n")
    txtbox_schedaTec.insert(tk.END, "Anno: "+schedaTecnica['Year']+"\n")
    txtbox_schedaTec.insert(tk.END, "Durata: "+schedaTecnica['Runtime']+"\n")
    txtbox_schedaTec.insert(tk.END, "Genere: "+schedaTecnica['Genre']+"\n")
    txtbox_schedaTec.insert(tk.END, "Regia: "+schedaTecnica['Director']+"\n")
    txtbox_schedaTec.insert(tk.END, "Cast: "+schedaTecnica['Actors']+"\n")
    txtbox_schedaTec.insert(tk.END, "Trama: "+schedaTecnica['Plot']+"\n")

    # riblocco la scrivibilità del textbox
    txtbox_schedaTec.configure(state='disabled')



# REALIZZAZIONE DELLA GUI
global txtbox_possibiliFilm
global txtbox_schedaTec
global path
global username
global apikey


username = "luca"
apikey = "Insert valid API"
path = ""


# finestra
root = tk.Tk()

### CAMPI DI TESTO ###

# campo di inserimento titolo del film
canvas_newMovie = tk.Canvas(root, width = 400, height = 20)
canvas_newMovie.grid(column=0, row=0)
entry_newMovie = tk.Entry (root) 
canvas_newMovie.create_window(200, 10, window=entry_newMovie, width=200)

## label nuovo username
label_newMovie = tk.Label(root, text= "Titolo film")
canvas_newMovie.create_window(50, 10, window=label_newMovie)

# textbox per tutti i film 
txtbox_possibiliFilm = tk.Text(root, height=10, width=100)
txtbox_possibiliFilm.configure(state='disabled')
txtbox_possibiliFilm.grid(column=0, row=2)

# campo inserimento codice
canvas_codice = tk.Canvas(root, width = 400, height = 20)
canvas_codice.grid(column=0, row=3)
entry_codice = tk.Entry(root) 
canvas_codice.create_window(70, 10, window=entry_codice, width=50)

## label inserimento codice
label_codice= tk.Label(root, text= "Codice")
canvas_codice.create_window(0, 10, window=label_codice)

# textbox per scheda tecnica
txtbox_schedaTec = tk.Text(root, height=10, width=100)
txtbox_schedaTec.configure(state='disabled')
txtbox_schedaTec.grid(column=0, row=4)


### BOTTONI ###

# bottone per effettuare la ricerca di un nuovo film
searchFilmbtn = tk.Button(root, text="Cerca nuovo film", command=lambda: stampaPossibiliFilm(entry_newMovie.get()), width=20)
searchFilmbtn.grid(column=0, row=1)

# bottone per effettuare aggiungere il nuovo film alla lista
addFilmbtn = tk.Button(root, text="Aggiungi a lista", command=lambda: aggiungiFilm(entry_codice.get()), width=20)
addFilmbtn.grid(column=0, row=3)
canvas_codice.create_window(200, 10, window=addFilmbtn)

# bottone per visualizzare la scheda tecnica del film
schedaTecnicabtn = tk.Button(root, text="Scheda tecnica", command=lambda: mostraSchedaTecnica(entry_codice.get()), width=20)
schedaTecnicabtn.grid(column=0, row=3)
canvas_codice.create_window(400, 10, window=schedaTecnicabtn)


# lancia finestra
root.mainloop()