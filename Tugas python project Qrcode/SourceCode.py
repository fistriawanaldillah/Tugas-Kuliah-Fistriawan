from tkinter import *
import qrcode

root=Tk()
root.title("Qr generator")
root.geometry("1000x550")
root.config(bg="#AE2321")
root.resizable(False,False)

#icon_image
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

def generate():
    name=title.get()
    text=Entry
    qr=qrcode.make(text)
    # qrcode.make(text)
    qr.save("../Qrcode/"+ str(name)+".png")

    global image
    image=PhotoImage(file="../Qrcode/"+ str(name)+".png")
    image_view.config(image=image)

image_view=Label(root,bg="#AE2321")
image_view.pack(padx=50,pady=10,side=RIGHT)

Label(root,text="Title",fg="white",bg="#AE2321",font=15).place(x=50,y=170)

title=Entry(root,width=13,font="arial 15")
title.place(x=50,y=200)

title=Entry(root,width=28,font="arial 15")
title.place(x=50,y=250)

Button(root,text="Generate",width=20,height=2,bg="black",fg="white",command=generate).place(x=50,y=300)

root.mainloop()
