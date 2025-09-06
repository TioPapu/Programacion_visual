a, b, c = [1, 2, 3]
print(a) # 1
print(b) # 2
print(c) # 3

a, b, c = (1, 2, 3)
print(a) # 1
print(b) # 2
print(c) # 3


#a, b, c = (1, 2) # Error: ValueError: not enough values to unpack (expected 3, got 2)

#a, b = (1, 2, 3, 4) # Error: ValueError: too many values to unpack (expected 2) 


a, b, c = "123"
print(a) # 1
print(b) # 2
print(c) # 3



a, b, c = {'uno': 1, 'dos':2, 'tres': 3}
print(a) # uno
print(b) # dos
print(c) # tres

a, b, c= {'uno': 1, 'dos': 2, 'tres': 3}.values()
print(a)
print(b)
print(c)

a, b, c = range(3)
print(a) # 0
print(b) # 1
print(c) # 2

*a, b= [1, 2, 3]
print(a)
print(b)

a, *b =[1, 2, 3]
print(a)
print(b)

a=[1, 2]
b=[3, 4]
c=[*a, *b]
print(c)


a={'uno': 1, 'dos': 2}
b={'tres': 3, 'cuatro': 4}
c={**a, **b}
print(c)    

a = {"uno": 1, "dos": 2}
b = {"uno": 0, "dos": 0}

c = {**a, **b}

print(c)
# {'uno': 0, 'dos': 0}


for primero, *resto in [{"a": 1, "b": 2, "c": 3}, {"a": 4, "b": 5, "c": 6}]:
    print(primero)
    print(resto)


a,b = 1, 2
print(a, b)
a, b = b,a
print(a, b)

def funcion(a, *args, **kwargs):
    print(f"a={a}, args={args}, kwargs={kwargs}")

funcion(1)
funcion(1, 2)
funcion(1, 2, 3, cuatro=4, cinco =5)


