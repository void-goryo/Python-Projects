
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
        self.lblFname = Label(self.master, text = 'First Name: ', font = ('Helvetica', 16), fg = 'black', bg = 'lightgray')
        self.lblFname.grid(row = 0, column = 0, padx=(30,0), pady=(30,0))

        self.lblLname = Label(self.master, text = 'Last Name: ', font = ('Helvetica', 16), fg = 'black', bg = 'lightgray')
        self.lblLname.grid(row = 1, column = 0, padx=(30,0), pady=(30,0))

    #Text Fields
        self.txtFname = Entry(self.master, text = self.varFname, font = ('Helvetica', 16), fg = 'black', bg = 'lightgray')
        self.txtFname.grid(row =0, column=1, padx=(30,0), pady=(30,0))    #placment
        
        self.txtLname = Entry(self.master, text = self.varLname, font = ('Helvetica', 16), fg = 'black', bg = 'lightgray')
        self.txtLname.grid(row = 1, column = 1, padx=(30,0), pady=(30,0)) #calspan = 2 will expand into two columns

    #Button
        self.btnSubmit = Button(self.master, text='Submit', width = 10, height = 2)
        self.btnSubmit.grid(row = 2, column = 1, padx=(0,0), pady=(30, 0), sticky = NE)




        


if __name__ in '__main__':


    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
