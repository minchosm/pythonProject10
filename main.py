import tkinter
from tkinter import *
from tkinter import ttk
window = Tk()
lista = IntVar()
opcion1 = ttk.Radiobutton(window, text= "opcion 1", variable=lista, value=1).pack()
opcion2 = ttk.Radiobutton(window, text="opción 2", variable=lista, value=2).pack()
opcion3 = ttk.Radiobutton(window, text="Opción 3", variable=lista, value=3).pack()


def resetear():
    lista.set(0)

 
ttk.Button(window, text="Reiniciar", command=lambda: resetear()).pack()
window.mainloop()
