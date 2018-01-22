from Tkinter import *
from math import hypot

root = Tk()

def calc():
    ax = int(ent_ax.get())
    ay = int(ent_ay.get())
    bx = int(ent_bx.get())
    by = int(ent_by.get())
    cx = int(ent_cx.get())
    cy = int(ent_cy.get())

    ab = hypot(bx-ax,by-ay)
    ac = hypot(cx-ax,cy-ay)

    if ab>ac:
        z=bx,by
    else:
        z=cx,cy
    lb_ans.config(text='Answer:' + str(z))

def close_wind():
    root.destroy()

lb_x = Label (root,text="x")
lb_y = Label (root,text="y")
lb_a = Label (root,text="a")
lb_b = Label (root,text="b")
lb_c = Label (root,text="c")

lb_ans = Label (root,text="Answer:")

ent_ax = Entry (root)
ent_ay = Entry (root)
ent_bx = Entry (root)
ent_by = Entry (root)
ent_cx = Entry (root)
ent_cy = Entry (root)

btn_1 = Button (root,text="Calc",command=calc)
btn_ex = Button (root,text="Exit",command=close_wind)

lb_x.grid(row=0,column=1)
lb_y.grid(row=0,column=2)

lb_a.grid(row=1,column=0)
ent_ax.grid(row=1,column=1)
ent_ay.grid(row=1,column=2)

lb_b.grid(row=2,column=0)
ent_bx.grid(row=2,column=1)
ent_by.grid(row=2,column=2)

lb_c.grid(row=3,column=0)
ent_cx.grid(row=3,column=1)
ent_cy.grid(row=3,column=2)

lb_ans.grid(row=4,column=0,columnspan=3)

btn_1.grid(row=5,column=1,sticky="e")
btn_ex.grid(row=5,column=2,sticky="w")

root.mainloop()
