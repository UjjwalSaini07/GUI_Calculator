# This is The First Program Of Calculator in Which Exceptional Handling Used 
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

exit()
#IF you want to run the second program you make firstly first program as comment out 

# This is the code for Second Calculator In which exceptional handling not used but in that i used good design for buttons
from tkinter import *

win = Tk()  # This is to create a basic window
win.geometry("312x324")  # this is for the size of the window
win.resizable(0, 0)  # this is to prevent from resizing the window
win.title("Calculator")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 'bt_clear' function :This is used to clear
# the input field

def bt_clear():
    global expression
    expression = ""
    input_text.set("")

# 'bt_equal':This method calculates the expression
# present in input field

def bt_equal():
    global expression
    result = str(eval(expression))  # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""

expression = ""

# 'StringVar()' :It is used to get the instance of input field

input_text = StringVar()

# Let us creating a frame for the input field

input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)

input_frame.pack(side=TOP)

# Let us create a input field inside the 'Frame'

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
                    justify=RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)  # 'ipady' is internal padding to increase the height of input field

# Let us creating another 'Frame' for the button below the 'input_frame'

btns_frame = Frame(win, width=312, height=272.5, bg="grey")

btns_frame.pack()

# first row
clear = Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

# second row
seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)

eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)

nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

# third row
four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)

five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

# fourth row
one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)

three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
              command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

# fourth row
zero = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)

equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)

win.mainloop()
