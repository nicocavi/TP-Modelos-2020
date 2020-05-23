import numpy as np
import pandas as pd
from tkinter import Tk, Label, Button
from views.windows import VentanaMain

clientes_llegada = np.array([[10,0.1],[20,0.1],[30,0.5],[40,0.2],[50,0.1]])

tareas = ['Consulta', 'Compra apps menores', 'Instalacion SO', 'Ajuste apps menores', 'Ajuste SO']
tareas_data = np.array([[5,0.2],[12,0.3],[45,0.2],[12,0.2],[30,0.1]])

cl = pd.DataFrame(clientes_llegada, columns=['Tiempo(min)', 'Probabilidad'])

td = pd.DataFrame(tareas_data, index=tareas, columns=['Tiempo de servicio', 'Probabilidad'])


print(cl.to_string(index=False))
print(td)



root = Tk()
miVentana = VentanaMain(root)
root.mainloop()
