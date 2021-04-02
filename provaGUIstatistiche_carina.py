import tkinter as tk 
import matplotlib.pyplot as plt
import pandas as pd
import io

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk



def aggiorna():
    # statistiche inventate
    statistiche = {'A':25, 'B':40, 'C':35}
    #df = pd.DataFrame(statistiche, columns=list(statistiche.keys()))
    plt.pie(list(statistiche.values()), radius = 0.5)
    plt.legend(list(statistiche.keys()), loc='center left')
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = ImageTk.PhotoImage(Image.open(buf))
    #img = ImageTk.PhotoImage(Image.open(io.BytesIO(figura))) 
    immagine = tk.Label(image=img)
    immagine.image = img
    txtbox.image_create(tk.END, image=img)


# finestra base
root = tk.Tk()

# button
btn = tk.Button(root, text="aggiorna", command=lambda: aggiorna(), width=20)
btn.grid(column=0, row=0)

# textbox
txtbox = tk.Text(root, height=50, width=100)
txtbox.grid(column=0, row=4)



root.mainloop()