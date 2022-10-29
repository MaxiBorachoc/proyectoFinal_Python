from tkinter import *


raiz = Tk()
raiz.geometry('1400x800')
raiz.title("CATALOGO DE PRODUCTOS")
raiz.resizable(False, False)
raiz.config(bg="snow")
raiz.iconbitmap('PROYECTO_FINAL/assets/carrito.ico')

img_fondo=PhotoImage(file="PROYECTO_FINAL/assets/fondo.png")

imgArr=Label(raiz, image=img_fondo)
imgArr.place(x=0, y=0)

labelTitle = Label(raiz, text="BIENVENIDO A NUESTRO PORTAL DE VENTA", font=("Bebas Neue", 44), bg="snow", fg="RoyalBlue3")
labelTitle.place(x=370, y=100)
labelSub = Label(raiz, text="INGRESE Y HAGA SU PEDIDO", font=("Bebas Neue", 44), bg="snow", fg="RoyalBlue3")
labelSub.place(x=485, y=600)


botonCatalogo = Button(raiz,text="VER CATÁLOGO", width=30, height=5, bg="RoyalBlue3", font=("Bebas Neue", 19))
botonCatalogo.grid(row=0, column=0, pady=320, padx=140)


botonUltPedido = Button(raiz,text="ÚLTIMO PEDIDO", width=30, height=5, bg="RoyalBlue3", font=("Bebas Neue", 19))
botonUltPedido.grid(row=0, column=1, pady=300)

cuadro = LabelFrame(raiz, width=30, height=5, bg="snow")
cuadro.grid(row=0, column=2, pady=300, padx=160)
labelPedidoActual = Label(cuadro, text="PEDIDO ACTUAL VACÍO", width=30, height=5, bd="1px", bg="RoyalBlue3", font=("Bebas Neue", 19))
labelPedidoActual.pack()

botonPedidoActual = Button(raiz,text="PEDIDO ACTUAL", width=30, height=5, bg="RoyalBlue3", font=("Bebas Neue", 19))
botonPedidoActual.grid(row=0, column=2, pady=300, padx=160)


raiz.mainloop()