from tkinter import *

class MyWindow:
    def __init__ (self, win):
        self.Label1 = Label (win, fg = "Black", text = "Calculator", font = ('bold', 15))
        self.Label1.place (x = 135, y = 10)

        self.Label2 = Label (win, text = "Number 1: ")
        self.Label2.place (x = 50, y = 40)
        self.Entry1 = Entry (win, bd = 5)
        self.Entry1.place (x = 120, y = 40 )

        self.Label2 = Label (win, text = "Number 2: ")
        self.Label2.place (x = 50, y = 80)
        self.Entry2 = Entry (win, bd = 5)
        self.Entry2.place (x = 120, y = 80 )

        self.Label3 = Label (win, text = "Result: ")
        self.Label3.place (x = 60, y = 120)
        self.Entry3 = Entry (win, bd = 5)
        self.Entry3.place (x = 120, y = 120)

        self.Button1 = Button (win, bg = "black", fg = "white", text = "Add", command = self.add)
        self.Button1.place (x = 60, y = 160)

        self.Button2 = Button (win, bg = "black", fg = "white", text = "Subtract", command = self.sub)
        self.Button2.place (x = 100, y = 160)

        self.Button3 = Button (win, bg = "black", fg = "white", text = "Multiply", command = self.mul)
        self.Button3.place (x = 160, y = 160)

        self.Button4 = Button (win, bg = "black", fg = "white", text = "Divide", command = self.div)
        self.Button4.place (x = 220, y = 160)

        self.Button5 = Button (win, bg = "black", fg = "white", text = "Clear")
        self.Button5.place (x = 270, y = 160)
        self.Button5.bind('<Button-1>', self.clear)

        self.Button6 = Button (win, bg = "black", fg = "white", text = "hehe", command= self.special)
        self.Button6.place (x = 90, y = 200, width = 200)


    def add (self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result  = num1 + num2
        self.Entry3.insert(END, str(result))

    def sub (self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result  = num1 - num2
        self.Entry3.insert(END, str(result))

    def mul(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))

    def div(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 / num2
        self.Entry3.insert(END, str(result))

    def clear(self, win):
        self.Entry1.delete(0, 'end')
        self.Entry2.delete(0, 'end')
        self.Entry3.delete(0, 'end')

    def special (self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = 'Miss na kita! :>'
        self.Entry3.insert(END, str(result))

window = Tk()
MyWin = MyWindow(window)
window.geometry("400x300+10+10")
window.title("Standard Calculator")
window.mainloop()

