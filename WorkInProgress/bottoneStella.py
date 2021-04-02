import tkinter as tk
from tkinter import ttk
from tkinter import Canvas


#Funzione per salvare il voto
def salvaVoto1():
    #global voto
    global win
    global win_due
    #voto = 1
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
    global voto
    global win
    voto = 2
    win.destroy()
def salvaVoto3():
    global voto
    global win
    voto = 3
    win.destroy()
def salvaVoto4():
    global voto
    global win
    voto = 4
    win.destroy()
def salvaVoto5():
    global voto
    global win
    voto = 5
    win.destroy()
def salvaVoto6():
    global voto
    global win
    voto = 6
    win.destroy()
def salvaVoto7():
    global voto
    global win
    voto = 7
    win.destroy()
def salvaVoto8():
    global voto
    global win
    voto = 8
    win.destroy()
def salvaVoto9():
    global voto
    global win
    voto = 9
    win.destroy()
def salvaVoto10():
    global voto
    global win
    voto = 10
    win.destroy()
def salvaSkip():
    global voto
    global win
    voto = 11
    win.destroy()

#Funzione per aprire il pop-up
def popup():
    global voto
    global win
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


# finestra
root = tk.Tk()

# bottone per aggiungere il nuovo film alla lista
addFilmbtn = tk.Button(root, text="Aggiungi a lista", command=lambda: popup(), width=20)
addFilmbtn.grid(column=0, row=3)

# lancia finestra
root.mainloop()

