def saludo():
    mensaje = "¡Hola mundo!"
    print(mensaje)
saludo()
#print(mensaje)  # Error: mensaje no está definido fuera de la función

def funcion_exterior():
    mensaje="¡Hola desde la función exterior!"
    def funcion_interior():
        print(mensaje)
    funcion_interior()
funcion_exterior()

mensaje = "Hola desde el alcance global"  # Variable global

def imprimir_mensaje():
    print(mensaje)  # Accediendo a la variable global

imprimir_mensaje()

print(mensaje)  # También accesible fuera de las funciones


from math import sqrt
a=16

raiz_cuadrada = sqrt(a)
print(f"La raíz cuadrada de {a} es {raiz_cuadrada}")


