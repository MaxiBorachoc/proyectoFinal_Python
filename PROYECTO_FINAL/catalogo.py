from tkinter import *
from tkinter import ttk
from PIL import Image

raiz = Tk()
raiz.geometry('1400x800')
raiz.title("CATALOGO DE PRODUCTOS")
raiz.resizable(False, False)
raiz.config(bg="RoyalBlue3")
raiz.iconbitmap('PROYECTO_FINAL/assets/carrito.ico')

def combo():
    lista2=Label(raiz, text="MODELO", font=("Bebas Neue", 22), bg="RoyalBlue3")
    lista2.grid(row=1, column=1,padx=80, pady=10)

    labelTitle.place_forget()
    
    opcion_model=StringVar()
    model=("mod1", "mod2", "mod3")

    opcion_model_tipo=StringVar()
    model_tipo=("modelo1", "modelo2", "modelo4", "modelo5")

    combobox3=ttk.Combobox(raiz, width=30, textvariable=opcion_model, values=model)
    combobox3.current(0)
    combobox3.grid(row=1, column=2)
    
    combobox3_1=ttk.Combobox(raiz, width=30, textvariable=opcion_model_tipo, values=model_tipo)
    combobox3_1.current(0)
    combobox3_1.grid(row=1, column=3)

    lista1=Label(raiz, text="TIPO", font=("Bebas Neue", 22), bg="RoyalBlue3")
    lista1.grid(row=3, column=1,padx=80, pady=10)

    opcion_tipo=StringVar()
    alterTipo=("Indiel", "Valeo", "Audi")

    combobox=ttk.Combobox(raiz, width=30, textvariable=opcion_tipo, values=alterTipo)
    combobox.current(0)
    combobox.grid(row=3, column=2)

    lista2=Label(raiz, text="MARCA", font=("Bebas Neue", 22), bg="RoyalBlue3")
    lista2.grid(row=4, column=1,padx=80, pady=10)

    opcion_marca=StringVar()
    marca=("Luces bajas", "Luces altas", "Guiños", "Auxiliares", "Stop", "Marcha Atrás")

    combobox2=ttk.Combobox(raiz, width=30, textvariable=opcion_marca, values=marca)
    combobox2.current(0)
    combobox2.grid(row=2, column=2)

    lista2=Label(raiz, text="AÑO", font=("Bebas Neue", 22), bg="RoyalBlue3")
    lista2.grid(row=2, column=1,padx=80, pady=10)

    opcion=StringVar()
    anio=("1990-95", "1996-00", "2001-05", "2006-2010", "2011-15", "2016-2022")

    combobox4=ttk.Combobox(raiz, width=30, textvariable=opcion, values=anio)
    combobox4.current(0)
    combobox4.grid(row=4, column=2)

    cuadro_añadir = LabelFrame(raiz, width=7, height=4, bg="snow", bd=".5px")
    cuadro_añadir.place(x=650, y=450)

    ##labelPedir = Label(cuadro_añadir, text="Añadir al pedido", width=15, height=4, bg="gray75", font=("", 9))
    ##labelPedir.pack()

    botonPedir = Button(cuadro_añadir, text="Añadir al pedido", width=15, height=4, bg="medium sea green")
    botonPedir.pack()
    contador = IntVar()
    contador= 0
    botonCarrito = Button(raiz, text=contador, width=6, height=2, bg="snow", font=("", 14))
    botonCarrito.place(x=24, y=700)

def arranque():
    botonAlter.grid_forget()
    imgAlter.place_forget()
    imgArr.place_forget()
    imgLuc.place_forget()
    botonLuces.grid_forget()

    botonArranque.grid_forget()

    botonAtras = Button(raiz, text="<-", width=10, height=2, bg="snow")
    botonAtras.place(x=1350, y=700)

    labelPedidoActual = Label(raiz, text="CATALOGO PARA MOTOR DE ARRANQUE", width=30, height=1, bg="RoyalBlue3", font=("Bebas Neue", 28), fg="IndianRed3")
    labelPedidoActual.grid(row=0, column=2, pady=50, padx=180)

    combo()

def alter():
    botonAlter.grid_forget()
    botonLuces.grid_forget()
    botonArranque.grid_forget()
    imgAlter.place_forget()
    imgArr.place_forget()
    imgLuc.place_forget()
    botonAtras = Button(raiz, text="<-", width=10, height=2, bg="snow")
    botonAtras.place(x=1350, y=700)
   
    labelPedidoActual = Label(raiz, text="CATALOGO PARA ALTERNADOR", width=30, height=1, bg="RoyalBlue3", font=("Bebas Neue", 28), fg="IndianRed3")
    labelPedidoActual.grid(row=0, column=2, pady=50, padx=180)
    combo()
   

def luces():
    botonAlter.grid_forget()
    botonLuces.grid_forget()
    botonArranque.grid_forget()
    imgAlter.place_forget()
    imgArr.place_forget()
    imgLuc.place_forget()
    botonAtras = Button(raiz, text="<-", width=10, height=2, bg="snow")
    botonAtras.place(x=1350, y=700)
  
    
    labelPedidoActual = Label(raiz, text="CATALOGO PARA LUCES", width=30, height=1, bg="RoyalBlue3", font=("Bebas Neue", 28), fg="IndianRed3")
    labelPedidoActual.grid(row=0, column=2, pady=50, padx=180)

    combo()
   
img_alter= PhotoImage(file="PROYECTO_FINAL/assets/alternador.png")
img_arr= PhotoImage(file="PROYECTO_FINAL/assets/arranque.png")
img_faro= PhotoImage(file="PROYECTO_FINAL/assets/faro.png")

labelTitle = Label(raiz, text="SELECCIONE EL TIPO DE PRODUCTO", font=("Bebas Neue", 44), bg="RoyalBlue3", fg="IndianRed3")
labelTitle.place(x=390, y=30)

imgArr=Label(raiz, image=img_arr, bg="RoyalBlue3")
imgArr.place(x=840, y=140)

imgAlter=Label(raiz, image=img_alter, bg="RoyalBlue3")
imgAlter.place(x=840, y=350)

imgLuc=Label(raiz, image=img_faro, bg="RoyalBlue3", width=300, height=150)
imgLuc.place(x=820, y=560)

botonArranque = Button(raiz,text="MOTOR DE ARRANQUE", bg="IndianRed3", command=arranque, font=("Bebas Neue", 23), width=30)
botonArranque.grid(row=1, column=0, pady=160, padx=140)

botonAlter = Button(raiz,text="ALTERNADOR",  bg="IndianRed3", command=alter, font=("Bebas Neue", 23), width=30)
botonAlter.grid(row=2, column=0, padx=140)


botonLuces = Button(raiz, text="LUCES", bg="IndianRed3", command=luces, font=("Bebas Neue", 23), width=30)
botonLuces.grid(row=3, column=0, pady=150, padx=140)




raiz.mainloop()