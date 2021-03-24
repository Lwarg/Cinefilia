import tkinter as tk
import requests
import json
from tkinter import ttk

###################################################################################################################
###################################################################################################################
###################################################################################################################

# FUNZIONI BOTTONI

### funzione corrispondente al bottone registerbtn (per registrare un nuovo utente)
def register(user, DBpath):
    txtbox_outputregistrazione.configure(state='normal')
    txtbox_outputregistrazione.insert(tk.END, "registrazione in corso...")
    txtbox_outputregistrazione.delete("1.0","end")

    # l'username viene appeso nel file users.txt che si trova nella cartella sincronizzata con google drive
    userGiaPresente = False
    fileTestoLettura = open(''+ DBpath +'/users.txt','r')
    fileTestoScrittura = open(''+ DBpath +'/users.txt','a')
    for riga in fileTestoLettura:
        if riga.strip() == user:
            userGiaPresente = True
    if not userGiaPresente:
        fileTestoScrittura.write("" + user + "\n")
        nuovoFileTesto = open('' + DBpath + '/elencoFilmdi' + user + '.txt','w')
        txtbox_outputregistrazione.insert(tk.END,user+" registrato correttamente")
    else: 
        txtbox_outputregistrazione.insert(tk.END,"Username già presente")
        txtbox_outputregistrazione.configure(state='disabled')

###################################################################################################################

### funzione corrispondente al bottone loginbtn (per loggare un utente)
def login(user, DBpath):
    global utente
    global database

    txtbox_outputlogin.configure(state='normal')
    txtbox_outputlogin.insert(tk.END, "accesso in corso...")
    txtbox_outputlogin.delete("1.0","end")

    try:
        database = DBpath
        # l'username viene appeso nel file users.txt che si trova nella cartella sincronizzata con google drive
        userEsistente = False
        utenti = open(''+ DBpath +'/users.txt','r')
        for riga in utenti:
            if riga.strip() == user:
                userEsistente = True
                txtbox_outputlogin.insert(tk.END,"Accesso effettuato come "+user)
                utente = user

                # attivo tutti i bottoni e i campi di inserimento
                entry_newMovie.configure(state='normal')
                entry_newMovie.configure(state='normal')
                searchFilmbtn.configure(state='normal')


                break
        if not userEsistente:
            txtbox_outputlogin.insert(tk.END,"Utente non esistente, registrati")
            entry_newMovie.configure(state='disabled')
            entry_newMovie.configure(state='disabled')
            searchFilmbtn.configure(state='disabled')
            txtbox_schedaTec.configure(state='disabled')
            entry_codice.configure(state='disabled')
            addFilmbtn.configure(state='disabled')
            schedaTecnicabtn.configure(state='disabled')
    except:
        txtbox_outputlogin.insert(tk.END,"Database not found")
    finally:
        txtbox_outputlogin.configure(state='disabled')

###################################################################################################################

### funzione corrispondente al bottone searchFilmbtn (per cercare un nuovo film)
def stampaPossibiliFilm(film):
    global txtbox_possibiliFilm
    global apikey
    global data

    # rendo scrivibile il textbox e la pulisco se già scritta
    txtbox_possibiliFilm.configure(state='normal')
    txtbox_possibiliFilm.insert(tk.END, "cercando film...")
    txtbox_possibiliFilm.delete("1.0","end")

    # pulisco i campi inserimento codice e scheda tecnica e disabilito campo inserimanto codice e i bottoni aggiungi a lista e scheda tecnica
    txtbox_schedaTec.configure(state='normal')
    txtbox_schedaTec.insert(tk.END, "...")
    txtbox_schedaTec.delete("1.0","end")
    txtbox_schedaTec.configure(state='disabled')
    entry_codice.configure(state='disabled')
    addFilmbtn.configure(state='disabled')
    schedaTecnicabtn.configure(state='disabled')

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
            
            # abilito campo di inserimento codice e bottoni aggiungi a lista e scheda tecnica
            entry_codice.configure(state='normal')
            addFilmbtn.configure(state='normal')
            schedaTecnicabtn.configure(state='normal')

        else:
            txtbox_possibiliFilm.insert(tk.END,'Film NON trovato')
    except:
        txtbox_possibiliFilm.insert(tk.END,'API request error')

    
    # riblocco la scrivibilità del textbox
    txtbox_possibiliFilm.configure(state='disabled')

###################################################################################################################

### funzione corrispondente al bottone addbtn (per aggiungere un film alla lista )
def aggiungiFilm(codice):
    global utente
    global database
    global data

    
    # rendo scrivibile il textbox e la pulisco se già scritta
    txtbox_schedaTec.configure(state='normal')
    txtbox_schedaTec.insert(tk.END, "caricamento...")
    txtbox_schedaTec.delete("1.0","end")

    # prendo l'id del film corrispondente al codice inserito nell'apposito campo
    film_scelto = data['Search'][int(codice)-1]['imdbID']

    # il film viene appeso nel file elencoFilmdiuser.txt che si trova nella cartella sincronizzata con google drive
    filmGiaPresente = False
    fileTestoLettura = open(''+ database +'/elencoFilmdi'+utente+'.txt','r')
    for riga in fileTestoLettura:
        if riga.strip() == film_scelto:
            filmGiaPresente = True
            break
    fileTestoLettura.close()
    if not filmGiaPresente:
        fileTestoScrittura = open(''+ database +'/elencoFilmdi'+utente+'.txt','a')
        fileTestoScrittura.write("" + film_scelto + "\n")
        txtbox_schedaTec.insert(tk.END, data['Search'][int(codice)-1]['Title']+" aggiunto ai Miei Film")
        fileTestoScrittura.close()
    else: 
        txtbox_schedaTec.insert(tk.END,data['Search'][int(codice)-1]['Title']+" è già presente in elenco")





    
    

    # riblocco la scrivibilità del textbox
    txtbox_schedaTec.configure(state='disabled')


###################################################################################################################

### funzione corrispondente al bottone schedaTecnicabtn (per visualizzare la scheda tecnica di un film )
def mostraSchedaTecnica(codice):
    global utente
    global txtbox_schedaTec
    global apikey
    global data

    try:
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
    except:
        txtbox_schedaTec.insert(tk.END, "Codice non valido")

    # riblocco la scrivibilità del textbox
    txtbox_schedaTec.configure(state='disabled')


###################################################################################################################
###################################################################################################################
###################################################################################################################

# REALIZZAZIONE DELLA GUI
global txtbox_possibiliFilm
global txtbox_schedaTec
global database
global utente
global apikey


apikey = "Insert a valid API"

# finestra base
root = tk.Tk()

# tabs di primo livello
tabControl = ttk.Notebook(root)
tabAccedi = ttk.Frame(tabControl)
tabCerca = ttk.Frame(tabControl)
tabMyMovies = ttk.Frame(tabControl)
tabStatistiche = ttk.Frame(tabControl)

tabControl.add(tabAccedi, text ='Accedi')
tabControl.add(tabCerca, text ='Cerca')
tabControl.add(tabMyMovies, text ='Miei Film')
tabControl.add(tabStatistiche, text ='Statistiche')
tabControl.pack(expand = 1, fill ="both")

###################################################################################################################

### TAB LOG ###

# tabs di secondo livello
tabAccediControl = ttk.Notebook(tabAccedi)
tabRegistra = ttk.Frame(tabAccediControl)
tabLogin = ttk.Frame(tabAccediControl)

tabAccediControl.add(tabRegistra, text ='Registrati')
tabAccediControl.add(tabLogin, text ='Login')
tabAccediControl.pack(expand = 1, fill ="both")


### TAB REGISTRATI ###

# campo di inserimento nuovo username
canvas_newUser = tk.Canvas(tabRegistra, width = 400, height = 20)
canvas_newUser.grid(column=0, row=1)
entry_newUser = tk.Entry (tabRegistra) 
canvas_newUser.create_window(200, 10, window=entry_newUser)

# label nuovo username
label_newUser = tk.Label(tabRegistra, text= "Nuovo Username")
canvas_newUser.create_window(50, 10, window=label_newUser)

# campo di inserimento path della cartella sincronizzata con google drive
canvas_newDB = tk.Canvas(tabRegistra, width = 400, height = 20)
canvas_newDB.grid(column=0, row=2)
entry_newDB = tk.Entry (tabRegistra) 
canvas_newDB.create_window(200, 10, window=entry_newDB)

# label database
label_newDB = tk.Label(tabRegistra, text= "Path Database")
canvas_newDB.create_window(50, 10, window=label_newDB)

# textbox per messaggio di output
txtbox_outputregistrazione = tk.Text(tabRegistra, height=5, width=100)
txtbox_outputregistrazione.configure(state='disabled')
txtbox_outputregistrazione.grid(column=0, row=4)

# bottone per effettuare la registrazione
registerbtn = tk.Button(tabRegistra, text="Registrati", command=lambda: register(entry_newUser.get(), entry_newDB.get()), width=20)
registerbtn.grid(column=0, row=3)


### TAB LOGIN ###

# campo di inserimento nuovo username
canvas_User = tk.Canvas(tabLogin, width = 400, height = 20)
canvas_User.grid(column=0, row=1)
entry_User = tk.Entry (tabLogin) 
canvas_User.create_window(200, 10, window=entry_User)

# label nuovo username
label_User = tk.Label(tabLogin, text= "Username")
canvas_User.create_window(50, 10, window=label_User)

# campo di inserimento path della cartella sincronizzata con google drive
canvas_DB = tk.Canvas(tabLogin, width = 400, height = 20)
canvas_DB.grid(column=0, row=2)
entry_DB = tk.Entry (tabLogin) 
canvas_DB.create_window(200, 10, window=entry_DB)

# label database
label_DB = tk.Label(tabLogin, text= "Path Database")
canvas_DB.create_window(50, 10, window=label_DB)

# textbox per messaggio di output
txtbox_outputlogin = tk.Text(tabLogin, height=5, width=100)
txtbox_outputlogin.configure(state='disabled')
txtbox_outputlogin.grid(column=0, row=4)

# bottone per effettuare la registrazione
loginbtn = tk.Button(tabLogin, text="Login", command=lambda: login(entry_User.get(), entry_DB.get()), width=20)
loginbtn.grid(column=0, row=3)


###################################################################################################################

### TAB CERCA ###

# campo di inserimento titolo del film
canvas_newMovie = tk.Canvas(tabCerca, width = 400, height = 20)
canvas_newMovie.grid(column=0, row=0)
entry_newMovie = tk.Entry (tabCerca) 
canvas_newMovie.create_window(200, 10, window=entry_newMovie, width=200)
entry_newMovie.configure(state='disabled')

## label nuovo username
label_newMovie = tk.Label(tabCerca, text= "Titolo film")
canvas_newMovie.create_window(50, 10, window=label_newMovie)

# textbox per tutti i film 
txtbox_possibiliFilm = tk.Text(tabCerca, height=10, width=100)
txtbox_possibiliFilm.configure(state='disabled')
txtbox_possibiliFilm.grid(column=0, row=2)

# campo inserimento codice
canvas_codice = tk.Canvas(tabCerca, width = 400, height = 20)
canvas_codice.grid(column=0, row=3)
entry_codice = tk.Entry(tabCerca) 
canvas_codice.create_window(70, 10, window=entry_codice, width=50)
entry_codice.configure(state='disabled')

## label inserimento codice
label_codice= tk.Label(tabCerca, text= "Codice")
canvas_codice.create_window(0, 10, window=label_codice)

# textbox per scheda tecnica
txtbox_schedaTec = tk.Text(tabCerca, height=10, width=100)
txtbox_schedaTec.configure(state='disabled')
txtbox_schedaTec.grid(column=0, row=4)

# bottone per effettuare la ricerca di un nuovo film
searchFilmbtn = tk.Button(tabCerca, text="Cerca nuovo film", command=lambda: stampaPossibiliFilm(entry_newMovie.get()), width=20)
searchFilmbtn.grid(column=0, row=1)
searchFilmbtn.configure(state='disabled')

# bottone per effettuare aggiungere il nuovo film alla lista
addFilmbtn = tk.Button(tabCerca, text="Aggiungi a lista", command=lambda: aggiungiFilm(entry_codice.get()), width=20)
addFilmbtn.grid(column=0, row=3)
canvas_codice.create_window(200, 10, window=addFilmbtn)
addFilmbtn.configure(state='disabled')

# bottone per visualizzare la scheda tecnica del film
schedaTecnicabtn = tk.Button(tabCerca, text="Scheda tecnica", command=lambda: mostraSchedaTecnica(entry_codice.get()), width=20)
schedaTecnicabtn.grid(column=0, row=3)
canvas_codice.create_window(400, 10, window=schedaTecnicabtn)
schedaTecnicabtn.configure(state='disabled')


###################################################################################################################

# lancia finestra
root.mainloop()