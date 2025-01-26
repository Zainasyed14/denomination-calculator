from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination Calculator")
root.configure(bg='navy blue')
root.geometry("650x400")

upload = Image.open("app_img.jpg")
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='navy blue')
upload = upload.resize((300,300))
label.place(x=180, y=20)

label1 = Label(root,
               text="Hi there!! Welcome to The Denomination Calculator Application.",
               bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        "Alert!" ,"Do you want to calculate the denomination?")
    if MsgBox == 'ok':
        topwin()

button1 = Button(root,
                 text="Let's get started!",
                 command=msg,
                 bg='brown',
                 fg='white')
button1.place(x=260 , y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg='light grey')
    top.geometry("600x350")
    label = Label(top , text="Enter total amount" , bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are the number of notes for each denomination", bg='light grey')

    l1 = Label(top, text="Rs. 5000", bg='light grey')
    l2 = Label(top, text="Rs. 1000", bg='light grey')
    l3 = Label(top, text="Rs. 500" , bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note5000 = amount//5000
            amount %= 5000
            note1000 = amount//1000
            amount %= 1000
            note500 = amount//500

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note5000))
            t2.insert(END, str(note1000))
            t3.insert(END, str(note500))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(top, text="Calculate" , command=calculator, bg='brown', fg='white')

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    topwin.mainloop()
root.mainloop()
