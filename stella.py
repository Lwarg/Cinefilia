import tkinter as tk
from tkinter import Canvas

root = tk.Tk()

star_one_left = tk.Canvas(root,width=100,height=100)
star_one_left.grid(row=0,column=0)
star_one_right = tk.Canvas(root,width=100,height=100)
star_one_right.grid(row=0,column=1)
star_two = tk.Canvas(root,width=100,height=100)
star_two.grid(row=0,column=2)
star_three = tk.Canvas(root,width=100,height=100)
star_three.grid(row=0,column=3)
star_four = tk.Canvas(root,width=100,height=100)
star_four.grid(row=0,column=3)
star_five = tk.Canvas(root,width=100,height=100)
star_five.grid(row=0,column=4)

#metà stella (lato destro)
points2 = [0,10,10,40,40,40,15,60,25,90,0,70]
#metà stella (lato sinistro)
points1 = [50,70,25,90,35,60,10,40,40,40,50,10]
#stella intera
points = [10,40,40,40,50,10,60,40,90,40,65,60,75,90,50,70,25,90,35,60]
#Per aumentare o diminuire la grandezza della stella:
# for i in range(len(points)):
#     points[i] = points[i]/5

star_one.create_polygon(points,outline='red',fill='orange',width=2)
star_one.create_polygon(points,outline='red',fill='white',width=2)
star_two.create_polygon(points,outline='red',fill='orange',width=2)
star_three.create_polygon(points,outline='red',fill='white',width=2)
star_four.create_polygon(points,outline='red',fill='orange',width=2)
star_five.create_polygon(points,outline='red',fill='orange',width=2)


root.mainloop()