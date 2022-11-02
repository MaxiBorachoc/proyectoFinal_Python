from tkinter import *
from tkinter import ttk
import functools
import cat_alt
import cat_arr
import cat_luc

def combo(root):

    lista2=Label(root, text="MODELO", font=("Bebas Neue", 22), bg="RoyalBlue3")
    lista2.grid(row=1, column=1)
 
    opcion_model=StringVar()
    model=("mod1", "mod2", "mod3")

    opcion_model_tipo=StringVar()
    model_tipo=("modelo1", "modelo2", "modelo4", "modelo5")

    combobox3=ttk.Combobox(root, width=30, textvariable=opcion_model, values=model)
    combobox3.current(0)
    combobox3.grid(row=1, column=2)
    
    combobox3_1=ttk.Combobox(root, width=30, textvariable=opcion_model_tipo, values=model_tipo)
    combobox3_1.current(0)
    combobox3_1.grid(row=1, column=3)

    lista1=Label(root, text="TIPO", font=("Bebas Neue", 22), bg="RoyalBlue3")
    lista1.grid(row=3, column=1,padx=80, pady=10)

    opcion_tipo=StringVar()
    alterTipo=("Indiel", "Valeo", "Audi")

    combobox=ttk.Combobox(root, width=30, textvariable=opcion_tipo, values=alterTipo)
    combobox.current(0)
    combobox.grid(row=3, column=2)

    lista2=Label(root, text="MARCA", font=("Bebas Neue", 22), bg="RoyalBlue3")
    lista2.grid(row=4, column=1,padx=80, pady=10)

    opcion_marca=StringVar()
    marca=("Luces bajas", "Luces altas", "Guiños", "Auxiliares", "Stop", "Marcha Atrás")

    combobox2=ttk.Combobox(root, width=30, textvariable=opcion_marca, values=marca)
    combobox2.current(0)
    combobox2.grid(row=2, column=2)

    lista2=Label(root, text="AÑO", font=("Bebas Neue", 22), bg="RoyalBlue3")
    lista2.grid(row=2, column=1,padx=80, pady=10)

    opcion=StringVar()
    anio=("1990-95", "1996-00", "2001-05", "2006-2010", "2011-15", "2016-2022")

    combobox4=ttk.Combobox(root, width=30, textvariable=opcion, values=anio)
    combobox4.current(0)
    combobox4.grid(row=4, column=2)

    cuadro_añadir = LabelFrame(root, width=7, height=4, bg="snow", bd=".5px")
    cuadro_añadir.place(x=425, y=590)

    labelPedir = Label(cuadro_añadir, text="Añadir al pedido", width=15, height=4, bg="gray75", font=("", 9))
    labelPedir.pack()

    ##botonPedir = Button(raiz, text="Añadir al pedido", width=15, height=4, bg="medium sea green")
    ##botonPedir.place(x=425, y=590)
    contador = IntVar()
    contador= 0
    botonCarrito = Button(root, text=contador, width=5, height=2, bg="snow", font=("", 14))
    botonCarrito.place(x=6, y=600)