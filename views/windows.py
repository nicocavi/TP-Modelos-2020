from tkinter import Tk, Label, Button, Spinbox

class VentanaMain:
    def __init__(self, master):
        self.master = master
        master.title("PC YA!")
        self.etiqueta = Label(master, text="Clientes:")
        self.etiqueta.grid(row=0, column=0)
        self.botonSaludo = Spinbox(master, from_=0, to=1, increment=0.1 )
        self.botonSaludo.grid(row=0, column=1)
        self.botonCerrar = Button(master, text="Cerrar", command=master.quit)
        self.botonCerrar.grid(row=0, column=2)
    def saludar(self):
    	print("hey")