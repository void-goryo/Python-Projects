
from tkinter import *


#window
win = Tk()
f = Frame(win)

#label
l = Label(win, text = 'This should be above everything')
l.pack()

#buttons
b1 = Button(f, text = 'One')
b2 = Button(f, text = 'Two')
b1.configure(text = 'Uno')  #override


#display
b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT, padx = 10)

#b1.grid(row=0, column=0)
#b2.grid(row=1, column=1)


#definitions
def but1():
    print('Uno was pushed')


#commands
b1.configure(command=but1)

#text
v = StringVar()
e = Entry(win, textvariable = v)
e.pack()
v.set('Type here')

#list
lb = Listbox(f, height = 3)
lb.pack()
lb.insert(END, 'first')
lb.insert(END, 'second')
lb.insert(END, 'third')
lb.insert(END, 'forth')

#scrollbar
sb = Scrollbar(win, orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)

#link list w/ bar
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)

f.pack()
