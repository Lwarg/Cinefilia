import tkinter as tk
import requests
import json



# funzione corrispondente al bottone registerbtn (per registrare un nuovo utente)
def stampaPossibiliFilm(user, film):
    global username
    global testo_possibiliFilm
    global txtbox_possibiliFilm
    global apikey

    # rendo scrivibile il textbox
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






# REALIZZAZIONE DELLA GUI
global testo_possibiliFilm
global txtbox_possibiliFilm
global username
global apikey


username = "luca"
apikey = "Insert valid API"

# finestra
root = tk.Tk()

# campo di inserimento titolo del film
canvas_newMovie = tk.Canvas(root, width = 400, height = 20)
canvas_newMovie.grid(column=0, row=1)
entry_newMovie = tk.Entry (root) 
canvas_newMovie.create_window(200, 10, window=entry_newMovie, width=200)

## label nuovo username
label_newMovie = tk.Label(root, text= "Titolo film")
canvas_newMovie.create_window(50, 10, window=label_newMovie)

# textbox con tutti i film possibili (quelli col titolo simile a quello inserito)
textVar = []
testo_possibiliFilm = ""
textVar.append(tk.StringVar())
txtbox_possibiliFilm = tk.Text(root, height=10, width=100)
txtbox_possibiliFilm.configure(state='disabled')
txtbox_possibiliFilm.grid(column=0, row=2)
#canvas_possibleNewMovies = tk.Canvas(root, width = 400, height = 200)
#canvas_possibleNewMovies.grid(column=0, row=2)
#entry_possibleNewMovies = tk.Entry (root) 
#canvas_possibleNewMovies.create_window(200, 50, window=entry_possibleNewMovies, width = 400, height = 100)



# bottone per effettuare la registrazione
registerbtn = tk.Button(root, text="Aggiungi nuovo film", command=lambda: stampaPossibiliFilm(username, entry_newMovie.get()), width=20)
registerbtn.grid(column=0, row=0)


# lancia finestra
root.mainloop()