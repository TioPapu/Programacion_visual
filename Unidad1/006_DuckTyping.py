class pato:
    def hablar(self):
        print("¡Cua! ¡Cua!")

p = pato()
p.hablar()  


def llama_hablar(x):
    x.hablar()

llama_hablar(p)

class perro:
    def hablar(self):
        print("¡Guau! ¡Guau!")  

class gato:
    def hablar(self):
        print("¡Miau! ¡Miau!")

class vaca:
    def hablar(self):
        print("¡Muu! ¡Muu!")


llama_hablar(perro())
llama_hablar(gato())
llama_hablar(vaca())


lista=[pato(), perro(), gato(), vaca()]
for animal in lista:
    llama_hablar(animal)

class Foo():
    def __len__(self):
        return 99
    
class Bar():
    pass

print(len(Foo())) # 99
#print(len(Bar())) # Error

print(3*3)   # 9
print(3*"3") # 333