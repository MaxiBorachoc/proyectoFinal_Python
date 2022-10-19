from tkinter import *
from tkinter import ttk
from tkinter import messagebox

raiz = Tk()
raiz.resizable(False, False)
raiz.title("¡A JUGAR!")
raiz.iconbitmap('TP_2/assets/soccer-ball_39433.ico')


miImage=PhotoImage(file="TP_2/assets/thumb_futbol-protocolo-deportes-49.png")

miFrame=Frame(raiz, width=850, height=460)
miFrame.pack()

imgLabel=Label(raiz, image=miImage)
imgLabel.place(x=0, y=0)

alquiler=LabelFrame(raiz, text="Alquiler:", width=380, height=200)
alquiler.place(x=5, y=10)
alquiler.config(bg="DarkSeaGreen1")

f5=Checkbutton(alquiler, text="Fútbol 5")
f5.grid(row=0, column=1, padx=4, pady=4)

f7=Checkbutton(alquiler, text="Fútbol 7")
f7.grid(row=0, column=2)

f11=Checkbutton(alquiler, text="Fútbol 11")
f11.grid(row=0, column=3)

textCancha=Entry(alquiler)
textCancha.grid(row=1, column=1, padx=5)

tipodeCancha=Label(alquiler, text="Sintetico o Natural:")
tipodeCancha.grid(row=1, column=0, padx=1)

textPelotas=Entry(alquiler)
textPelotas.grid(row=1, column=3)

tipodePelota=Label(alquiler, text="Pique o Medio Pique:")
tipodePelota.grid(row=1, column=2, padx=5, pady=10)

opcion=StringVar()
turnos=("15:00", "15:30", "16:00", "16:30", "17:00", "17:30","18:00", "18:30", "19:00", "19:30", "20:00", "20:30")

combobox=ttk.Combobox(alquiler, width=10, textvariable=opcion, values=turnos)
combobox.current(0)
combobox.grid(row=2, column=1)

horarios=Label(alquiler, text="Horarios de los turnos")
horarios.grid(row=2, column=0, pady=5, padx=10)
horarios.config("justify")

def bSalir():
    alquiler.destroy()

def bAceptar():
    messagebox.showinfo("Alquier", "¡Solicitud realizada!")

botonSalir=Button(alquiler, text="Salir", command=bSalir)
botonSalir.grid(row=3, column=1)
botonSalir.config(bg="tan1")

botonAceptar=Button(alquiler, text="Aceptar", command=bAceptar)
botonAceptar.grid(row=3, column=2, padx=0)
botonAceptar.config(bg="tan1")






raiz.mainloop()