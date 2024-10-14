from tkinter import *
from tkinter import messagebox

class myWindow:
    def __init__ (self, win):
        self.Label1 = Label (win, fg = "Black", text = "Account Registration System", font = ('bold'))
        self.Label1.place (x = 100, y = 30)

        self.Label2 = Label (win, text = "First Name: ")
        self.Label2.place (x = 100, y = 70)
        self.Entry2 = Entry (win, bd = 1)
        self.Entry2.place (x = 170, y = 70 )

        self.Label3 = Label(win, text="Last Name: ")
        self.Label3.place(x=100, y=100)
        self.Entry3 = Entry(win, bd=1)
        self.Entry3.place(x=170, y=100)

        self.Label4 = Label(win, text="Username: ")
        self.Label4.place(x=100, y=130)
        self.Entry4 = Entry(win, bd=1)
        self.Entry4.place(x=170, y=130)

        self.Label5 = Label(win, text="Password: ")
        self.Label5.place(x=100, y=160)
        self.Entry5 = Entry(win, bd=1,  show = "*")
        self.Entry5.place(x=170, y=160)

        self.Label6 = Label(win, text="Email Address: ")
        self.Label6.place(x=80, y=190)
        self.Entry6 = Entry(win, bd=1)
        self.Entry6.place(x=170, y=190)

        self.Label7 = Label(win, text="Contact Number: ")
        self.Label7.place(x=65, y=220)
        self.Entry7 = Entry(win, bd=1)
        self.Entry7.place(x=170, y=220)

        self.Button1 = Button(win, bg="white", fg="black", text="Submit", command = self.submit)
        self.Button1.place(x=120, y=250)

        self.Button2 = Button(win, bg="white", fg="black", text="Clear", command= self.clear)
        self.Button2.place(x=220, y=250)

    def clear(self):
        self.Entry2.delete(0, 'end')
        self.Entry3.delete(0, 'end')
        self.Entry4.delete(0, 'end')
        self.Entry5.delete(0, 'end')
        self.Entry6.delete(0, 'end')
        self.Entry7.delete(0, 'end')

    def submit(self):
        # Gather all entries
        entries = {
            "First Name": self.Entry2.get(),
            "Last Name": self.Entry3.get(),
            "Username": self.Entry4.get(),
            "Password": self.Entry5.get(),
            "Email": self.Entry6.get(),
            "Contact Number": self.Entry7.get()
        }

        # Check if any entry is empty
        for field, value in entries.items():
            if not value:
                messagebox.showwarning("Input Error", f"{field} is required!")
                return

        # If all entries are filled, show success message
        messagebox.showinfo("Success", "Sucessfully Submitted!")
