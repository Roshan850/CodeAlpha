from tkinter import *
from tkinter import messagebox     
from random import randint  


root = Tk()
root.title("PASSWORD GENERATOR")
img= PhotoImage(file="D:\\RKJ\\Tkinter\\password image.png")
root.iconphoto(False,img)
# root.iconbitmap("D:\\RKJ\\Tkinter\\password image.png")
root.geometry("500x300")
root.config(bg="#121212")  # Dark background

my_password = chr(randint(33, 126))

def new_rand():
    pw_entry.delete(0, END)

    pw_length = int(my_entry.get())

    my_password = ""

    for x in range(pw_length):
        my_password += chr(randint(33, 126))

    pw_entry.insert(0, my_password)

def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# LabelFrame
lf = LabelFrame(root, text="How many Characters?", bg="#1f1f2e", fg="#e0e0e0", font=("arial", 12, "bold"))
lf.pack(pady=20)

# Entry for password length
my_entry = Entry(lf, font=("arial", 24), bg="#2c2c3e", fg="#ffffff", justify="center", bd=2, relief="groove")
my_entry.pack(pady=20, padx=20)

# Entry for generated password
pw_entry = Entry(root, text='', font=("arial", 24), bd=0, bg="#2c2c3e", fg="#ffffff", justify="center")
pw_entry.pack(pady=20)

# Frame for buttons
my_frame = Frame(root, bg="#121212")
my_frame.pack(pady=20)

# Buttons
my_button = Button(my_frame, text="Generate Strong Password", command=new_rand, font=("arial", 12, "bold"), bg="#ff5722", fg="#ffffff", activebackground="#e64a19", activeforeground="#ffffff", bd=3, relief="raised")
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboard", command=clipper, font=("arial", 12, "bold"), bg="#03a9f4", fg="#ffffff", activebackground="#0288d1", activeforeground="#ffffff", bd=3, relief="raised")
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()
