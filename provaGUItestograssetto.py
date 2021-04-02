import tkinter as tk 
global database

database = 'C:/Users/splin/Google Drive (simonemailtesting1@gmail.com)/appCinefilia'

def aggiorna():
    f = open(database + '/bacheca.txt','r')
    lista = []
    for line in f:
        lista.append(line)
    lista.reverse()
    f.close()
    txtbox.insert(tk.END, "aggiorno...")
    txtbox.delete("1.0","end")
    for post in lista:
        user = post.split("|")[0]
        commento = post.split("|")[1]
        txtbox.insert(tk.END, user+"\n")
        txtbox.insert(tk.END, commento + "\n\n")
        txtbox.tag_config(user, font='Helvetica 12 bold', foreground='blue')  # Set font, size and style


# finestra base
root = tk.Tk()

# button
btn = tk.Button(root, text="aggiorna", command=lambda: aggiorna(), width=20)
btn.grid(column=0, row=0)

# textbox
txtbox = tk.Text(root, height=50, width=100)
txtbox.grid(column=0, row=4)



root.mainloop()