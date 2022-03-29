#Import the required library
from tkinter import *
#Create an instance of tkinter frame
win = Tk()
win.geometry("750x250")
#Create a String Object and set the default value
var = StringVar()
#Create a text label
label = Entry(win, textvariable = var, font=('Helvetica 20 italic'))
label.pack()
#Create an entry widget to change the variable value
text = Entry(win, textvariable = var)
text.pack()
win.mainloop()