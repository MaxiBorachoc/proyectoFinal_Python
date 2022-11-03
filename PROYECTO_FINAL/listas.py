from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import functools
import cat_alt
import cat_arr
import cat_luc


contador = 0

pedido=[] 

def combo(root, ruta):
   
    if ruta=="arranque":
        marca=("Indiel", "Valeo", "Audi")
        tipo=("Impulsor", "Bobina", "Portaescobillas", "Tapa delantera", "Tapa trasera")
    elif ruta=="alter":
        marca=("Indiel", "Valeo", "Audi")
        tipo=("Regulador", "Portadiodos", "Rotor", "Polea", "Estator", "Rulemanes")
    elif ruta=="luc":
        marca=("Phillips", "Valeo", "Osram")
        tipo=("Luces bajas", "Luces altas", "Guiños", "Auxiliares", "Stop", "Marcha Atrás")
   


    lista2=Label(root, text="MODELO", font=("Bebas Neue", 22), bg="RoyalBlue3")
    lista2.grid(row=1, column=1)
 
    opcion_model=StringVar()
    model=("Fiat", "Volkswagen", "Peugeot", "Ford", "Toyota")
    opcion_model_tipo=StringVar()

    def cuenta(event):
        if comboAnio.get()!="" and comboTipo.get()!="" and comboMarca.get()!="":
            botonPedir = Button(root, text="Añadir al pedido", width=15, height=4, bg="medium sea green", command=añadir)
            botonPedir.place(x=425, y=590)


   


    def cambia(event):
        auto = comboModel.get()
        if auto == "Fiat":
            model_tipo=("Uno", "147", "Palio", "Strada", "Fiorino", "Cronos")
            combobox(model_tipo)
        elif auto == "Volkswagen":
            model_tipo=("Gol", "Golf", "Polo", "T-Cross", "Vento", "Bora", "Amarok")
            combobox(model_tipo)
        elif auto == "Peugeot":
            model_tipo=("106", "206", "207", "306", "307", "208")
            combobox(model_tipo)
        elif auto == "Ford":
            model_tipo=("Fiesta", "Fiesta Kinect", "Focus", "Ranger", "Taunus", "F100", "Maverick")
            combobox(model_tipo)
        elif auto == "Toyota":
            model_tipo=("Yaris", "Ethios", "Hilux", "Corolla", "Taunus", "F100", "Maverick")
            combobox(model_tipo)

  


    def combobox(model_tipo):
         comboModel_2=ttk.Combobox(root, width=30, textvariable=opcion_model_tipo, values=model_tipo)
         comboModel_2.grid(row=1, column=3)
         comboModel_2.bind("<<ComboboxSelected>>", cuenta)
         
        

  
               
    
    

    comboModel=ttk.Combobox(root, width=30, textvariable=opcion_model, values=model)
    comboModel.current(0)
    comboModel.grid(row=1, column=2)
    comboModel.bind("<<ComboboxSelected>>", cambia)

        

    lista1=Label(root, text="TIPO", font=("Bebas Neue", 22), bg="RoyalBlue3")
    lista1.grid(row=3, column=1,padx=80, pady=10)


    opcion_marca=StringVar()
   
    comboMarca=ttk.Combobox(root, width=30, textvariable=opcion_marca, values=marca)
    comboMarca.current(0)
    comboMarca.grid(row=4, column=2)

    lista2=Label(root, text="MARCA", font=("Bebas Neue", 22), bg="RoyalBlue3")
    lista2.grid(row=4, column=1,padx=80, pady=10)

    opcion_tipo=StringVar()
    

    comboTipo=ttk.Combobox(root, width=30, textvariable=opcion_tipo, values=tipo)
    comboTipo.current(0)
    comboTipo.grid(row=3, column=2)

    lista2=Label(root, text="AÑO", font=("Bebas Neue", 22), bg="RoyalBlue3")
    lista2.grid(row=2, column=1,padx=80, pady=10)

    opcion=StringVar()
    anio=("1990-95", "1996-00", "2001-05", "2006-2010", "2011-15", "2016-2022")

    comboAnio=ttk.Combobox(root, width=30, textvariable=opcion, values=anio)
    comboAnio.current(0)
    comboAnio.grid(row=2, column=2)

    cuadro_añadir = LabelFrame(root, width=7, height=4, bg="snow", bd=".5px")
    cuadro_añadir.place(x=425, y=590)

    labelPedir = Label(cuadro_añadir, text="Añadir al pedido", width=15, height=4, bg="gray75", font=("", 9))
    labelPedir.pack()
    
    
    
    
    comboMarca.bind("<<ComboboxSelected>>", cuenta)
    comboTipo.bind("<<ComboboxSelected>>", cuenta)
    comboAnio.bind("<<ComboboxSelected>>", cuenta)   

    def añadir():
        pedido.append(comboTipo.get())
        pedido.append(comboMarca.get())
        pedido.append(comboModel.get())
        pedido.append(comboAnio.get())
        messagebox.showinfo("Pedido", "¡PEDIDO REALIZADO CON ÉXITO!")
        global contador 
        contador.set(contador.get()+1)

    global contador
    contador = IntVar(value=0)

    botonCarrito = Button(root, textvariable=contador, width=5, height=2, bg="snow", font=("", 14))
    botonCarrito.place(x=6, y=600)