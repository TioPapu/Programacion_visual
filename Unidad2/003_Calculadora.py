import tkinter as tk

def calcular(operacion):
    try:
        num1 = float(entry_num1.get())  
        num2 = float(entry_num2.get())   

       
        if operacion == "sumar":
            resultado = num1 + num2
        elif operacion == "restar":
            resultado = num1 - num2
        elif operacion == "multiplicar":
            resultado = num1 * num2
        elif operacion == "dividir":
          
            if num2 == 0:
                resultado = "Error: División por cero"
            else:
                resultado = num1 / num2

        
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        
        label_resultado.config(text="Error: Ingresa solo números")


ventana = tk.Tk()
ventana.title("Calculadora Básica")


tk.Label(ventana, text="Primer número:").grid(row=0, column=0, padx=5, pady=5)

entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=0, column=1, padx=5, pady=5)


tk.Label(ventana, text="Segundo número:").grid(row=1, column=0, padx=5, pady=5)

entry_num2 = tk.Entry(ventana)
entry_num2.grid(row=1, column=1, padx=5, pady=5)


btn_sumar = tk.Button(ventana, text="Sumar", command=lambda: calcular("sumar"))

btn_sumar.grid(row=2, column=0, padx=10, pady=10)

btn_restar = tk.Button(ventana, text="Restar", command=lambda: calcular("restar"))

btn_restar.grid(row=2, column=1, padx=10, pady=10)

btn_multiplicar = tk.Button(ventana, text="Multiplicar", command=lambda: calcular("multiplicar"))

btn_multiplicar.grid(row=3, column=0, padx=10, pady=10)

btn_dividir = tk.Button(ventana, text="Dividir", command=lambda: calcular("dividir"))

btn_dividir.grid(row=3, column=1, padx=10, pady=10)

label_resultado = tk.Label(ventana, text="Resultado: ")

label_resultado.grid(row=4, column=0, columnspan=2, padx=5, pady=20)


ventana.mainloop()