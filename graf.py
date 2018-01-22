from math import *
from Tkinter import *

f = input('f(x):')

root = Tk()

canv = Canvas(root, width = 1000, height = 1000, bg = "white")
canv.create_line(500,1000,500,0,width=2,arrow=LAST) 
canv.create_line(0,500,1000,500,width=2,arrow=LAST) 

First_x = -500;

for i in range(16000):
	if (i % 800 == 0):
		k = First_x + (1 / 16) * i
		canv.create_line(k + 500, -3 + 500, k + 500, 3 + 500, width = 0.5, fill = 'black')
		canv.create_text(k + 515, -10 + 500, text = str(k), fill="purple", font=("Helvectica", "10"))
		if (k != 0):
			canv.create_line(-3 + 500, k + 500, 3 + 500, k + 500, width = 0.5, fill = 'black')
			canv.create_text(20 + 500, k + 500, text = str(k), fill="purple", font=("Helvectica", "10"))
	try:
		x = First_x + (1 / 16) * i
		new_f = f.replace('x', str(x))
		y = -eval(new_f) + 500
		x += 500
		canv.create_oval(x, y, x + 1, y + 1, fill = 'black')
	except:
		pass
canv.pack()	
root.mainloop()
