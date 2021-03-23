import tkinter as tk
import requests
import json

# Funzione corrispondente al bottone visualizzaFilm
def visualizzaListaFilm(user):
    elencoFilm = open('C:/Users/simac/Google Drive/appCinefilia/elencoFilmdi'+ user +'.txt','r')
# richiesta titolo film tramite API
    apikey = "8ca5768b&" # 1000 requests al giorno
# restituisco in output i film visti dall'ultimo al primo
    count = 1
    for film in reversed(list(elencoFilm)):
        url = "http://www.omdbapi.com/?i="+film[:-1]+"&apikey="+apikey
        response = requests.request("GET", url)
        # print(response)
        data = json.loads(response.text)
        print(count,"-",data['Title'])
        count +=1


# REALIZZAZIONE DELLA GUI
global testo_possibiliFilm
global txtbox_possibiliFilm
global username
global apikey

username = "luca"
apikey = "8ca5768b&"

# finestra
root = tk.Tk()

# textbox con tutti i film visti dall'utente (si parte dall'ultimo e si va a ritroso)
textVar = []
testo_possibiliFilm = ""
textVar.append(tk.StringVar())
txtbox_possibiliFilm = tk.Text(root, height=10, width=100)
txtbox_possibiliFilm.configure(state='disabled')
txtbox_possibiliFilm.grid(column=0, row=2)

# bottone per visualizzare la lista dei film
visualizzaFilm = tk.Button(root, text="Lista dei film visti", command=lambda: visualizzaListaFilm(username), width=20)
visualizzaFilm.grid(column=0, row=0)

# lancia finestra
root.mainloop()