from tkinter import *

root = Tk()
root.geometry("200x200")

def show():
    if(opt.get() == opt2.get()):
        lbl.config(text="Same thing")
    else:
        lbl.config(text=opt.get() + " " + opt2.get())

list1 = ["1", "2", "3", "4"]
list2 = ["1", "2", "3", "4"]


opt = StringVar(value="Pick")
opt2 = StringVar(value="Pick")

OptionMenu(root, opt, *list1).pack()
OptionMenu(root, opt2, *list2).pack()

Button(root, text="Click Me", command=show).pack()

lbl = Label(root, text=" ")
lbl.pack()

root.mainloop()