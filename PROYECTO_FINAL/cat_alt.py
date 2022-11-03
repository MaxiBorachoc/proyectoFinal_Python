from tkinter import *
from tkinter import ttk
import functools
import listas

def alter(parent):
    parent.withdraw()
    root = Toplevel(parent)
    root.geometry('1000x700')
    root.config(bg="RoyalBlue3")
    root.protocol("WM_DELETE_WINDOW", functools.partial(volver, parent, root))
    botonAtras = Button(root, text="<-", width=12, height=3, bg="snow")
    botonAtras.place(x=900, y=600)

    labelPedidoActual = Label(root, text="CATALOGO PARA ALTERNADOR", width=30, height=1, bg="RoyalBlue3", font=("Bebas Neue", 28), fg="IndianRed3")
    labelPedidoActual.grid(row=0, column=2, pady=50, padx=50)
    ruta = "alter"
    listas.combo(root, ruta)
    
    botonAtras = Button(root, text="<-", width=12, height=3, bg="snow", command=functools.partial(volver, parent, root))
    botonAtras.place(x=900, y=600)
    
def volver(parent, root):
    parent.deiconify()
    root.destroy()