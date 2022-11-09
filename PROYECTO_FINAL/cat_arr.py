from tkinter import *
from tkinter import ttk
import functools
import listas

def arranque(parent):
        parent.withdraw()
        root = Toplevel(parent)
        root.geometry('750x450')
        root.config(bg="RoyalBlue3")
        root.iconbitmap('PROYECTO_FINAL/assets/carrito.ico')
        root.protocol("WM_DELETE_WINDOW", functools.partial(volver, parent, root))
   
        labelPedidoActual = Label(root, text="CATALOGO PARA MOTOR DE ARRANQUE", width=30, height=1, bg="RoyalBlue3", font=("Bebas Neue", 28), fg="IndianRed3")
        labelPedidoActual.grid(row=0, column=1, padx=0, pady=10)
        ruta = "arranque"
        listas.combo(root, ruta)

        botonAtras = Button(root, text="<-", width=8, height=2, bg="snow", command=functools.partial(volver, parent, root))
        botonAtras.place(x=660, y=390)
        
def volver(parent, root):
    parent.deiconify()
    root.destroy()