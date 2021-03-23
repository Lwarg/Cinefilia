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
#    for film in reversed(list(elencoFilm.read())):
    for film in elencoFilm:
        idFilm = film.strip()
        lista.append(idFilm)
    lista.reverse()
    for film in lista:
        url = "http://www.omdbapi.com/?i="+film+"&apikey="+apikey
        response = requests.request("GET", url)
        # print(response)
        data = json.loads(response.text)
        testo = str(count)+" - "+ data['Title'] + "\n"
        txtbox_possibiliFilm.insert(tk.END, testo)
        url_immagine = ""+ data ['Poster'] + ""
        response = requests.get(url_immagine)
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)))
        # immagine_byt = urlopen(url_immagine).read()
        # immagine_b64 = base64.encodebytes(immagine_byt)
        # foto = tk.PhotoImage(data=immagine_b64)
        # r = requests.get(data['Poster'])
        # im = Image.open(io.BytesIO(r.content))
        # im.save(im, format='JPEG')
        # immagine = im.getbuffer()
        panel = tk.Label(root, image=img)
        txtbox_possibiliFilm.insert(tk.END, panel.pack(side="bottom", fill="both", expand="yes"))
        # cv = tk.Canvas(bg='white')
        # cv.pack(side='top', fill='both', expand='yes')
        # cv.create_image(10, 10, image=foto, anchor='nw')
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
txtbox_possibiliFilm = tk.Text(root, height=10, width=100)
txtbox_possibiliFilm.configure(state='disabled')
txtbox_possibiliFilm.grid(column=0, row=2)

# bottone per visualizzare la lista dei film
visualizzaFilm = tk.Button(root, text="Lista dei film visti", command=lambda: visualizzaListaFilm(username), width=20)
visualizzaFilm.grid(column=0, row=0)

# lancia finestra
root.mainloop()