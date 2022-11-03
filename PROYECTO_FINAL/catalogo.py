from tkinter import *
from tkinter import ttk
import functools
from PIL import Image, ImageTk
import cat_arr
import cat_alt
import cat_luc


def initCat(parent):
    parent.withdraw()
    root = Toplevel(parent)
    root.geometry('1000x700')
    root.resizable(False, False)
    root.title("CATALOGO DE PRODUCTOS")
    root.config(bg="RoyalBlue3")
    root.iconbitmap('PROYECTO_FINAL/assets/carrito.ico')
    root.protocol("WM_DELETE_WINDOW", functools.partial(volver, parent, root))

    img1 = Image.open("PROYECTO_FINAL/assets/alternador.png")
    img2 = Image.open("PROYECTO_FINAL/assets/arranque.png")
    img3 = Image.open("PROYECTO_FINAL/assets/faro.png")

    img_alter= ImageTk.PhotoImage(img1)
    img_arr= ImageTk.PhotoImage(img2)
    img_faro= ImageTk.PhotoImage(img3)

    labelTitle = Label(root, text="SELECCIONE EL TIPO DE PRODUCTO", font=("Bebas Neue", 44), bg="RoyalBlue3", fg="IndianRed3")
    labelTitle.place(x=175, y=30)

    imgArr=Label(root, image=img_arr, bg="RoyalBlue3")
    imgArr.place(x=640, y=130)

    imgAlter=Label(root, image=img_alter, bg="RoyalBlue3")
    imgAlter.place(x=640, y=340)

    imgLuc=Label(root, image=img_faro, bg="RoyalBlue3", width=300, height=150)
    imgLuc.place(x=620, y=550)
    
    def irArr():
        cat_arr.arranque(root)

    def irAlter():
        cat_alt.alter(root)

    def irLuc():
        cat_luc.luces(root)

         
    botonArranque = Button(root,text="MOTOR DE ARRANQUE", bg="IndianRed3", command=irArr, font=("Bebas Neue", 18), width=30)
    botonArranque.grid(row=1, column=0, pady=160, padx=140)

    botonAlter = Button(root,text="ALTERNADOR",  bg="IndianRed3", command=irAlter, font=("Bebas Neue", 18), width=30)
    botonAlter.grid(row=2, column=0, padx=140)


    botonLuces = Button(root, text="LUCES", bg="IndianRed3", command=irLuc, font=("Bebas Neue", 18), width=30)
    botonLuces.grid(row=3, column=0, pady=150, padx=140)


    botonAtras = Button(root, text="<-", width=12, height=3, bg="snow", command=functools.partial(volver, parent, root))
    botonAtras.place(x=900, y=600)
   
    
    root.mainloop()


def volver(parent, root):
    parent.deiconify()
    root.destroy()

