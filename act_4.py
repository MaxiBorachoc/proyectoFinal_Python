from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("REPUESTOS")
raiz.geometry("1200x580")

"""-----------------------MENU----------------------------------------"""
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=500, height=500)
archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Guardar pedido")
archivoMenu.add_command(label="Deshacer pedido")
archivoMenu.add_command(label="Cargar pedido")

archivoEdit=Menu(barraMenu, tearoff=0)
archivoEdit.add_command(label="Ver anterior pedido")
archivoEdit.add_command(label="Ver precios")
archivoEdit.add_command(label="Agrandar pantalla")

archivoHelp=Menu(barraMenu, tearoff=0)
archivoHelp.add_command(label="Shortcuts")
archivoHelp.add_command(label="Reportar error")
archivoHelp.add_command(label="Acerca de")

barraMenu.add_cascade(label="Inicio", menu=archivoMenu)
barraMenu.add_cascade(label="Ver", menu=archivoEdit)
barraMenu.add_cascade(label="Ayuda", menu=archivoHelp)

cuaderno1=ttk.Notebook(raiz)
cuaderno1.pack(fill="both", expand="yes")

pag1=Frame(cuaderno1)
pag2=Frame(cuaderno1)
pag3=Frame(cuaderno1)
"""-------------------------------------------------------------------------"""

cuaderno1.add(pag1, text="HOME")
cuaderno1.add(pag2, text="PRODUCTOS")
cuaderno1.add(pag3, text="CONTACTO")


"""-----------------------  PESTAÑA 1----------------------------------------"""
pag1.config(bg="PeachPuff2")

titulo=Label(pag1, text="REPUESTOS", font=("Cascadia Code", 35))
titulo.place(x=490, y=80)
titulo.config(bg="PeachPuff2")

titulo2=Label(pag1, text="REPARACIONES", font=("Cascadia Code", 35))
titulo2.place(x=490, y=180)
titulo2.config(bg="PeachPuff2")

titulo3=Label(pag1, text="AUXILIOS", font=("Cascadia Code", 35))
titulo3.place(x=490, y=280)
titulo3.config(bg="PeachPuff2")

miImage=PhotoImage(file="TP_2/assets/a136684933be5a133673f88b352de0cf.png")
imgLabel=Label(pag1, image=miImage)
imgLabel.place(x=25, y=60)
"""-------------------------------------------------------------------------"""



"""-----------------------  PESTAÑA 2----------------------------------------"""
"""--------------LISTA 1--------------"""
pag2.config(bg="PeachPuff3")
miImage2=PhotoImage(file="TP_2/assets/faro.png")
imgLabel=Label(pag2, image=miImage2)
imgLabel.grid(row=0, column=0, padx=100, pady=10)

lista1=Label(pag2, text="TIPO", font=("Cascadia Code", 18))
lista1.grid(row=0, column=1,padx=10, pady=10)

lista1_2=Label(pag2, text="MODELOS", font=("Cascadia Code", 18))
lista1_2.grid(row=0, column=3,padx=20, pady=10)

opcion=StringVar()
farosTipo=("Luces bajas", "Luces altas", "Guiños", "Auxiliares", "Stop", "Marcha Atrás")

opcion_1=StringVar()
mod=("Peugeot", "Volkswagen", "Fiat","Toyota","Chevrolet","Hyundai", "Ford")

combobox=ttk.Combobox(pag2, width=10, textvariable=opcion, values=farosTipo)
combobox.current(0)
combobox.grid(row=0, column=2)

combobox=ttk.Combobox(pag2, width=10, textvariable=opcion_1, values=mod)
combobox.current(0)
combobox.grid(row=0, column=4)

def bFaro():
    botonFaro.config(bg="lime green")
    botonFaro.config(text="PEDIDO REALIZADO")
    opciones="Tipo: "+str(opcion.get())+" | Modelo: " + str(opcion_1.get())
    pedido=Label(pag2, text=opciones, bg="PeachPuff3")
    pedido.grid(row=0, column=6)


botonFaro=Button(pag2, text="PEDIR", command=bFaro)
botonFaro.grid(row=0, column=5, padx=15)


"""-----------------------------------"""
"""--------------LISTA 2--------------"""
miImage3=PhotoImage(file="TP_2/assets/arranque.png")
imgLabel=Label(pag2, image=miImage3)
imgLabel.grid(row=1, column=0, pady=10, padx=100)

lista2=Label(pag2, text="TIPO", font=("Cascadia Code", 18))
lista2.grid(row=1, column=1,padx=10, pady=10)

lista2_1=Label(pag2, text="MODELOS", font=("Cascadia Code", 18))
lista2_1.grid(row=1, column=3,padx=10, pady=10)

opcion2=StringVar()
opcion2_1=StringVar()
marca=("Valeo", "Indiel", "Audi")
mod=("Peugeot", "Volkswagen", "Fiat","Toyota","Chevrolet","Hyundai", "Ford")

combobox=ttk.Combobox(pag2, width=10, textvariable=opcion2, values=marca)
combobox.current(0)
combobox.grid(row=1, column=2)

combobox=ttk.Combobox(pag2, width=10, textvariable=opcion2_1, values=mod)
combobox.current(0)
combobox.grid(row=1, column=4)

def bArr():
    botonArr.config(bg="lime green")
    botonArr.config(text="PEDIDO REALIZADO")
    opciones="Tipo: "+str(opcion2.get())+" | Modelo: " + str(opcion2_1.get())
    pedido=Label(pag2, text=opciones, bg="PeachPuff3")
    pedido.grid(row=1, column=6)

botonArr=Button(pag2, text="PEDIR", command=bArr)
botonArr.grid(row=1, column=5, padx=15)

"""-----------------------------------"""
"""--------------LISTA 3--------------"""
miImage4=PhotoImage(file="TP_2/assets/alter.png")
imgLabel=Label(pag2, image=miImage4)
imgLabel.grid(row=2, column=0, pady=10, padx=100)

lista3=Label(pag2, text="TIPO", font=("Cascadia Code", 18))
lista3.grid(row=2, column=1,padx=10, pady=10)

lista3_1=Label(pag2, text="MODELOS", font=("Cascadia Code", 18))
lista3_1.grid(row=2, column=3,padx=10, pady=10)

opcion3=StringVar()
opcion3_1=StringVar()
marca=("Valeo", "Indiel", "Audi")
mod=("Peugeot", "Volkswagen", "Fiat","Toyota","Chevrolet","Hyundai", "Ford")

combobox=ttk.Combobox(pag2, width=10, textvariable=opcion3, values=marca)
combobox.current(0)
combobox.grid(row=2, column=2)

combobox=ttk.Combobox(pag2, width=10, textvariable=opcion3_1, values=mod)
combobox.current(0)
combobox.grid(row=2, column=4)

def bAlter():
    botonAlter.config(bg="lime green")
    botonAlter.config(text="PEDIDO REALIZADO")
    opciones="Tipo: "+str(opcion3.get())+" | Modelo: " + str(opcion3_1.get())
    pedido=Label(pag2, text=opciones, bg="PeachPuff3")
    pedido.grid(row=2, column=6)

botonAlter=Button(pag2, text="PEDIR", command=bAlter)
botonAlter.grid(row=2, column=5, padx=15)

"""-----------------------------------"""
"""-----------------------PESTAÑA 3----------------------------------------"""
pag3.config(bg="PeachPuff4")

contact=Label(pag3, text="CONTACTATE CON NOSOTROS", font=("Cascadia Code", 32), bg="PeachPuff4")
contact.place(x=300, y=50)

mail=LabelFrame(pag3, text="Contacto", bg="PeachPuff4")
mail.place(x=370, y=120)

nombre=Label(mail, text="Nombre: ", bg="PeachPuff4")
nombre.grid(row=0, column=0, padx=15, pady=10)

nombreCaja=Entry(mail, width=30)
nombreCaja.grid(row=0, column=1, padx=15, pady=10)

email=Label(mail, text="E-mail: ", bg="PeachPuff4")
email.grid(row=1, column=0, padx=5, pady=10)

emailCaja=Entry(mail, width=30)
emailCaja.grid(row=1, column=1, padx=15, pady=10)

msj=Label(mail, text="Mensaje: ", bg="PeachPuff4")
msj.grid(row=2, column=0, padx=15, pady=10)

msjCaja=Text(mail, width=40, height=10)
msjCaja.grid(row=2, column=1, padx=15, pady=20)

def envio():
    enviar.config(text="Mensaje enviado!", bg="light green")

enviar=Button(mail, text="Enviar mensaje", bg="light blue", command=envio)
enviar.grid(row=3, column=1, pady=10)





"""-------------------------------------------------------------------------"""
raiz.mainloop()