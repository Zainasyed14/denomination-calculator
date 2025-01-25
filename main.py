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


root.mainloop()
