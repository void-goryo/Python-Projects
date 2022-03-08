
import tkinter
from tkinter import *



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('learning Tkinter!')
        self.master.config(bg = 'light gray')
            
        #text box
        self.varFname = StringVar()
        self.varLname = StringVar()

    #Indicators
        self.lblFname = Lable(self.master, text = 'First Name: ', font = ('Helvetica', 16), fg = 'black', bg = 'lightblue')
        self.txtFname.grid(row = 0, column = 0)

        self.lblLname = Lable(self.master, text = 'Last Name: ', font = ('Helvetica', 16), fg = 'black', bg = 'lightblue')
        self.txtLname.grid(row = 1, column = 0)

    #Text Fields
        self.txtFname = Entry(self.master, text = self.varFname, font = ('Helvetica', 16), fg = 'black', bg = 'lightblue')
        self.txtFname.grid(row =, column=)    #placment
        
        self.txtLname = Entry(self.master, text = self.varLname, font = ('Helvetica', 16), fg = 'black', bg = 'lightblue')
        self.txtLname.grid()


if __name__ in '__main__':


    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
