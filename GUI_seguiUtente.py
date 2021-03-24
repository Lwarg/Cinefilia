import tkinter as tk

def cercaUtente(user):

    txtbox_output.configure(state='normal')
    txtbox_output.insert(tk.END, "ricerca utente in corso...")
    txtbox_output.delete("1.0","end")

    fileTesto = open('C:/Users/simac/Google Drive/appCinefilia/users.txt','r')
    flag = 0
    for riga in fileTesto:
        if riga.strip() == user:
            flag = 1
            break
    if flag == 1:
        txtbox_output.insert(tk.END,""+user)
        seguiUtente.configure(state='normal')
    else:
        txtbox_output.insert(tk.END,"L'utente " + user + " non è registrato!")
    
    txtbox_output.configure(state='disabled')


def followUser(user):
    
    global utente
    global seguiUtente
    
    fileTesto = open('C:/Users/simac/Google Drive/appCinefilia/amicidi' + utente + '.txt','r')
    flag = 0
    for riga in fileTesto:
        if riga.strip() == user:
            flag = 1
            break
    if user == utente:
        flag = 2
    if flag == 0:
        txtbox_output.configure(state='normal')
        txtbox_output.delete("1.0","end")
        fileTesto = open('C:/Users/simac/Google Drive/appCinefilia/amicidi' + utente + '.txt','a')
        fileTesto.write("" + user + "\n")
        txtbox_output.insert(tk.END,"Alla grande! Ora " + user + " è un tuo amico!")
        eliminaAmico.configure(state='normal')
    elif flag == 1:
        txtbox_output.configure(state='normal')
        txtbox_output.delete("1.0","end")
        txtbox_output.insert(tk.END,"Ops, sei già amico di " + user + "!")
        eliminaAmico.configure(state='normal')
    elif flag == 2:
        seguiUtente.configure(state='disabled')

# def defollowUser(user):
#     global utente
#     with open('C:/Users/simac/Google Drive/appCinefilia/amicidi' + utente + '.txt','r') as f:
#         lines = f.readlines()
#     with open('C:/Users/simac/Google Drive/appCinefilia/amicidi' + utente + '.txt','w') as f:
#     for line in lines:
#         if line.strip("\n") != user:
#             f.write(line)




###################################################################################################

global utente
global apikey

utente = "Simone"

# finestra base
tabAmici = tk.Tk()

# campo di inserimento ricerca utente
canvas_ricercaUtente = tk.Canvas(width = 400, height = 20)
canvas_ricercaUtente.grid(column=0, row=0) 
entry_ricercaUtente = tk.Entry (tabAmici)
canvas_ricercaUtente.create_window(200, 10, window=entry_ricercaUtente, width=200)

## label ricerca utente
label_ricercaUtente = tk.Label(text= "Cerca utente")
canvas_ricercaUtente.create_window(50, 10, window=label_ricercaUtente)

# bottone per effettuare la ricerca di un utente
searchUser = tk.Button(tabAmici, text="Cerca", command=lambda: cercaUtente(entry_ricercaUtente.get()), width=20)
searchUser.grid(column=0, row=1)

# textbox per l'utente cercato
txtbox_output = tk.Text(tabAmici, height=10, width=100)
txtbox_output.configure(state='disabled')
txtbox_output.grid(column=0, row=2)

# bottone per "seguire" l'utente cercato
seguiUtente = tk.Button(tabAmici, text="Segui!", command=lambda: followUser(entry_ricercaUtente.get()), width=20)
seguiUtente.grid(column=0, row=3)
seguiUtente.configure(state='disabled')

# bottone per "defolloware" l'utente cercato
eliminaAmico = tk.Button(tabAmici, text="Non seguire più", command=lambda: defollowUser(entry_ricercaUtente.get()), width=20)
eliminaAmico.grid(column=0, row=4)
eliminaAmico.configure(state='disabled')

# lancia finestra
tabAmici.mainloop()