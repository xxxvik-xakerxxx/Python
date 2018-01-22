from Tkinter import *

root = TK()

def ui():

def dany():
    x = int(ent_x.get())
    y = int(ent_y.get())
    fr_ent.config(width=(8.43)*(x),height=(12,75)*(y))
    win = Toplavel (root,bg="lightblue")
    win.title("Daniy")
    fr_ent = Frame (win,bg="gray")
    for i>x:
        for i>y:
            ent_(x)(y)= Entry(fr_ent)
            

    btn_ok = Button (win,text="OK",command=calc)


def calc():

def close_wind():
    root.destroy()

ent_x = Entry (root)
ent_y = Entry (root)

lb_0 = Lable (root,text="Zero:")



fr_lb = Frame (root,bg="gray")

btn_calc = Button (root,text="Calc",command=dany)
btn_ex = Button (root,text="Exit",command=close_wind)


root.mainloop()
