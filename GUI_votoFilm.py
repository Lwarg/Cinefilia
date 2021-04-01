import tkinter as tk
from tkinter import ttk

#Funzione per salvare il voto
def salvaVoto1():
    global voto
    global win
    voto = 1
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
    win = tk.Toplevel()
    win.wm_title("Window")
    l = tk.Label(win, text="Aggiungi una valutazione al film!")
    l.grid(row=0, column=0)
    voto1 = ttk.Button(win, text="1", command=salvaVoto1)
    voto1.grid(row=1, column=1)
    voto2 = ttk.Button(win, text="2", command=salvaVoto2)
    voto2.grid(row=1, column=2)
    voto3 = ttk.Button(win, text="3", command=salvaVoto3)
    voto3.grid(row=1, column=3)
    voto4 = ttk.Button(win, text="4", command=salvaVoto4)
    voto4.grid(row=1, column=4)
    voto5 = ttk.Button(win, text="5", command=salvaVoto5)
    voto5.grid(row=1, column=5)
    voto6 = ttk.Button(win, text="6", command=salvaVoto6)
    voto6.grid(row=1, column=6)
    voto7 = ttk.Button(win, text="7", command=salvaVoto7)
    voto7.grid(row=1, column=7)
    voto8 = ttk.Button(win, text="8", command=salvaVoto8)
    voto8.grid(row=1, column=8)
    voto9 = ttk.Button(win, text="9", command=salvaVoto9)
    voto9.grid(row=1, column=9)
    voto10 = ttk.Button(win, text="10", command=salvaVoto10)
    voto10.grid(row=1, column=10)
    votoSkip = ttk.Button(win, text="Skip", command=salvaSkip)
    votoSkip.grid(row=2, column=5)


global voto
voto = 0

# finestra
root = tk.Tk()

# bottone per aggiungere il nuovo film alla lista
addFilmbtn = tk.Button(root, text="Aggiungi a lista", command=lambda: popup(), width=20)
addFilmbtn.grid(column=0, row=3)

# lancia finestra
root.mainloop()