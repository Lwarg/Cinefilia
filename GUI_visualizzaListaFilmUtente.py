import tkinter as tk
import requests
import json
from PIL import Image,ImageTk #INSTALLARE LA LIBRERIA imageio
import io

# Funzione corrispondente al bottone visualizzaFilm
def visualizzaListaFilm(user):

    global txtbox_possibiliFilm

    # rendo scrivibile il textbox
    txtbox_possibiliFilm.configure(state='normal')
    txtbox_possibiliFilm.insert(tk.END, "cercando film...")
    txtbox_possibiliFilm.delete("1.0","end")

    elencoFilm = open('C:/Users/simac/Google Drive/appCinefilia/elencoFilmdi'+ user +'.txt','r')
    
    # richiesta titolo film tramite API
    apikey = "8ca5768b&" # 1000 requests al giorno
    
    # restituisco in output i film visti dall'ultimo al primo
    count = 1
    lista = []
    for film in elencoFilm:
        idFilm = film.strip()
        lista.append(idFilm)
    lista.reverse()
    for film in lista:
        url = "http://www.omdbapi.com/?i="+film+"&apikey="+apikey
        response = requests.request("GET", url)
        data = json.loads(response.text)
        testo = str(count)+" - "+ data['Title'] + "\n"
        txtbox_possibiliFilm.insert(tk.END, testo)
        url_immagine = ""+ data ['Poster'] + ""
        response = requests.get(url_immagine)
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data))) 
        immagine = tk.Label(image=img)
        immagine.image = img
        immagine.place(x=500, y=count*100)
        count +=1

    # riblocco la scrivibilità del textbox
    txtbox_possibiliFilm.configure(state='disabled')


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
txtbox_possibiliFilm = tk.Text(root, height=100, width=100)
txtbox_possibiliFilm.configure(state='disabled')
txtbox_possibiliFilm.grid(column=0, row=2)

# bottone per visualizzare la lista dei film
visualizzaFilm = tk.Button(root, text="Lista dei film visti", command=lambda: visualizzaListaFilm(username), width=20)
visualizzaFilm.grid(column=0, row=0)

# lancia finestra
root.mainloop()