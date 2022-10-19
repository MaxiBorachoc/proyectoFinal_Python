from tkinter import *

raiz = Tk()
raiz.geometry('1500x800')
raiz.title("CATALOGO DE PRODUCTOS")
raiz.resizable(False, False)

botonCatalogo = Button(raiz,text="VER CATÁLOGO", width=30, height=5)
botonCatalogo.grid(row=0, column=0, pady=300, padx=180)


botonUltPedido = Button(raiz,text="ÚLTIMO PEDIDO", width=30, height=5)
botonUltPedido.grid(row=0, column=1, pady=300)

labelPedidoActual = Label(raiz, text="PEDIDO ACTUAL VACÍO")
labelPedidoActual.grid(row=0, column=2, pady=300, padx=180)
##botonPedidoActual = Button(raiz,text="PEDIDO ACTUAL", width=30, height=5)
##botonPedidoActual.grid(row=0, column=2, pady=300, padx=180)


raiz.mainloop()