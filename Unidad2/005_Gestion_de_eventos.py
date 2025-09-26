#Practica 1---------------------------------------------------------------

import tkinter as tk

root = tk.Tk()
root.title("Control Salidas Digitales")

estados = [False, False, False, False]
labels = []

for i in range(4):
    def cambiar_estado(idx=i):
        estados[idx] = not estados[idx]
        labels[idx].config(text="ENCENDIDO" if estados[idx] else "APAGADO")
    
    tk.Button(root, text=f"Salida {i+1}", command=cambiar_estado).grid(row=i, column=0)
    label = tk.Label(root, text="APAGADO", bg="red")
    label.grid(row=i, column=1)
    labels.append(label)

root.mainloop()


#Practica 2 -------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Monitor Sensorial")

def verificar():
    try:
        valor = float(entry.get())
        label_valor.config(text=f"Valor: {valor}°C")
        
        if 10 <= valor <= 80:
            label_estado.config(text="Rango SEGURO", bg="green")
        else:
            label_estado.config(text="FUERA de Rango", bg="red")
            messagebox.showwarning("Alerta", "¡Valor peligroso detectado!")
    except:
        messagebox.showerror("Error", "Ingrese un número válido")

entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Verificar", command=verificar).pack()
label_valor = tk.Label(root, text="Valor: --")
label_valor.pack()
label_estado = tk.Label(root, text="Estado: Desconocido")
label_estado.pack()

root.mainloop()


#Practica 3 --------------------------------------------------------------------------------------

import tkinter as tk

root = tk.Tk()
root.title("Acceso IoT")

def verificar():
    if entry.get() == "iot2025":
        label.config(text="Acceso CONCEDIDO", bg="green")
    else:
        label.config(text="Acceso DENEGADO", bg="red")

tk.Label(root, text="Clave de acceso:").pack()
entry = tk.Entry(root, show="*")
entry.pack()
tk.Button(root, text="Verificar", command=verificar).pack()
label = tk.Label(root, text="Esperando verificación...")
label.pack()

root.mainloop()



#Práctica 4----------------------------------------------------------------------------------------


import tkinter as tk

root = tk.Tk()
root.title("Modo de Operación")

modo = tk.StringVar(value="Manual")

def actualizar():
    label.config(text=f"Modo seleccionado: {modo.get()}")

for texto, valor in [("Manual", "Manual"), ("Automático", "Automatico"), ("Mantenimiento", "Mantenimiento")]:
    tk.Radiobutton(root, text=texto, variable=modo, value=valor, command=actualizar).pack()

label = tk.Label(root, text="Modo seleccionado: Manual")
label.pack()

root.mainloop()


#Practica 5-----------------------------------------------
import tkinter as tk
import random

root = tk.Tk()
root.title("Monitor de Red")

estados = ["En línea", "Desconectado", "Alerta"]

def consultar():
    label.config(text=random.choice(estados))

tk.Button(root, text="Consultar estado", command=consultar).pack()
label = tk.Label(root, text="Presione consultar")
label.pack()

root.mainloop()