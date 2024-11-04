from tkinter import *

class myWindow:
    def __init__(self, win):
        self.Button1 = Button(win, bg="white", fg="black", text="Click to Change Color", command=self.changeColor)
        self.Button1.place(x=140, y=140)

    def changeColor(self):
        self.Button1.config(bg='yellow')

window = Tk()
MyWin = myWindow(window)
window.geometry("400x300+700+300")
window.title("Special Midterm Exam in OOP")
window.mainloop()
