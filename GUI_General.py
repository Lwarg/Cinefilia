import tkinter as tk
import requests
import json
import io
import operator
import pandas as pd
import numpy as np

from tkinter import ttk
from tkinter import *
from tkinter import Canvas
from PIL import Image,ImageTk
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error


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
    numero_utenti = 0
    for riga in fileTestoLettura:
        numero_utenti += 1
        if riga.strip().split(",")[1] == user:
            userGiaPresente = True
    if not userGiaPresente:
        nuovo_id = str(numero_utenti+1001)
        fileTestoScrittura.write(""+ nuovo_id +"," + user + "\n")
        nuovoFileTesto = open('' + DBpath + '/elencoFilmdi' + user + '.txt','w')
        nuovoFileListaAmici = open(''+ DBpath + '/amicidi'+ user + '.txt', 'w')
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

    #try:
    database = DBpath
    # l'username viene appeso nel file users.txt che si trova nella cartella sincronizzata con google drive
    userEsistente = False
    utenti = open(''+ DBpath +'/users.txt','r')
    for riga in utenti:
        if riga.strip().split(",")[1]  == user:
            userEsistente = True
            utente = user
            # carico i dati dell'utente
            visualizzaListaFilm()
            visualizzaStatistiche()
            visualizzaListaAmici()
            # attivo tutti i bottoni e i campi di inserimento
            entry_newMovie.configure(state='normal')
            entry_newMovie.configure(state='normal')
            searchFilmbtn.configure(state='normal')
            logoutbtn.configure(state='normal')
            entry_ricercaUtente.configure(state='normal')
            searchUserbtn.configure(state='normal')
            entry_nuovoCommento.configure(state='normal')
            pubblicabtn.configure(state='normal')
            aggiornabtn.configure(state='normal')
            segnalabtn.configure(state='normal')
            visualizzaAmici.configure(state='normal')
            suggeriscibtn.configure(state='normal')
            loginbtn.configure(state='disabled')
            # messaggio di output all'utente
            txtbox_outputlogin.insert(tk.END,"Accesso effettuato come "+user)
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
        entry_ricercaUtente.configure(state='disabled')
        searchUserbtn.configure(state='disabled')
        seguiUtentebtn.configure(state='disabled')
        eliminaAmicobtn.configure(state='disabled')
        entry_nuovoCommento.configure(state='disabled')
        pubblicabtn.configure(state='disabled')
        aggiornabtn.configure(state='disabled')
        segnalabtn.configure(state='disabled')
        visualizzaAmici.configure(state='disabled')
        suggeriscibtn.configure(state='disabled')
    #except:
    #    txtbox_outputlogin.insert(tk.END,"Errore di accesso")
    #finally:
    #    txtbox_outputlogin.configure(state='disabled')


###################################################################################################################

### funzione corrispondente al bottone logoutbtn (per loggare un utente)
def logout():
    global utente
    global database

    testo = "Uscita in corso..."

    # ripulitura campi di testo
    txtbox_outputlogin.configure(state='normal')
    txtbox_outputlogin.insert(tk.END, testo)
    txtbox_outputlogin.delete("1.0","end")
    txtbox_outputlogin.configure(state='disabled')

    txtbox_possibiliFilm.configure(state='normal')
    txtbox_possibiliFilm.insert(tk.END, testo)
    txtbox_possibiliFilm.delete("1.0","end")
    txtbox_possibiliFilm.configure(state='disabled')

    txtbox_schedaTec.configure(state='normal')
    txtbox_schedaTec.insert(tk.END, testo)
    txtbox_schedaTec.delete("1.0","end")
    txtbox_schedaTec.configure(state='disabled')

    txtbox_mieiFilm.configure(state='normal')
    txtbox_mieiFilm.insert(tk.END, testo)
    txtbox_mieiFilm.delete("1.0","end")
    txtbox_mieiFilm.configure(state='disabled')

    txtbox_statistiche.configure(state='normal')
    txtbox_statistiche.insert(tk.END, testo)
    txtbox_statistiche.delete("1.0","end")
    txtbox_statistiche.configure(state='disabled')

    txtbox_numeroAmici.configure(state='normal')
    txtbox_numeroAmici.insert(tk.END, testo)
    txtbox_numeroAmici.delete("1.0","end")
    txtbox_numeroAmici.configure(state='disabled')

    txtbox_mieiAmici.configure(state='normal')
    txtbox_mieiAmici.insert(tk.END, testo)
    txtbox_mieiAmici.delete("1.0","end")
    txtbox_mieiAmici.configure(state='disabled')

    txtbox_filmAmici.configure(state='normal')
    txtbox_filmAmici.insert(tk.END, testo)
    txtbox_filmAmici.delete("1.0","end")
    txtbox_filmAmici.configure(state='disabled')

    txtbox_output.configure(state='normal')
    txtbox_output.insert(tk.END, testo)
    txtbox_output.delete("1.0","end")
    txtbox_output.configure(state='disabled')

    txtbox_bacheca.configure(state='normal')
    txtbox_bacheca.insert(tk.END, testo)
    txtbox_bacheca.delete("1.0","end")
    txtbox_bacheca.configure(state='disabled')

    txtbox_suggeriti.configure(state='normal')
    txtbox_suggeriti.insert(tk.END, testo)
    txtbox_suggeriti.delete("1.0","end")
    txtbox_suggeriti.configure(state='disabled')

    entry_newMovie.configure(state='normal')
    entry_newMovie.insert(tk.END, '00')
    entry_newMovie.delete(0, 'end')
    entry_newMovie.configure(state='disabled')

    entry_codice.configure(state='normal')
    entry_codice.insert(tk.END, '00')
    entry_codice.delete(0, 'end')
    entry_codice.configure(state='disabled')

    entry_codice_amico.configure(state='normal')
    entry_codice_amico.insert(tk.END, '00')
    entry_codice_amico.delete(0, 'end')
    entry_codice_amico.configure(state='disabled')

    entry_ricercaUtente.configure(state='normal')
    entry_ricercaUtente.insert(tk.END, '00')
    entry_ricercaUtente.delete(0, 'end')
    entry_ricercaUtente.configure(state='disabled')

    entry_nuovoCommento.configure(state='normal')
    entry_nuovoCommento.insert(tk.END, '00')
    entry_nuovoCommento.delete(0, 'end')
    entry_nuovoCommento.configure(state='disabled')
    
    # Disabilito il bottone logout e quelli delle altre tab
    logoutbtn.configure(state='disabled')
    searchFilmbtn.configure(state='disabled')
    schedaTecnicabtn.configure(state='disabled')
    addFilmbtn.configure(state='disabled')
    searchUserbtn.configure(state='disabled')
    seguiUtentebtn.configure(state='disabled')
    eliminaAmicobtn.configure(state='disabled')
    visualizzaFilmAmico.configure(state='disabled')
    pubblicabtn.configure(state='disabled')
    aggiornabtn.configure(state='disabled')
    segnalabtn.configure(state='disabled')
    visualizzaAmici.configure(state='disabled')
    suggeriscibtn.configure(state='disabled')

    # abilito il login
    loginbtn.configure(state='normal')
    
    
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

### funzioni corrispondenti al bottone addbtn (per aggiungere un film alla lista )

#Funzioni per salvare il voto
def salvaVoto1():
    global utente
    global database
    global win
    global win_due
    fileTestoScrittura = open(''+ database +'/elencoFilmdi'+utente+'.txt','a')
    fileTestoScrittura.write("1\n")
    win_due = tk.Toplevel()
    win_due.wm_title("Window")
    l_due = tk.Label(win_due, text="Grazie per il tuo voto!")
    l_due.grid(row=0, column=0)
    star_one_left = tk.Canvas(win_due,width=100,height=100)
    star_one_left.grid(row=1,column=0)
    points1 = [50,70,25,90,35,60,10,40,40,40,50,10]
    star_one_left.create_polygon(points1,outline='red',fill='orange',width=2)
    bottone_uscita = tk.Button(win_due, text="OK", command=win_due.destroy,width=10)
    bottone_uscita.grid(row=2,column=0)
    win.destroy()
def salvaVoto2():
    global utente
    global database
    global win
    global win_due
    fileTestoScrittura = open(''+ database +'/elencoFilmdi'+utente+'.txt','a')
    fileTestoScrittura.write("2\n")
    win_due = tk.Toplevel()
    win_due.wm_title("Window")
    l_due = tk.Label(win_due, text="Grazie per il tuo voto!")
    l_due.grid(row=0, column=0)
    star_one = tk.Canvas(win_due,width=100,height=100)
    star_one.grid(row=1,column=0)
    points = [10,40,40,40,50,10,60,40,90,40,65,60,75,90,50,70,25,90,35,60]
    star_one.create_polygon(points,outline='red',fill='orange',width=2)
    bottone_uscita = tk.Button(win_due, text="OK", command=win_due.destroy,width=10)
    bottone_uscita.grid(row=2,column=0)
    win.destroy()
def salvaVoto3():
    global utente
    global database
    global win
    global win_due
    fileTestoScrittura = open(''+ database +'/elencoFilmdi'+utente+'.txt','a')
    fileTestoScrittura.write("3\n")
    win_due = tk.Toplevel()
    win_due.wm_title("Window")
    l_due = tk.Label(win_due, text="Grazie per il tuo voto!")
    l_due.grid(row=0, column=0)
    star_one = tk.Canvas(win_due,width=100,height=100)
    star_one.grid(row=1,column=0)
    star_one_left = tk.Canvas(win_due,width=100,height=100)
    star_one_left.grid(row=1,column=1)
    points = [10,40,40,40,50,10,60,40,90,40,65,60,75,90,50,70,25,90,35,60]
    points1 = [50,70,25,90,35,60,10,40,40,40,50,10]
    star_one.create_polygon(points,outline='red',fill='orange',width=2)
    star_one_left.create_polygon(points1,outline='red',fill='orange',width=2)
    bottone_uscita = tk.Button(win_due, text="OK", command=win_due.destroy,width=10)
    bottone_uscita.grid(row=2,column=0)
    win.destroy()
def salvaVoto4():
    global utente
    global database
    global win
    global win_due
    fileTestoScrittura = open(''+ database +'/elencoFilmdi'+utente+'.txt','a')
    fileTestoScrittura.write("4\n")
    win_due = tk.Toplevel()
    win_due.wm_title("Window")
    l_due = tk.Label(win_due, text="Grazie per il tuo voto!")
    l_due.grid(row=0, column=0)
    star_one = tk.Canvas(win_due,width=100,height=100)
    star_one.grid(row=1,column=0)
    star_two = tk.Canvas(win_due,width=100,height=100)
    star_two.grid(row=1,column=1)
    points = [10,40,40,40,50,10,60,40,90,40,65,60,75,90,50,70,25,90,35,60]
    star_one.create_polygon(points,outline='red',fill='orange',width=2)
    star_two.create_polygon(points,outline='red',fill='orange',width=2)
    bottone_uscita = tk.Button(win_due, text="OK", command=win_due.destroy,width=10)
    bottone_uscita.grid(row=2,column=0)
    win.destroy()
def salvaVoto5():
    global utente
    global database
    global win
    global win_due
    fileTestoScrittura = open(''+ database +'/elencoFilmdi'+utente+'.txt','a')
    fileTestoScrittura.write("5\n")
    win_due = tk.Toplevel()
    win_due.wm_title("Window")
    l_due = tk.Label(win_due, text="Grazie per il tuo voto!")
    l_due.grid(row=0, column=0)
    star_one = tk.Canvas(win_due,width=100,height=100)
    star_one.grid(row=1,column=0)
    star_two = tk.Canvas(win_due,width=100,height=100)
    star_two.grid(row=1,column=1)
    star_one_left = tk.Canvas(win_due,width=100,height=100)
    star_one_left.grid(row=1,column=2)
    points = [10,40,40,40,50,10,60,40,90,40,65,60,75,90,50,70,25,90,35,60]
    points1 = [50,70,25,90,35,60,10,40,40,40,50,10]
    star_one.create_polygon(points,outline='red',fill='orange',width=2)
    star_two.create_polygon(points,outline='red',fill='orange',width=2)
    star_one_left.create_polygon(points1,outline='red',fill='orange',width=2)
    bottone_uscita = tk.Button(win_due, text="OK", command=win_due.destroy,width=10)
    bottone_uscita.grid(row=2,column=0)
    win.destroy()
def salvaVoto6():
    global utente
    global database
    global win
    global win_due
    fileTestoScrittura = open(''+ database +'/elencoFilmdi'+utente+'.txt','a')
    fileTestoScrittura.write("6\n")
    win_due = tk.Toplevel()
    win_due.wm_title("Window")
    l_due = tk.Label(win_due, text="Grazie per il tuo voto!")
    l_due.grid(row=0, column=0)
    star_one = tk.Canvas(win_due,width=100,height=100)
    star_one.grid(row=1,column=0)
    star_two = tk.Canvas(win_due,width=100,height=100)
    star_two.grid(row=1,column=1)
    star_three = tk.Canvas(win_due,width=100,height=100)
    star_three.grid(row=1,column=2)
    points = [10,40,40,40,50,10,60,40,90,40,65,60,75,90,50,70,25,90,35,60]
    star_one.create_polygon(points,outline='red',fill='orange',width=2)
    star_two.create_polygon(points,outline='red',fill='orange',width=2)
    star_three.create_polygon(points,outline='red',fill='orange',width=2)
    bottone_uscita = tk.Button(win_due, text="OK", command=win_due.destroy,width=10)
    bottone_uscita.grid(row=2,column=0)
    win.destroy()
def salvaVoto7():
    global utente
    global database
    global win
    global win_due
    fileTestoScrittura = open(''+ database +'/elencoFilmdi'+utente+'.txt','a')
    fileTestoScrittura.write("7\n")
    win_due = tk.Toplevel()
    win_due.wm_title("Window")
    l_due = tk.Label(win_due, text="Grazie per il tuo voto!")
    l_due.grid(row=0, column=0)
    star_one = tk.Canvas(win_due,width=100,height=100)
    star_one.grid(row=1,column=0)
    star_two = tk.Canvas(win_due,width=100,height=100)
    star_two.grid(row=1,column=1)
    star_three = tk.Canvas(win_due,width=100,height=100)
    star_three.grid(row=1,column=2)
    star_one_left = tk.Canvas(win_due,width=100,height=100)
    star_one_left.grid(row=1,column=3)
    points = [10,40,40,40,50,10,60,40,90,40,65,60,75,90,50,70,25,90,35,60]
    points1 = [50,70,25,90,35,60,10,40,40,40,50,10]
    star_one.create_polygon(points,outline='red',fill='orange',width=2)
    star_two.create_polygon(points,outline='red',fill='orange',width=2)
    star_three.create_polygon(points,outline='red',fill='orange',width=2)
    star_one_left.create_polygon(points1,outline='red',fill='orange',width=2)
    bottone_uscita = tk.Button(win_due, text="OK", command=win_due.destroy,width=10)
    bottone_uscita.grid(row=2,column=0)   
    win.destroy()
def salvaVoto8():
    global utente
    global database
    global win
    global win_due
    fileTestoScrittura = open(''+ database +'/elencoFilmdi'+utente+'.txt','a')
    fileTestoScrittura.write("8\n")
    win_due = tk.Toplevel()
    win_due.wm_title("Window")
    l_due = tk.Label(win_due, text="Grazie per il tuo voto!")
    l_due.grid(row=0, column=0)
    star_one = tk.Canvas(win_due,width=100,height=100)
    star_one.grid(row=1,column=0)
    star_two = tk.Canvas(win_due,width=100,height=100)
    star_two.grid(row=1,column=1)
    star_three = tk.Canvas(win_due,width=100,height=100)
    star_three.grid(row=1,column=2)
    star_four = tk.Canvas(win_due,width=100,height=100)
    star_four.grid(row=1,column=3)
    points = [10,40,40,40,50,10,60,40,90,40,65,60,75,90,50,70,25,90,35,60]
    star_one.create_polygon(points,outline='red',fill='orange',width=2)
    star_two.create_polygon(points,outline='red',fill='orange',width=2)
    star_three.create_polygon(points,outline='red',fill='orange',width=2)
    star_four.create_polygon(points,outline='red',fill='orange',width=2)
    bottone_uscita = tk.Button(win_due, text="OK", command=win_due.destroy,width=10)
    bottone_uscita.grid(row=2,column=0)
    win.destroy()
def salvaVoto9():
    global utente
    global database
    global win
    global win_due
    fileTestoScrittura = open(''+ database +'/elencoFilmdi'+utente+'.txt','a')
    fileTestoScrittura.write("9\n")
    win_due = tk.Toplevel()
    win_due.wm_title("Window")
    l_due = tk.Label(win_due, text="Grazie per il tuo voto!")
    l_due.grid(row=0, column=0)
    star_one = tk.Canvas(win_due,width=100,height=100)
    star_one.grid(row=1,column=0)
    star_two = tk.Canvas(win_due,width=100,height=100)
    star_two.grid(row=1,column=1)
    star_three = tk.Canvas(win_due,width=100,height=100)
    star_three.grid(row=1,column=2)
    star_four = tk.Canvas(win_due,width=100,height=100)
    star_four.grid(row=1,column=3)
    star_one_left = tk.Canvas(win_due,width=100,height=100)
    star_one_left.grid(row=1,column=4)
    points = [10,40,40,40,50,10,60,40,90,40,65,60,75,90,50,70,25,90,35,60]
    points1 = [50,70,25,90,35,60,10,40,40,40,50,10]
    star_one.create_polygon(points,outline='red',fill='orange',width=2)
    star_two.create_polygon(points,outline='red',fill='orange',width=2)
    star_three.create_polygon(points,outline='red',fill='orange',width=2)
    star_four.create_polygon(points,outline='red',fill='orange',width=2)
    star_one_left.create_polygon(points1,outline='red',fill='orange',width=2)
    bottone_uscita = tk.Button(win_due, text="OK", command=win_due.destroy,width=10)
    bottone_uscita.grid(row=2,column=0)
    win.destroy()
def salvaVoto10():
    global utente
    global database
    global win
    global win_due
    fileTestoScrittura = open(''+ database +'/elencoFilmdi'+utente+'.txt','a')
    fileTestoScrittura.write("10\n")
    win_due = tk.Toplevel()
    win_due.wm_title("Window")
    l_due = tk.Label(win_due, text="Grazie per il tuo voto!")
    l_due.grid(row=0, column=0)
    star_one = tk.Canvas(win_due,width=100,height=100)
    star_one.grid(row=1,column=0)
    star_two = tk.Canvas(win_due,width=100,height=100)
    star_two.grid(row=1,column=1)
    star_three = tk.Canvas(win_due,width=100,height=100)
    star_three.grid(row=1,column=2)
    star_four = tk.Canvas(win_due,width=100,height=100)
    star_four.grid(row=1,column=3)
    star_five = tk.Canvas(win_due,width=100,height=100)
    star_five.grid(row=1,column=4)
    points = [10,40,40,40,50,10,60,40,90,40,65,60,75,90,50,70,25,90,35,60]
    star_one.create_polygon(points,outline='red',fill='orange',width=2)
    star_two.create_polygon(points,outline='red',fill='orange',width=2)
    star_three.create_polygon(points,outline='red',fill='orange',width=2)
    star_four.create_polygon(points,outline='red',fill='orange',width=2)
    star_five.create_polygon(points,outline='red',fill='orange',width=2)
    bottone_uscita = tk.Button(win_due, text="OK", command=win_due.destroy,width=10)
    bottone_uscita.grid(row=2,column=0)
    win.destroy()
def salvaSkip():
    global utente
    global database
    global win
    fileTestoScrittura = open(''+ database +'/elencoFilmdi'+utente+'.txt','a')
    fileTestoScrittura.write("11\n")
    win.destroy()

# aggiungo la possibilità di assegnare un voto al film tramite pop-up
def valutazioneFilm():
    global win
    global voto
    global img_one
    global img_two
    img_one = tk.PhotoImage(file='leftStar_white.png')
    img_two = tk.PhotoImage(file='rightStar_white.png')
    win = tk.Toplevel()
    win.wm_title("Window")
    l = tk.Label(win, text="Aggiungi una valutazione al film!")
    l.grid(row=0, column=0)
    stellaSinistra_uno = ttk.Button(win, image=img_one,command=salvaVoto1)
    stellaSinistra_uno.grid(row=1, column=1)
    stellaDestra_uno = ttk.Button(win, image=img_two, command=salvaVoto2)
    stellaDestra_uno.grid(row=1, column=2)
    stellaSinistra_due = ttk.Button(win, image=img_one, command=salvaVoto3)
    stellaSinistra_due.grid(row=1, column=3)
    stellaDestra_due = ttk.Button(win, image=img_two, command=salvaVoto4)
    stellaDestra_due.grid(row=1, column=4)
    stellaSinistra_tre = ttk.Button(win, image=img_one, command=salvaVoto5)
    stellaSinistra_tre.grid(row=1, column=5)
    stellaDestra_tre = ttk.Button(win, image = img_two, command=salvaVoto6)
    stellaDestra_tre.grid(row=1, column=6)
    stellaSinistra_quattro = ttk.Button(win, image = img_one, command=salvaVoto7)
    stellaSinistra_quattro.grid(row=1, column=7)
    stellaDestra_quattro = ttk.Button(win, image = img_two, command=salvaVoto8)
    stellaDestra_quattro.grid(row=1, column=8)
    stellaSinistra_cinque = ttk.Button(win, image = img_one, command=salvaVoto9)
    stellaSinistra_cinque.grid(row=1, column=9)
    stellaDestra_cinque = ttk.Button(win, image = img_two, command=salvaVoto10)
    stellaDestra_cinque.grid(row=1, column=10)
    votoSkip = ttk.Button(win, text="Skip", command=salvaSkip)
    votoSkip.grid(row=2, column=5)

def aggiungiFilm(codice):
    global utente
    global database
    global data
    global voto
    global win

    
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
        if riga.strip().split(",")[0] == film_scelto:
            filmGiaPresente = True
            break
    fileTestoLettura.close()
    if not filmGiaPresente:
        fileTestoScrittura = open(''+ database +'/elencoFilmdi'+utente+'.txt','a')
        fileTestoScrittura.write("" + film_scelto + ",")
        valutazioneFilm()
        txtbox_schedaTec.insert(tk.END, data['Search'][int(codice)-1]['Title']+" aggiunto ai Miei Film")
        fileTestoScrittura.close()
        visualizzaListaFilm()
        visualizzaStatistiche()
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

### funzione corrispondente alla tab Miei Film (per visualizzare l'elenco dei miei film )

def visualizzaListaFilm():
    global txtbox_mieiFilm
    global database
    global utente
    global apikey
    global img

    # rendo scrivibile il textbox
    txtbox_mieiFilm.configure(state='normal')
    txtbox_mieiFilm.insert(tk.END, "cercando film...")
    txtbox_mieiFilm.delete("1.0","end")

    elencoFilm = open(database +'/elencoFilmdi'+ utente +'.txt','r')

    # restituisco in output i film visti dall'ultimo al primo
    count = 1
    lista = []
    for film in elencoFilm:
        idFilm = film.strip().split(",")[0]
        lista.append(idFilm)
    lista.reverse()
    for film in lista:
        try:
            url = "http://www.omdbapi.com/?i="+film+"&apikey="+apikey
            response = requests.request("GET", url)
            data = json.loads(response.text)
            #testo = str(count)+" - "+ data['Title'].upper() + "\n"
            #txtbox_mieiFilm.insert(tk.END, testo)
            url_immagine = ""+ data ['Poster'] + ""
            response = requests.get(url_immagine)
            img_data = response.content
            img = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data))) 
            immagine = tk.Label(image=img)
            immagine.image = img
            txtbox_mieiFilm.image_create(tk.END, image=img)
            txtbox_mieiFilm.insert(tk.END, "    ")
            #immagine.place(x=500, y=count*100)
        except:
            url = "http://www.omdbapi.com/?i="+film+"&apikey="+apikey
            response = requests.request("GET", url)
            data = json.loads(response.text)
            testo = str(count)+" - "+ data['Title'].upper() + "\n"
            txtbox_mieiFilm.insert(tk.END, testo)

        count +=1

    # riblocco la scrivibilità del textbox
    txtbox_possibiliFilm.configure(state='disabled')


###################################################################################################################

### funzione corrispondente alla tab statistiche 

def visualizzaStatistiche():
    global txtbox_statistiche
    global database
    global utente
    global apikey

    # rendo scrivibile il textbox
    txtbox_statistiche.configure(state='normal')
    txtbox_statistiche.insert(tk.END, "caricamento...")
    txtbox_statistiche.tag_config("labeltag", font="Italic 12 bold", foreground="navy")
    txtbox_statistiche.tag_config("texttag", font="Italic 11", foreground="black")
    txtbox_statistiche.tag_config("texttagB", font="Italic 11 bold", foreground="black")
    txtbox_statistiche.delete("1.0","end")

    elencoFilm = open(database +'/elencoFilmdi'+ utente +'.txt','r')

    schede_tecniche = []
    for film in elencoFilm:
        idFilm = film.strip().split(",")[0]
        # ricerca film tramite API usando l'ID del film
        url = "http://www.omdbapi.com/?i="+idFilm+"&apikey="+apikey
        response = requests.request("GET", url)
        schede_tecniche.append(json.loads(response.text))

    # numero film visti
    numero_film_visti = len(schede_tecniche)
    txtbox_statistiche.insert(tk.END,"Numero di film visti: ", "labeltag")
    txtbox_statistiche.insert(tk.END, str(numero_film_visti)+"\n\n", "texttag")
    durata = 0
    generi = dict()
    registi = dict()
    attori = dict()
    for film in schede_tecniche:
        # somma durata totale 
        if film['Runtime'].split(" ")[0] == 'N/A':
            durata += 90 # se non ho i dati aggiungo una durata stimata di 90 minuti 
        else:
            durata = durata + int(film['Runtime'].split(" ")[0])
        # conteggio generi
        tipologie = film['Genre'].split(", ")
        for genere in tipologie:
            if genere != 'N/A':
                if genere in generi:
                    generi[genere] += 1
                else:
                    generi[genere] = 1
        # conteggio registi
        if film['Director'] != 'N/A':
            if film['Director'] in registi:
                registi[film['Director']] += 1
            else:
                registi[film['Director']] = 1
        # conteggio attori
        cast = film['Actors'].split(", ")
        for actor in cast:
            if actor != 'N/A':
                if actor in attori:
                    attori[actor] += 1
                else:
                    attori[actor] = 1


    # durata
    durata = int(durata/60*100)/100
    txtbox_statistiche.insert(tk.END,"Tempo totale a guardare film: ", "labeltag")
    txtbox_statistiche.insert(tk.END, str(durata)+" ore\n\n", "texttag")

    if len(generi) > 2:
        # genere più visto
        primoGenere = max(generi.items(), key=operator.itemgetter(1))[0]
        film_primoGenere = generi[primoGenere]
        generi.pop(primoGenere)

        secondoGenere = max(generi.items(), key=operator.itemgetter(1))[0]
        film_secondoGenere = generi[secondoGenere]
        generi.pop(secondoGenere)

        terzoGenere = max(generi.items(), key=operator.itemgetter(1))[0]
        film_terzoGenere = generi[terzoGenere]
        generi.pop(terzoGenere)

        txtbox_statistiche.insert(tk.END, "\n GENERI PREFERITI \n", "labeltag")
        txtbox_statistiche.insert(tk.END, primoGenere + ": ", "texttagB") 
        txtbox_statistiche.insert(tk.END, str(film_primoGenere) +" film\n", "texttag")
        txtbox_statistiche.insert(tk.END, secondoGenere + ": ", "texttagB")
        txtbox_statistiche.insert(tk.END, str(film_secondoGenere) +" film\n", "texttag")
        txtbox_statistiche.insert(tk.END, terzoGenere + ": ", "texttagB")
        txtbox_statistiche.insert(tk.END, str(film_terzoGenere) +" film\n", "texttag")

    if len(registi) > 2:
        # regista più seguito
        primoRegista = max(registi.items(), key=operator.itemgetter(1))[0]
        film_primoRegista = registi[primoRegista]
        registi.pop(primoRegista)

        secondoRegista = max(registi.items(), key=operator.itemgetter(1))[0]
        film_secondoRegista = registi[secondoRegista]
        registi.pop(secondoRegista)

        terzoRegista = max(registi.items(), key=operator.itemgetter(1))[0]
        film_terzoRegista = registi[terzoRegista]
        registi.pop(terzoRegista)

        txtbox_statistiche.insert(tk.END, "\n REGISTI PREFERITI \n", "labeltag")
        txtbox_statistiche.insert(tk.END, primoRegista + ": ", "texttagB")
        txtbox_statistiche.insert(tk.END, str(film_primoRegista) +" film\n", "texttag")
        txtbox_statistiche.insert(tk.END, secondoRegista + ": ", "texttagB")
        txtbox_statistiche.insert(tk.END, str(film_secondoRegista) +" film\n", "texttag")
        txtbox_statistiche.insert(tk.END, terzoRegista + ": ", "texttagB")
        txtbox_statistiche.insert(tk.END, str(film_terzoRegista) +" film\n", "texttag")

    if len(attori) > 2:
        # attori più seguiti
        primoAttore = max(attori.items(), key=operator.itemgetter(1))[0]
        film_primoAttore = attori[primoAttore]
        attori.pop(primoAttore)

        secondoAttore = max(attori.items(), key=operator.itemgetter(1))[0]
        film_secondoAttore = attori[secondoAttore]
        attori.pop(secondoAttore)

        terzoAttore = max(attori.items(), key=operator.itemgetter(1))[0]
        film_terzoAttore = attori[terzoAttore]
        attori.pop(terzoAttore)

        txtbox_statistiche.insert(tk.END, "\n ATTORI PREFERITI \n", "labeltag")
        txtbox_statistiche.insert(tk.END, primoAttore + ": ", "texttagB")
        txtbox_statistiche.insert(tk.END, str(film_primoAttore) +" film\n", "texttag")
        txtbox_statistiche.insert(tk.END, secondoAttore + ": ", "texttagB")
        txtbox_statistiche.insert(tk.END, str(film_secondoAttore) +" film\n", "texttag")
        txtbox_statistiche.insert(tk.END, terzoAttore + ": ", "texttagB")
        txtbox_statistiche.insert(tk.END, str(film_terzoAttore) +" film\n", "texttag")

    # riblocco la scrivibilità del textbox
    txtbox_statistiche.configure(state='disabled')


###################################################################################################################

### funzione corrispondente searchUserbtn (ricerca un utente da seguire o meno) 

def cercaUtente(user):
    global database
    global utente

    txtbox_output.configure(state='normal')
    txtbox_output.insert(tk.END, "ricerca utente in corso...")
    txtbox_output.delete("1.0","end")

    fileTesto = open(database+'/users.txt','r')
    flag = 0
    for riga in fileTesto:
        if riga.strip().split(",")[1]  == user:
            flag = 1
            break
    if utente == user:
        txtbox_output.insert(tk.END,""+user)
        seguiUtentebtn.configure(state='disabled')
    elif flag == 1 and utente!=user:
        txtbox_output.insert(tk.END,""+user)
        seguiUtentebtn.configure(state='normal')
        eliminaAmicobtn.configure(state='normal')
    else:
        txtbox_output.insert(tk.END,"L'utente " + user + " non è registrato!")
    
    txtbox_output.configure(state='disabled')

###################################################################################################################

### funzione corrispondente seguiUtentebtn (segui un nuovo utente) 

def followUser(user):
    global database
    global utente
    global seguiUtente
    
    fileTesto = open(database+'/amicidi' + utente + '.txt','r')
    flag = 0
    for riga in fileTesto:
        if riga.strip() == user:
            flag = 1
            break   
    if flag == 0:
        txtbox_output.configure(state='normal')
        txtbox_output.delete("1.0","end")
        fileTesto = open(database + '/amicidi' + utente + '.txt','a')
        fileTesto.write("" + user + "\n")
        txtbox_output.insert(tk.END,"Alla grande! Ora " + user + " è un tuo amico!")
        eliminaAmicobtn.configure(state='normal')
    elif flag == 1:
        txtbox_output.configure(state='normal')
        txtbox_output.delete("1.0","end")
        txtbox_output.insert(tk.END,"Ops, sei già amico di " + user + "!")
        eliminaAmicobtn.configure(state='normal')
    
    visualizzaListaAmici()
    txtbox_output.configure(state='disabled')


###################################################################################################################

### funzione corrispondente eliminaAmicobtn (non seguire più un utente) 

def defollowUser(user):
    global database
    global utente
    with open(database + '/amicidi' + utente + '.txt','r') as f:
        lines = f.readlines()
    with open(database + '/amicidi' + utente + '.txt','w') as f:
        for line in lines:
            if line.strip("\n") != user:
                f.write(line)
    txtbox_output.configure(state='normal')
    txtbox_output.delete("1.0","end")
    txtbox_output.insert(tk.END,"Non sei più amico di " + user)
    txtbox_output.configure(state='disabled')
    eliminaAmicobtn.configure(state='disabled')


###################################################################################################################

### funzione corrispondente alla lista amici 

def visualizzaListaAmici():
    global database
    global utente
    global txtbox_mieiAmici
    global txtbox_numeroAmici

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

    # segna quanti ne segui
    txtbox_numeroAmici.configure(state='normal')
    txtbox_numeroAmici.insert(tk.END, "aggiorno...")
    txtbox_numeroAmici.delete("1.0","end")
    txtbox_numeroAmici.tag_config("followtag", font = 'Italic 12 bold', foreground='navy')
    txtbox_numeroAmici.insert(tk.END, "Segui: ", "followtag")
    txtbox_numeroAmici.insert(tk.END,str(count-1)+" "*5)
    

    #segna quanti ti seguono
    numeroAmici = 0
    fileUtenti = open(''+database+'/users.txt','r')
    for user in fileUtenti:
        if utente != user.strip().split(",")[1]:
            fileUtenti2 = open(''+database+'/amicidi'+user.strip().split(",")[1] +'.txt','r')
            for amici in fileUtenti2:
                if amici.strip() == utente:
                    numeroAmici += 1
    txtbox_numeroAmici.insert(tk.END, "Followers: ", "followtag")
    txtbox_numeroAmici.insert(tk.END,str(numeroAmici))
    txtbox_numeroAmici.configure(state='disabled')

    visualizzaFilmAmico.configure(state='normal')
    entry_codice_amico.configure(state='normal')

###################################################################################################################

### funzione per visualizzare i film di un tuo amico 

def visualizzaFilm(codice):

    global database
    global utente
    global apikey

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
        idFilm = film.split(",")[0]
        lista.append(idFilm)
    lista.reverse()
    if len(lista) > 1:
        txtbox_filmAmici.tag_config("listaAmicoTag", font='Italic 12 bold', foreground='navy')
        txtbox_filmAmici.insert(tk.END, "Film di "+amico+"\n", "listaAmicoTag")

    for film in lista:
        url = "http://www.omdbapi.com/?i="+film+"&apikey="+apikey
        response = requests.request("GET", url)
        data = json.loads(response.text)
        testo = str(contatore)+" - "+ data['Title'] + "\n"
        txtbox_filmAmici.insert(tk.END, testo)
        contatore += 1
    
    txtbox_filmAmici.configure(state='disable')

###################################################################################################################

### funzione corrispondente pubblicabtn (pubblica un commento) 
def verificaVolgarita(commento):
    import pickle
    # Pre processing del testo (stemmer Snowball, stop words in italiano...)
    import re 
    import nltk 
    nltk.download('stopwords') 
    from nltk.corpus import stopwords 
    from nltk.stem import SnowballStemmer 
    stemmer_ita = SnowballStemmer('italian')
    review_2 = re.sub('[^a-zA-Z]', ' ', commento)
    review_2 = review_2.lower() 
    review_2 = review_2.split()  
    review_2 = [stemmer_ita.stem(word) for word in review_2
                if not word in set(stopwords.words('italian'))] 
    review_2 = ' '.join(review_2) 

    # Importo il modello allenato
    modelloFrasiVolgari = pickle.load(open(database + "/modelloFrasiVolgari.pickle","rb"))
    # Importo lista attributi per adattare la nuova entry al modello
    features = open (database + "/featureModelloFrasiVolgari.txt","r")
    x_test = []
    for i in features:
        if i.strip() in review_2:
            x_test.append(1)
        else:
            x_test.append(0)
    X_test = [x_test]

    # Faccio la predizione sulla volgarità
    y_pred = modelloFrasiVolgari.predict(X_test)
    return y_pred

def pubblicazionePossibileFraseVolgare(nuovoCommento):
    global utente
    global database
    global popup
    fin = open(database + '/bacheca.txt','a')
    line = utente + "|" + nuovoCommento +"\n" 
    fin.write(line)
    fin.close()
    possibiliPostVolgari = open(database + "/possibiliPostVolgari.txt","a")
    line = utente + "|" + nuovoCommento +"\n"
    possibiliPostVolgari.write(line)
    possibiliPostVolgari.close()
    popup.destroy()

def pubblica(nuovoCommento):
    global utente
    global database
    global popup

    # Funzione per verificare che la frase non abbia contenuti offensivi
    predizioneFrase = verificaVolgarita(nuovoCommento)

    if predizioneFrase[0] == "pulita":
        fin = open(database + '/bacheca.txt','a')
        line = utente + "|" + nuovoCommento +"\n" 
        fin.write(line)
        fin.close()
    else:
        popup = tk.Toplevel()
        popup.wm_title("Window")
        warning = tk.Label(popup, text="Il tuo commento potrebbe essere volgare, sei sicuro di volerlo pubblicare?")
        warning.grid(row=0, column=0)
        annullaCommento = ttk.Button(popup, text="NO",command=popup.destroy)
        annullaCommento.grid(row=1, column=0)
        confermaCommento = ttk.Button(popup, text="SI",command=lambda:pubblicazionePossibileFraseVolgare(nuovoCommento))
        confermaCommento.grid(row=1, column=1)

###################################################################################################################

### funzione corrispondente aggiornabtn (aggiorna la bacheca) 
  
def aggiorna():
    global utente
    global database

    f = open(database + '/bacheca.txt','r')
    lista = []
    for line in f:
        lista.append(line)
    lista.reverse()
    f.close()

    txtbox_bacheca.configure(state='normal')
    txtbox_bacheca.insert(tk.END, "aggiorno...")
    txtbox_bacheca.delete("1.0","end")
    for post in lista:
        user = post.split("|")[0]
        commento = post.split("|")[1]
        txtbox_bacheca.tag_config("usertag", font='Italic 10 bold', foreground='navy')  # Set font, size and style
        txtbox_bacheca.tag_config("posttag", font='Italic 12')
        txtbox_bacheca.insert(tk.END, user+"\n", "usertag")
        txtbox_bacheca.insert(tk.END, commento + "\n\n", "posttag")
    

    txtbox_bacheca.configure(state='disabled')

###################################################################################################################

def segnala(commentoSegnalato):
    frasiSegnalate = open(database + "/frasiSegnalate.txt","a")
    frasiSegnalate.write(commentoSegnalato+"\n")
    frasiSegnalate.close()
    finestraRingraziamento = tk.Toplevel()
    finestraRingraziamento.wm_title("Window")
    ringraziamento = tk.Label(finestraRingraziamento, text="Grazie per la tua segnalazione!")
    ringraziamento.grid(row=0, column=0)
    bottoneUscita = tk.Button(finestraRingraziamento, text="OK", command=finestraRingraziamento.destroy,width=10)
    bottoneUscita.grid(row=1,column=0)

###################################################################################################################

### funzione corrispondente suggeriscibtn (aggiorna i film suggeriti) 
def aggiornaSuggerimenti():
    global utente
    global database
    global apikey

    # refresh textbox
    txtbox_suggeriti.configure(state='normal')
    txtbox_suggeriti.insert(tk.END, "...")
    txtbox_suggeriti.delete("1.0","end")
    txtbox_suggeriti.configure(state='disabled')

    # creazione automatica del dataset
    file_utenti = open(database + "/users.txt", 'r')
    dataset = []
    for dati_utente in file_utenti:
        id_utente = dati_utente.split(",")[0]
        nome_utente = dati_utente.strip().split(",")[1]
        if nome_utente == utente:
            id_utente_loggato = id_utente
        file_film = open(database + "/elencoFilmdi" + nome_utente + ".txt", 'r')
        for dati_film in file_film:
            id_film = dati_film.split(",")[0]
            voto_film = dati_film.strip().split(",")[1]
            nuova_istanza = [id_utente, id_film, int(voto_film)]
            dataset.append(nuova_istanza)
        file_film.close()
    file_utenti.close()

    df = pd.DataFrame(dataset, columns=['User', 'Item', 'Rating'])
    df.dropna(inplace=True)

    # Creazione matrice USER-ITEM
    matriceUI = df.pivot_table(index=['User'], columns=['Item'], values='Rating').fillna(0)
    item_list = list(matriceUI.columns)
    # converto la pivot table in matrice sparsa
    matriceUI = sparse.lil_matrix(matriceUI)

    # Creazione matrice ITEM-ITEM similarity
    m_m_similarity = cosine_similarity(matriceUI.T, dense_output = False)

    # inizializzo alcune variabili che mi servono
    userID = int(id_utente_loggato) - 1001
    user_rating_list = []
    not_rated = []
    numero_totale_film = m_m_similarity.shape[0]
    for i in range(numero_totale_film):
        user_rating_list.append(matriceUI[userID, i])
        if matriceUI[userID, i] == 0.0:
            not_rated.append(i)

    # faccio la predizione dei ratings  
    suggested = []
    rating_pred = []
    for col in range(numero_totale_film):
        if matriceUI[userID, col] == 0:
            # aggiungo l'item alla lista suggeriti
            suggested.append(item_list[col])

            # predico che voto l'user darebbe all'item
            item_similarity_list = []
            denominatore = 0
            for i in range(numero_totale_film):
                item_similarity_list.append(m_m_similarity[col, i])
                if i not in not_rated:
                    denominatore += m_m_similarity[col, i]
            numeratore = np.dot(np.array(item_similarity_list), np.array(user_rating_list))
            if denominatore != 0:
                rating_pred.append(int(numeratore/denominatore))
            else:
                rating_pred.append('NaN')

    film_da_suggerire = sorted(zip(rating_pred, suggested), reverse=True)[:3]
   
    # mandare a video le locandine dei film suggeriti
    txtbox_suggeriti.configure(state='normal')
    for i in range(len(film_da_suggerire)):
        try:
            url = "http://www.omdbapi.com/?i="+film_da_suggerire[i][1]+"&apikey="+apikey
            response = requests.request("GET", url)
            data = json.loads(response.text)
            #testo = str(count)+" - "+ data['Title'].upper() + "\n"
            #txtbox_mieiFilm.insert(tk.END, testo)
            url_immagine = ""+ data ['Poster'] + ""
            response = requests.get(url_immagine)
            img_data = response.content
            img = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data))) 
            immagine = tk.Label(image=img)
            immagine.image = img
            txtbox_suggeriti.image_create(tk.END, image=img)
            txtbox_suggeriti.insert(tk.END, "    ")
            #immagine.place(x=500, y=count*100)
        except:
            url = "http://www.omdbapi.com/?i="+film+"&apikey="+apikey
            response = requests.request("GET", url)
            data = json.loads(response.text)
            testo = str(count)+" - "+ data['Title'].upper() + "\n"
            txtbox_suggeriti.insert(tk.END, testo)

    txtbox_suggeriti.configure(state='disabled')

###################################################################################################################
###################################################################################################################
###################################################################################################################

# REALIZZAZIONE DELLA GUI
global txtbox_possibiliFilm
global txtbox_schedaTec
global txtbox_mieiFilm
global txtbox_mieiAmici
global txtbox_numeroAmici
global database
global utente
global apikey


apikey = "insert valid api"

# finestra base
root = tk.Tk()

maincolor = 'red3' #'#ffffcc'
secondcolor = 'gold'
style = ttk.Style()
 
style.theme_create('cinema', settings={
    ".": {
        "configure": {
            "background": maincolor, # All except tabs
            "font": 'red'
        }
    },
    "TNotebook": {
        "configure": {
            "background":maincolor, # Your margin color
            "tabmargins": [2, 5, 0, 0], # margins: left, top, right, separator
        }
    },
    "TNotebook.Tab": {
        "configure": {
            "background": maincolor, # tab color when not selected
            "padding": [10, 2], # [space between text and horizontal tab-button border, space between text and vertical tab_button border]
            "font":"white"
        },
        "map": {
            "background": [("selected", secondcolor)], # Tab color when selected
            "expand": [("selected", [1, 1, 1, 0])] # text margins
        }
    }
})
 
style.theme_use('cinema')

# tabs di primo livello
tabControl = ttk.Notebook(root)
tabAccedi = ttk.Frame(tabControl, )
tabCerca = ttk.Frame(tabControl)
tabMyMovies = ttk.Frame(tabControl)
tabStatistiche = ttk.Frame(tabControl)
tabAmici = ttk.Frame(tabControl)
tabHome = ttk.Frame(tabControl)
tabSuggeriti = ttk.Frame(tabControl)

tabControl.add(tabAccedi, text ='Accedi')
tabControl.add(tabCerca, text ='Cerca')
tabControl.add(tabMyMovies, text ='Miei Film')
tabControl.add(tabStatistiche, text ='Statistiche')
tabControl.add(tabAmici, text = 'Amici')
tabControl.add(tabHome, text = 'Home')
tabControl.add(tabSuggeriti, text = 'Film Suggeriti')
tabControl.pack(expand = 1, fill ="both")



## label work in progress
canvas_wip2 = tk.Canvas(tabSuggeriti, width = 400, height = 20)
canvas_wip2.grid(column=0, row=4)
label_wip2= tk.Label(tabSuggeriti, text= "work in progress")
canvas_wip2.create_window(400, 30, window=label_wip2)


###################################################################################################################

### TAB LOG ###

# tabs di secondo livello
tabAccediControl = ttk.Notebook(tabAccedi)
tabLogin = ttk.Frame(tabAccediControl)
tabRegistra = ttk.Frame(tabAccediControl)


tabAccediControl.add(tabLogin, text ='Login')
tabAccediControl.add(tabRegistra, text ='Registrati')
tabAccediControl.pack(expand = 1, fill ="both")


### TAB REGISTRATI ###

# campo di inserimento nuovo username
canvas_newUser = tk.Canvas(tabRegistra, width = 400, height = 20, background=maincolor)
canvas_newUser.grid(column=0, row=1)
entry_newUser = tk.Entry (tabRegistra) 
canvas_newUser.create_window(200, 10, window=entry_newUser)

# label nuovo username
label_newUser = tk.Label(tabRegistra, text= "Nuovo Username", background=maincolor)
canvas_newUser.create_window(50, 10, window=label_newUser)

# campo di inserimento path della cartella sincronizzata con google drive
canvas_newDB = tk.Canvas(tabRegistra, width = 400, height = 20, background=maincolor)
canvas_newDB.grid(column=0, row=2)
entry_newDB = tk.Entry (tabRegistra) 
canvas_newDB.create_window(200, 10, window=entry_newDB)

# label database
label_newDB = tk.Label(tabRegistra, text= "Path Database", background=maincolor)
canvas_newDB.create_window(50, 10, window=label_newDB)

# textbox per messaggio di output
txtbox_outputregistrazione = tk.Text(tabRegistra, height=5, width=100, background=secondcolor)
txtbox_outputregistrazione.configure(state='disabled')
txtbox_outputregistrazione.grid(column=0, row=4)

# bottone per effettuare la registrazione
registerbtn = tk.Button(tabRegistra, text="Registrati", command=lambda: register(entry_newUser.get(), entry_newDB.get()), width=20, background="gold")
registerbtn.grid(column=0, row=3)


### TAB LOGIN ###

# campo di inserimento nuovo username
canvas_User = tk.Canvas(tabLogin, width = 400, height = 20,background=maincolor)
canvas_User.grid(column=0, row=1)
entry_User = tk.Entry (tabLogin) 
canvas_User.create_window(200, 10, window=entry_User)

# label nuovo username
label_User = tk.Label(tabLogin, text= "Username", background=maincolor)
canvas_User.create_window(50, 10, window=label_User)

# campo di inserimento path della cartella sincronizzata con google drive
canvas_DB = tk.Canvas(tabLogin, width = 400, height = 20, background=maincolor)
canvas_DB.grid(column=0, row=2)
entry_DB = tk.Entry (tabLogin) 
canvas_DB.create_window(200, 10, window=entry_DB)

# label database
label_DB = tk.Label(tabLogin, text= "Path Database", background=maincolor)
canvas_DB.create_window(50, 10, window=label_DB)

# textbox per messaggio di output
txtbox_outputlogin = tk.Text(tabLogin, height=5, width=100, background=secondcolor)
txtbox_outputlogin.configure(state='disabled')
txtbox_outputlogin.grid(column=0, row=4)

# bottone per effettuare il login
loginbtn = tk.Button(tabLogin, text="Login", command=lambda: login(entry_User.get(), entry_DB.get()), width=20, background="gold")
loginbtn.grid(column=0, row=3)

# bottone per effettuare il logout
logoutbtn = tk.Button(tabLogin, text="Logout", command=lambda: logout(), width=20, background="gold")
logoutbtn.grid(column=0, row=5)
logoutbtn.configure(state='disabled')

###################################################################################################################

### TAB CERCA ###

# campo di inserimento titolo del film
canvas_newMovie = tk.Canvas(tabCerca, width = 400, height = 20, background=maincolor)
canvas_newMovie.grid(column=0, row=0)
entry_newMovie = tk.Entry(tabCerca) 
canvas_newMovie.create_window(200, 10, window=entry_newMovie, width=200)
entry_newMovie.configure(state='disabled')

## label nuovo film
label_newMovie = tk.Label(tabCerca, text= "Titolo film", background=maincolor)
canvas_newMovie.create_window(50, 10, window=label_newMovie)

# textbox per tutti i film 
txtbox_possibiliFilm = tk.Text(tabCerca, height=10, width=100, background=secondcolor)
txtbox_possibiliFilm.configure(state='disabled')
txtbox_possibiliFilm.grid(column=0, row=2)

# campo inserimento codice
canvas_codice = tk.Canvas(tabCerca, width = 400, height = 20, background=maincolor)
canvas_codice.grid(column=0, row=3)
entry_codice = tk.Entry(tabCerca) 
canvas_codice.create_window(70, 10, window=entry_codice, width=50)
entry_codice.configure(state='disabled')

## label inserimento codice
label_codice= tk.Label(tabCerca, text= "Codice", background=maincolor)
canvas_codice.create_window(0, 10, window=label_codice)

# textbox per scheda tecnica
txtbox_schedaTec = tk.Text(tabCerca, height=10, width=100, background=secondcolor)
txtbox_schedaTec.configure(state='disabled')
txtbox_schedaTec.grid(column=0, row=4)

# bottone per effettuare la ricerca di un nuovo film
searchFilmbtn = tk.Button(tabCerca, text="Cerca nuovo film", command=lambda: stampaPossibiliFilm(entry_newMovie.get()), width=20, background="gold")
searchFilmbtn.grid(column=0, row=1)
searchFilmbtn.configure(state='disabled')

# bottone per effettuare aggiungere il nuovo film alla lista
addFilmbtn = tk.Button(tabCerca, text="Aggiungi a lista", command=lambda: aggiungiFilm(entry_codice.get()), width=20, background="gold")
addFilmbtn.grid(column=0, row=3)
canvas_codice.create_window(200, 10, window=addFilmbtn)
addFilmbtn.configure(state='disabled')

# bottone per visualizzare la scheda tecnica del film
schedaTecnicabtn = tk.Button(tabCerca, text="Scheda tecnica", command=lambda: mostraSchedaTecnica(entry_codice.get()), width=20, background="gold")
schedaTecnicabtn.grid(column=0, row=3)
canvas_codice.create_window(400, 10, window=schedaTecnicabtn)
schedaTecnicabtn.configure(state='disabled')


###################################################################################################################

### TAB MIEI FILM ###

# textbox con tutti i film visti dall'utente (si parte dall'ultimo e si va a ritroso)
txtbox_mieiFilm = tk.Text(tabMyMovies, height=50, width=100, background="red4")
txtbox_mieiFilm.configure(state='disabled')
txtbox_mieiFilm.grid(column=0, row=2)


###################################################################################################################

### TAB STATISTICHE ###

# textbox con le statistiche dei film visti dall'utente (si parte dall'ultimo e si va a ritroso)
txtbox_statistiche = tk.Text(tabStatistiche, height=100, width=100, background=secondcolor)
txtbox_statistiche.configure(state='disabled')
txtbox_statistiche.grid(column=0, row=2)

###################################################################################################################

### TAB AMICI ###

# tabs di secondo livello
tabAmiciControl = ttk.Notebook(tabAmici)
tabMieiAmici = ttk.Frame(tabAmiciControl)
tabCercaAmici = ttk.Frame(tabAmiciControl)
tabAmiciSuggeriti = ttk.Frame(tabAmiciControl)


tabAmiciControl.add(tabMieiAmici, text ='Miei Amici')
tabAmiciControl.add(tabCercaAmici, text ='Cerca Amici')
tabAmiciControl.add(tabAmiciSuggeriti, text ='Amici Suggeriti')
tabAmiciControl.pack(expand = 1, fill ="both")

## label work in progress
canvas_wip = tk.Canvas(tabAmiciSuggeriti, width = 400, height = 20, background=maincolor)
canvas_wip.grid(column=0, row=4)
label_wip= tk.Label(tabAmiciSuggeriti, text= "work in progress")
canvas_wip.create_window(400, 30, window=label_wip)

# textbox per visualizzare numero amici 
txtbox_numeroAmici = tk.Text(tabMieiAmici, height=2, width=100, background=secondcolor)
txtbox_numeroAmici.configure(state='disabled')
txtbox_numeroAmici.grid(column=0, row=1)

# textbox per tutti gli amici 
txtbox_mieiAmici = tk.Text(tabMieiAmici, height=10, width=100, background=secondcolor)
txtbox_mieiAmici.configure(state='disabled')
txtbox_mieiAmici.grid(column=0, row=4)

# campo inserimento codice
canvas_codice = tk.Canvas(tabMieiAmici, width = 400, height = 20, background=maincolor)
canvas_codice.grid(column=0, row=5)
entry_codice_amico = tk.Entry(tabMieiAmici) 
canvas_codice.create_window(70, 10, window=entry_codice_amico, width=50)
entry_codice_amico.configure(state='disabled')

## label inserimento codice
label_codiceamico= tk.Label(tabMieiAmici, text= "Codice",background=maincolor)
canvas_codice.create_window(0, 10, window=label_codiceamico)

# bottone per aggiornare il campo amici di un utente
visualizzaAmici = tk.Button(tabMieiAmici, text="Aggiorna", command=lambda: visualizzaListaAmici(), width=20, background="gold")
visualizzaAmici.grid(column=0, row=0)
visualizzaAmici.configure(state='disabled')

# bottone per visualizzare i film dell'amico seguito
visualizzaFilmAmico = tk.Button(tabMieiAmici, text="Vedi i film del tuo amico", command=lambda: visualizzaFilm(entry_codice_amico.get()), width=20, background="gold")
visualizzaFilmAmico.grid(column=0, row=4)
canvas_codice.create_window(200, 10, window=visualizzaFilmAmico)
visualizzaFilmAmico.configure(state='disabled')

# textbox per visualizzare i film degli amici 
txtbox_filmAmici = tk.Text(tabMieiAmici, height=100, width=100, background=secondcolor)
txtbox_filmAmici.configure(state='disabled')
txtbox_filmAmici.grid(column=0, row=6)

# campo di inserimento ricerca utente
canvas_ricercaUtente = tk.Canvas(tabCercaAmici, width = 400, height = 20, background=maincolor)
canvas_ricercaUtente.grid(column=0, row=0) 
entry_ricercaUtente = tk.Entry (tabCercaAmici)
canvas_ricercaUtente.create_window(200, 10, window=entry_ricercaUtente, width=200)
entry_ricercaUtente.configure(state='disabled')

## label ricerca utente
label_ricercaUtente = tk.Label(text= "Cerca utente", background=maincolor)
canvas_ricercaUtente.create_window(50, 10, window=label_ricercaUtente)

# bottone per effettuare la ricerca di un utente
searchUserbtn = tk.Button(tabCercaAmici, text="Cerca", command=lambda: cercaUtente(entry_ricercaUtente.get()), width=20, background="gold")
searchUserbtn.grid(column=0, row=1)
searchUserbtn.configure(state='disabled')

# textbox per l'utente cercato
txtbox_output = tk.Text(tabCercaAmici, height=2, width=100, background=secondcolor)
txtbox_output.configure(state='disabled')
txtbox_output.grid(column=0, row=2)

# bottone per "seguire" l'utente cercato
seguiUtentebtn = tk.Button(tabCercaAmici, text="Segui!", command=lambda: followUser(entry_ricercaUtente.get()), width=20, background="gold")
seguiUtentebtn.grid(column=0, row=3)
seguiUtentebtn.configure(state='disabled')

# bottone per "defolloware" l'utente cercato
eliminaAmicobtn = tk.Button(tabCercaAmici, text="Non seguire più", command=lambda: defollowUser(entry_ricercaUtente.get()), width=20, background="gold")
eliminaAmicobtn.grid(column=0, row=4)
eliminaAmicobtn.configure(state='disabled')


###################################################################################################################

### TAB HOME ###


# campo di inserimento nuovo commento
canvas_nuovoCommento = tk.Canvas(tabHome, width = 400, height = 40, background=maincolor)
canvas_nuovoCommento.grid(column=0, row=1) 
entry_nuovoCommento = tk.Entry (tabHome)
canvas_nuovoCommento.create_window(200, 25, window=entry_nuovoCommento, width=800, height=40)
entry_nuovoCommento.configure(state='disabled')

# textbox per bacheca
txtbox_bacheca = tk.Text(tabHome, height=50, width=100, background=secondcolor)
txtbox_bacheca.configure(state='disabled')
txtbox_bacheca.grid(column=0, row=6)

# bottone per pubblicare
pubblicabtn = tk.Button(tabHome, text="Pubblica", command=lambda: pubblica(entry_nuovoCommento.get()), width=20, background="gold")
pubblicabtn.grid(column=0, row=3)
pubblicabtn.configure(state='disabled')

# bottone per aggiornare la home
aggiornabtn = tk.Button(tabHome, text="Aggiorna", command=lambda: aggiorna(), width=20, background="gold")
aggiornabtn.grid(column=0, row=4)
aggiornabtn.configure(state='disabled')

# bottone per segnalare un commento
segnalabtn = tk.Button(tabHome, text="Segnala", command=lambda: segnala(entry_nuovoCommento.get()), width=20, background="gold")
segnalabtn.grid(column=0, row=5)
segnalabtn.configure(state='disabled')


###################################################################################################################

### TAB FILM SUGGERITI ###

# textbox per i film suggeriti
txtbox_suggeriti = tk.Text(tabSuggeriti, height=50, width=100, background="red4")
txtbox_suggeriti.configure(state='disabled')
txtbox_suggeriti.grid(column=0, row=1)


# bottone per aggiornare i suggerimenti
suggeriscibtn = tk.Button(tabSuggeriti, text="Aggiorna", command=lambda: aggiornaSuggerimenti(), width=20, background="gold")
suggeriscibtn.grid(column=0, row=0)
suggeriscibtn.configure(state='disabled')


###################################################################################################################

# lancia finestra
root.mainloop()