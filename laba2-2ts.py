from Tkinter import *

root = Tk()
 

def add():
    winadd = Toplevel (root)
    winadd.title("Add")
   # fr_ent = Frame (winadd,bg="gray").grid(row=0,column=1,columnspan=2)
    ent0 = Entry (winadd).grid(row=0,column=0)
    ent1 = Entry (winadd).grid(row=0,column=1)
    ent2 = Entry (winadd).grid(row=0,column=2)
    ent3 = Entry (winadd).grid(row=0,column=3)
    ent4 = Entry (winadd).grid(row=1,column=0)
    ent5 = Entry (winadd).grid(row=1,column=1)
    ent6 = Entry (winadd).grid(row=1,column=2)
    ent7 = Entry (winadd).grid(row=1,column=3)
    ent8 = Entry (winadd).grid(row=2,column=0)
    ent9 = Entry (winadd).grid(row=2,column=1)
    ent10 = Entry (winadd).grid(row=2,column=2)
    ent11 = Entry (winadd).grid(row=2,column=3)
    ent12 = Entry (winadd).grid(row=3,column=0)
    ent13 = Entry (winadd).grid(row=3,column=1)
    ent14 = Entry (winadd).grid(row=3,column=2)
    ent15 = Entry (winadd).grid(row=3,column=3)
    #bt_ok = Button (winadd,text="OK",command=add_lable).grid(row=4,column=0,columnspan=4)

    def add_lable():
        for i in range(15):
            a = int((ent + str(i)).get())
            (lb + str(i)).config(text=str(a))
    bt_ok = Button (winadd,text="OK",command=add_lable).grid(row=4,column=0,columnspan=4)





fr_lb = Frame (root,bg="gray").grid(row=0,column=1,columnspan=2)
lb0 = Label (fr_lb,text="0").grid(row=0,column=0)
lb1 = Label (fr_lb,text="0").grid(row=0,column=1)
lb2 = Label (fr_lb,text="0").grid(row=0,column=2)
lb3 = Label (fr_lb,text="0").grid(row=0,column=3)
lb4 = Label (fr_lb,text="0").grid(row=1,column=0) 
lb5 = Label (fr_lb,text="0").grid(row=1,column=1) 
lb6 = Label (fr_lb,text="0").grid(row=1,column=2) 
lb7 = Label (fr_lb,text="0").grid(row=1,column=3) 
lb8 = Label (fr_lb,text="0").grid(row=2,column=0) 
lb9 = Label (fr_lb,text="0").grid(row=2,column=1) 
lb10 = Label (fr_lb,text="0").grid(row=2,column=2) 
lb11 = Label (fr_lb,text="0").grid(row=2,column=3) 
lb12 = Label (fr_lb,text="0").grid(row=3,column=0) 
lb13 = Label (fr_lb,text="0").grid(row=3,column=1) 
lb14 = Label (fr_lb,text="0").grid(row=3,column=2) 
lb15 = Label (fr_lb,text="0").grid(row=3,column=3)

bt_add = Button (root,text="Add",command=add).grid(row=4,column=0,columnspan=2)
bt_ex = Button (root,text="Exit",command=root.destroy).grid(row=4,column=2,columnspan=2)
bt_calc = Button (root,text="Calc").grid(row=5,column=0,columnspan=4)

root.mainloop()
