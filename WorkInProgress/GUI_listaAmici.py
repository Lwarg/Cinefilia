import tkinter as tk
import requests
import json

def visualizzaListaAmici():
    global database
    global utente
    global apikey
    global txtbox_mieiAmici

    txtbox_mieiAmici.configure(state='normal')
    txtbox_mieiAmici.insert(tk.END, "ricerca in corso...")
    txtbox_mieiAmici.delete("1.0","end")

    fileTesto = open(''+ database +'/amicidi'+ utente + '.txt','r')
    count = 1
    for riga in fileTesto:
        testo = str(count)+" - "+ riga.strip() + "\n"
        txtbox_mieiAmici.insert(tk.END, testo)
        count += 1
    txtbox_mieiAmici.configure(state='disabled')
    visualizzaFilmAmico.configure(state='normal')

def visualizzaFilm(codice):

    global database
    global utente
    global apikey
    global txtbox_filmAmici

    txtbox_filmAmici.configure(state='normal')
    txtbox_filmAmici.insert(tk.END, "ricerca in corso...")
    txtbox_filmAmici.delete("1.0","end")

    fileTesto = open(''+ database +'/amicidi'+ utente + '.txt','r')
    counter = 1
    for riga in fileTesto:
        if counter <= int(codice):
            amico = riga.strip()
            counter += 1
    listaFilm = open(''+ database +'/elencoFilmdi'+ amico + '.txt','r')
    contatore = 1
    lista = []
    for film in listaFilm:
        idFilm = film.strip()
        lista.append(idFilm)
    lista.reverse()
    for film in lista:
        url = "http://www.omdbapi.com/?i="+film+"&apikey="+apikey
        response = requests.request("GET", url)
        data = json.loads(response.text)
        testo = str(contatore)+" - "+ data['Title'] + "\n"
        txtbox_filmAmici.insert(tk.END, testo)
        contatore += 1
    
    txtbox_filmAmici.configure(state='disable')

####################################################################################

global database
global utente
global apikey
global txtbox_mieiAmici
global txtbox_filmAmici

utente = "Simone"
apikey = "8ca5768b&"
database = "C:/Users/simac/Google Drive/appCinefilia"

# finestra base
tabListaAmici = tk.Tk()

# bottone per visualizzare la lista degli amici di un utente
visualizzaAmici = tk.Button(tabListaAmici, text="Visualizza Amici", command=lambda: visualizzaListaAmici(), width=20)
visualizzaAmici.grid(column=0, row=1)
visualizzaAmici.configure(state='normal')

# textbox per tutti gli amici 
txtbox_mieiAmici = tk.Text(tabListaAmici, height=10, width=100)
txtbox_mieiAmici.configure(state='disabled')
txtbox_mieiAmici.grid(column=0, row=2)

# campo inserimento codice
canvas_codice = tk.Canvas(tabListaAmici, width = 400, height = 20)
canvas_codice.grid(column=0, row=3)
entry_codice = tk.Entry(tabListaAmici) 
canvas_codice.create_window(70, 10, window=entry_codice, width=50)
entry_codice.configure(state='normal')

## label inserimento codice
label_codice= tk.Label(tabListaAmici, text= "Codice")
canvas_codice.create_window(0, 10, window=label_codice)

# bottone per visualizzare i film dell'amico seguito
visualizzaFilmAmico = tk.Button(tabListaAmici, text="Vedi i film del tuo amico", command=lambda: visualizzaFilm(entry_codice.get()), width=20)
visualizzaFilmAmico.grid(column=0, row=3)
canvas_codice.create_window(200, 10, window=visualizzaFilmAmico)
visualizzaFilmAmico.configure(state='disabled')

# textbox per visualizzare i film degli amici 
txtbox_filmAmici = tk.Text(tabListaAmici, height=100, width=100)
txtbox_filmAmici.configure(state='disabled')
txtbox_filmAmici.grid(column=0, row=4)

# lancia finestra
tabListaAmici.mainloop()