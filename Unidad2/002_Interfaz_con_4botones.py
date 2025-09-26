
import tkinter as tk
from tkinter import messagebox


def manejar_boton(numero_dispositivo):
    
    respuesta = messagebox.askyesno("Confirmar acción",
                                    f"¿Deseas activar el dispositivo {numero_dispositivo}?")
    if respuesta:
       
        messagebox.showinfo("Acción realizada",
                            f"Dispositivo {numero_dispositivo} activado correctamente.")
    else:
       
        messagebox.showinfo("Acción cancelada",
                            f"No se activó el dispositivo {numero_dispositivo}.")


ventana = tk.Tk()
ventana.title("Control Electrónico (Simulación)")
ventana.geometry("350x250")

boton1 = tk.Button(ventana, text="Activar Dispositivo 1",
                   command=lambda: manejar_boton(1))
boton1.pack(pady=10)

boton2 = tk.Button(ventana, text="Activar Dispositivo 2",
                   command=lambda: manejar_boton(2))
boton2.pack(pady=10)

boton3 = tk.Button(ventana, text="Activar Dispositivo 3",
                   command=lambda: manejar_boton(3))
boton3.pack(pady=10)

boton4 = tk.Button(ventana, text="Activar Dispositivo 4",
                   command=lambda: manejar_boton(4))
boton4.pack(pady=10)

ventana.mainloop()