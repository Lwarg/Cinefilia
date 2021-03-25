import tkinter as tk



# funzione corrispondente al bottone registerbtn (per registrare un nuovo utente)
def register(user, DBpath):
    # l'username viene appeso nel file users.txt che si trova nella cartella sincronizzata con google drive
    flag = 0
    fileTestoLettura = open(''+ DBpath +'/users.txt','r')
    fileTestoScrittura = open(''+ DBpath +'/users.txt','a')
    for riga in fileTestoLettura:
        if riga.strip() == user:
            flag = 1
    if flag == 0:
        fileTestoScrittura.write("" + user + "\n")
        nuovoFileTesto = open('' + DBpath + '/elencoFilmdi' + user + '.txt','w')
    else:
        print("Username già presente")
        print("Inserisci nuova username")
    print(user)
    print(DBpath)



# REALIZZAZIONE DELLA GUI

# finestra
root = tk.Tk()

# campo di inserimento nuovo username
canvas_newUser = tk.Canvas(root, width = 400, height = 20)
canvas_newUser.grid(column=0, row=1)
entry_newUser = tk.Entry (root) 
canvas_newUser.create_window(200, 10, window=entry_newUser)

## label nuovo username
label_newUser = tk.Label(root, text= "Nuovo Username")
canvas_newUser.create_window(50, 10, window=label_newUser)

# campo di inserimento path della cartella sincronizzata con google drive
canvas_DB = tk.Canvas(root, width = 400, height = 20)
canvas_DB.grid(column=0, row=2)
entry_DB = tk.Entry (root) 
canvas_DB.create_window(200, 10, window=entry_DB)

## label database
label_DB = tk.Label(root, text= "Path database")
canvas_DB.create_window(50, 10, window=label_DB)

# bottone per effettuare la registrazione
registerbtn = tk.Button(root, text="register", command=lambda: register(entry_newUser.get(), entry_DB.get()), width=20)
registerbtn.grid(column=0, row=0)


# lancia finestra
root.mainloop()