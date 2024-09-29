from currency_converter import CurrencyConverter
import tkinter as tk
from tkinter import*

background="#03051d"
framebg="EDEDED"
framefg="06283D"

a= CurrencyConverter()
root = tk.Tk()
root.geometry("700x380")
root.title("Currency Converter")
root.resizable(False,False)

#background image 
frame=Frame(root,bg="red")
frame.pack(fill=Y)

backgroundimage=PhotoImage(file="bg1.png")
Label(frame,image=backgroundimage).pack()


def clicked():
    amount=(e1.get())
    cur1=e2.get()
    cur2=e3.get()
    data = a.convert(amount,cur1,cur2)
    l5=tk.Label(root,text=data,font= "Times 15 bold",bg="#03051d",fg="#f8af3c").place(x=420,y=340)


#icon image 
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)


l1=tk.Label(root,text="Currency  Converter",font= "Times 25 bold", bg="#03051d",fg="#58a63c").place(x=215,y=20)
l2=tk.Label(root,text="Enter amount ",font= "Times 18 bold",bg="#03051d",fg="#f8af3c").place(x=208,y=110)
e1=tk.Entry(root)
l3=tk.Label(root,text="Enter currency",font= "Times 18 bold",bg="#03051d",fg="#f8af3c").place(x=202,y=160)
e2=tk.Entry(root)
l4=tk.Label(root,text="Required currency",font= "Times 16 bold",bg="#03051d",fg="#f8af3c").place(x=198,y=256)
e3=tk.Entry(root)
e4=tk.Entry(root,bg="#00264d",width=30,border=0)
e5=tk.Entry(root,bg="#00264d",width=30,border=0)


button= tk.Button(root,width=10,text="Convert",border=0,bg="#03051d",cursor='hand2',fg="#f8af3c",font= "Times 13 bold",command=clicked)
button.place(x=130,y=340)
e1.place(x=380,y=120)
e2.place(x=380,y=170)
e3.place(x=375,y=258)
e4.place(x=420,y=340)
e5.place(x=420,y=352)

root.mainloop()
