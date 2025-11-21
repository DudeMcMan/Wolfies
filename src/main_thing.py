from tkinter import *

root = Tk()
root.geometry("200x200")

def show():
    if(opt.get() == opt2.get()):
        lbl.config(text="Same thing")
    elif(opt.get() == "1"):
        if(opt2.get() == "2"):
            lbl.config(text=comboList[0])
        if(opt2.get() == "3"):
            lbl.config(text=comboList[1])
        if(opt2.get() == "4"):
            lbl.config(text=comboList[2])
    elif(opt.get() == "2"):
        if(opt2.get() == "1"):
            lbl.config(text=comboList[0])
        if(opt2.get() == "3"):
            lbl.config(text=comboList[3])
        if(opt2.get() == "4"):
            lbl.config(text=comboList[4])
    elif(opt.get() == "3"):
        if(opt2.get() == "1"):
            lbl.config(text=comboList[1])
        if(opt2.get() == "2"):
            lbl.config(text=comboList[3])
        if(opt2.get() == "4"):
            lbl.config(text=comboList[5])
    else:
        if(opt2.get() == "1"):
            lbl.config(text=comboList[2])
        if(opt2.get() == "2"):
            lbl.config(text=comboList[4])
        if(opt2.get() == "3"):
            lbl.config(text=comboList[5])


list1 = ["1", "2", "3", "4"]
list2 = ["1", "2", "3", "4"]
comboList = ["1 and 2", "1 and 3", "1 and 4", "2 and 3", "2 and 4", "3 and 4"]


opt = StringVar(value="Pick")
opt2 = StringVar(value="Pick")

OptionMenu(root, opt, *list1).pack()
OptionMenu(root, opt2, *list2).pack()

Button(root, text="Click Me", command=show).pack()

lbl = Label(root, text=" ")
lbl.pack()

root.mainloop()
