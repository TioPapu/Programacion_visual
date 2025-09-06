"""
def true():
    pass\
"""
# SyntaxError: invalid syntax

#is=4

# SyntaxError: invalid syntax

a = list("letras")
print(a)

"""
def list():
    print("funcion list")

a = list("letras")\
"""
# TypeError: list() takes 0 positional arguments but 1 was given

import keyword
print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

lenguaje = "Python"

if lenguaje == "Python":
    print("Estoy de acuerdo, Python es el mejor")
elif lenguaje == "java":
    print("Nome gusta, Java no mola")
else: 
    print("Ningun otro lenguaje supera Python")


x=0
while x<0:
    print(x)
    x+=1

for i in range(3):
    print(i)

i=0

for i in range(3):
    if i==1:
        continue
    print(i)


x=0 
while True:
    print(x)
    if x==3:
        break
    x += 1

x = (5==10)
print(x)

x=True
if x:
    print("Python")

def funcion():
    return 5
print("La funcion devuelve:", funcion())

def mi_funcion():
    pass
print(mi_funcion())
#salida: None

print(True and False)
print(True or False)
print(not True)

def funcion_suma(a, b):
    print("La suma es:", a+b)


funcion_suma(3, 5)


def funcion_suma_return(a,b):
    return a + b

suma=funcion_suma_return(3, 5)

print("La suma es:",suma)

def funcion_suma_pass(a, b):
    pass


i=0
def generador():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

for i in generador():
    print(i)    


class Miclase:
    def _init_(self):
        print("Creando objeto de mi clase")
objeto = Miclase()

x = "10"
valor= None
try:
    valor = int(x)
except Exception as e:
    print("Hubo un error:", e)   
finally:
    print("El valor es:", valor)

a=0 
def suma_uno():
    global a
    a = a +1

suma_uno()
print(a)

def funcion_a():
    x=10
    def funcion_b():
        nonlocal x
        x=20
        print("Funcion b:", x)
    funcion_b()
    print("Funcion a:", x)
funcion_a()

from collections import namedtuple

lista = ["a", "b", "c"]
print("a" in lista )

a= [1, 2]
b= [1, 2]
c= a   
print(a is b)
print(a is c)


a = 10
del a
# print(a)
# NameError: name 'a' is not defined

"""
with open('fichero.txt', 'r') as file:
    print(file.read())
"""

import asyncio

async def proceso(id_proceso):
    print("Empieza proceso:", id_proceso)
    await asyncio.sleep(10)
    print("Acaba proceso:", id_proceso)

async def main():
    await asyncio.gather(proceso(1), proceso(2), proceso(3))

asyncio.run(main())

# Salida:
# Empieza proceso: 1
# Empieza proceso: 2
# Empieza proceso: 3
# Acaba proceso: 1
# Acaba proceso: 2
# Acaba proceso: 3










