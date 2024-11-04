from tkinter import *

class myWindow:
    def __init__ (self, win):
        self.Label1 = Label (win, text = "Enter your fullname: ", fg = 'red')
        self.Label1.place (x = 30, y = 70)
        self.Entry1 = Entry (win, bd = 3)
        self.Entry1.place (x = 240, y = 70 )

        self.Button2 = Button(win, bg="white", fg="red", text="Click to display your Fullname", command= self.fullName)
        self.Button2.place(x=30, y=100)
        self.Entry2 = Entry (win, bd = 3)
        self.Entry2.place (x = 240, y = 100 )


    def fullName (self):
        entry = self.Entry1.get()
        result = entry
        self.Entry2.insert(END, result)

window = Tk()
MyWin = myWindow(window)
window.geometry("400x300+700+300")
window.title("Midterm in OOP")
window.mainloop()
