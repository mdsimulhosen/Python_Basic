from tkinter import *

root = Tk()
root.title("User Login")
root.geometry("500x300")

username = StringVar()
password = StringVar()

bl0 = Label(root, text="Page Login System", pady=5, fg="red", font=("calibri", 20, "bold"))
bl0.grid(row=0, column=1, columnspan=2, padx=20)

lb = Label(root, text="Username", bd=5, font=("calibri", 14, "bold"))
lb.grid(row=1, column=0, pady=5, padx=20)
e1 = Entry(root, textvariable=username, bd=5, font=("calibri", 14, "bold"))
e1.grid(row=1, column=1, pady=5, padx=20)

lb2 = Label(root, text="Password", bd=5, font=("calibri", 14, "bold"))
lb2.grid(row=2, column=0, pady=5, padx=20)
e2 = Entry(root, textvariable=password, bd=5, font=("calibri", 14, "bold"), show="*")
e2.grid(row=2, column=1, pady=5, padx=20)

lb4=Label(root, text="Wrong username or password !", font=("times new roman", 12, "bold"))

def login():
    name=e1.get()
    password=e2.get()
    if (name=="username" and password=="password"):
        lb5=Label(root, text="Login Successfully", font=("Vardana", 15,"bold"))
        lb5.grid(row=0, column=0, padx=10)
        e1.destroy()
        e2.destroy()
        lb.destroy()
        lb2.destroy()
        bl0.destroy()
        bt.destroy()
        lb4.destroy()

    else:
        lb4.grid(row=4, column=1, columnspan=2)
        e2.delete(0, END)
        e1.delete(0, END)

bt = Button(root, text="Login", bd=5, font=("calibri", 14, "bold"), command=login)
bt.grid(row=3, column=1, columnspan=2, pady=5, padx=20)

root.mainloop()
