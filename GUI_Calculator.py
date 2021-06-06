from tkinter import *
from tkinter import messagebox

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
                messagebox.showerror("Showerror", "Error")
        scvalue.set(value)
        screen.update()
    elif text == "Clear":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("500x730")
root.minsize(490,720)
root.maxsize(510,735)
root.title("Calculator")
root.wm_iconbitmap("Calculator.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue,borderwidth= "15" ,font="lucida 30 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# Creating First Frame
f1 = Frame(root)
# Button For Number 7
b = Button(f1, text="7", padx=21, pady=18, font="lucida 22 bold",borderwidth= "5" )
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
# Button For Number 8
b = Button(f1, text="8", padx=21, pady=18, font="lucida 22 bold",borderwidth= "5" )
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
# Button For Number 9
b = Button(f1, text="9", padx=21, pady=18, font="lucida 22 bold",borderwidth= "5" )
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
f1.pack()

# Creating Second Frame
f2 = Frame(root)
# Button For Number 4
b = Button(f2, text="4", padx=21, pady=18, font="lucida 22 bold",borderwidth= "5" )
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
# Button For Number 5
b = Button(f2, text="5", padx=21, pady=18, font="lucida 22 bold",borderwidth= "5" )
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
# Button For Number 6
b = Button(f2, text="6", padx=21, pady=18, font="lucida 22 bold",borderwidth= "5" )
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
f2.pack()

# Creating Third Frame
f3 = Frame(root)
# Button For Number 1
b = Button(f3, text="1", padx=21, pady=18, font="lucida 22 bold",borderwidth= "5" )
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
# Button For Number 2
b = Button(f3, text="2", padx=21, pady=18, font="lucida 22 bold",borderwidth= "5" )
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
# Button For Number 3
b = Button(f3, text="3", padx=21, pady=18, font="lucida 22 bold",borderwidth= "5" )
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
f3.pack()

# Creating Fourth Frame
f4 = Frame(root)
# Button For +
b = Button(f4, text="+", padx=22, pady=18, font="lucida 22 bold",borderwidth= "5" )
b.pack(side=LEFT,padx=12, pady=5)
b.bind("<Button-1>", click)
# Button For Number 0
b = Button(f4, text="0", padx=21, pady=18, font="lucida 22 bold",borderwidth= "5" )
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
# Button For -
b = Button(f4, text="-", padx=24, pady=18, font="lucida 22 bold",borderwidth= "5" )
b.pack(side=LEFT, padx=14, pady=5)
b.bind("<Button-1>", click)
f4.pack()

# Creating Fifth Frame
f5 = Frame(root)
# Button For *
b = Button(f5, text="*", padx=25, pady=18, font="lucida 22 bold",borderwidth= "5" )
b.pack(side=LEFT,padx=15, pady=5)
b.bind("<Button-1>", click)
# Button For /
b = Button(f5, text="/", padx=21, pady=18, font="lucida 22 bold",borderwidth= "5" )
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
# Button For =
b = Button(f5, text="=", padx=21, pady=18, font="lucida 22 bold",borderwidth= "5" )
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
f5.pack()

b=Button(root,text="Clear", font="lucida 18 bold",borderwidth= "3" )
b.pack()
b.bind("<Button-1>", click)

statusvar = StringVar()
statusvar.set("Program Created By Ujjwal Saini" )
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w", font="lucida 12 bold")
sbar.pack(side=BOTTOM, fill=X)

root.mainloop()