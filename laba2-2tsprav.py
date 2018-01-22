from Tkinter import *

N_ROWS=4
N_COLS=4

root = Tk()

ARRAY   = [[1 for c in range(N_COLS)] for r in range(N_ROWS)]
V_ARRAY = []

fr_lb = Frame (root,bg="gray").grid(row=0,column=1,columnspan=2)
for r in range(N_ROWS):
  V_ARRAY.append([])
  for c in range(N_COLS):
    V_ARRAY[r].append(Label(fr_lb, text=ARRAY[r][c]))
    V_ARRAY[r][c].grid(row=r, column=c)

def add():
  winadd = Toplevel (root)
  winadd.title("Add")
  A_ARRAY = []
  for r in range(N_ROWS):
    A_ARRAY.append([])
    for c in range(N_COLS):
      A_ARRAY[r].append(Entry(winadd))
      A_ARRAY[r][c].insert(0, '0')
      A_ARRAY[r][c].grid(row=r, column=c)
  bt_ok = Button (winadd,text="OK",command=lambda: mas_add(winadd, A_ARRAY)).grid(row=4,column=0,columnspan=4)

def calc (A_ARRAY):
	for r in range(N_ROWS):
		for c in range(N_COLS):
			i=0
			tg=0
			a=A_ARRAY[r][c]
			if tg==0 or a==0:
				i+1
				tg=1
				if r==4:
					tg=0


def mas_add(win, A_ARRAY):
  for r in range(N_ROWS):
    for c in range(N_COLS):
      cur_value = int(V_ARRAY[r][c]['text'])
      add_value = int(A_ARRAY[r][c].get())
      V_ARRAY[r][c]['text'] = str(cur_value + add_value)
  win.destroy()
  A_ARRAY = []

bt_add = Button (root,text="Add",command=add).grid(row=4,column=0,columnspan=2)
bt_ex = Button (root,text="Exit",command=root.destroy).grid(row=4,column=2,columnspan=2)
bt_calc = Button (root,text="Calc",command=calc).grid(row=5,column=0,columnspan=4)

mainloop()
