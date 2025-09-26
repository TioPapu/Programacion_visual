# 1 Monitoreo de sensores de temperatura
 
temps=[]
tempe=0
conta=0
for i in range(1,9):
    tempe=float(input(f"INGRESE LA TEMPERATURA DEL SENSOR {i}  :"))
    temps.append(tempe)
    print(temps)

for i in range(1,9):
    if temps[i-1]>60:
        print(f"Sensor {i} = {temps[i-1]}°C")
        conta +=1


print(f"La cantidad de sensores que superan 60°C es: {conta}")


#Validacion de clave de acceso
clave=[1,2,3,4,5]
hash=[]
conta=0
aciertos=0
for i in range(1,4):
    aciertos=0
    for j in range(1,5):
        digito=int(input(f"Ingrese el digito {j} de la clave:"))
        hash.append(digito)

    for k in range(1,5):
        if hash[k-1]  != clave[k-1]:
            print(f"clave erronea")
            conta += 1
            hash.clear()
            break
        else:
            aciertos +=1
            if aciertos ==4:
                print("CLAVE CORRECTA")
                hash.clear()
                exit()
    if conta >= 3:
        print("ALARMA ACTIVADA")
   

#3 Adquisición y procesamiento de señales analógicas
muestras=[]
for i in range(1,13):
    muestra=float(input(f"Ingrese la muestra {i}: "))
    muestras.append(muestra)
    print(muestras)
promedio=sum(muestras)/12
if promedio >3.3:
    print(f"Alerta Sobrevoltaje: {promedio}V")
else:
    print(f"Voltaje normal: {promedio}V")

#4 Registro de estados digitales
estados=[]
for i in range(1,11):
    estado=int(input(f"Ingrese el estado del boton {i} (0 o 1): "))
    estados.append(estado)
    print(estados)

def botones_presionados(estados):
    presionados=[]
    for j in range(1,11):
        if estados[j-1]==1:
            presionados.append(j)
    return presionados

print(f"Botones presionados: {botones_presionados(estados)}")



#5 Mapeo de sensores por posición y tipo

def crear_mapa_de_sensores():
    sensores=[]
    print("Tipos de sensor: 1=Térmico, 2=Luminoso, 3=Digital")
    for i in range(1,5):
        for j in range(1,4):
            tipo=input(f"Ingrese el numero de tipo de sensor en la posicion ({i},{j}): ")
            sensores.append((i,j,tipo))
    return sensores

sensor = 0
mapa = []
for i in range(4):  
    fila = []      
    for j in range(3):  
        sensor += 1
        fila.append(sensor)  
    mapa.append(fila)       
print("Mapa de sensores:")
for fila in mapa:
    print(fila)

def mostar_ubicacionytipo(sensores, mapa):
    consulta=input("Ingrese el numero de sensor a consultar (1 - 12): ")
    for i in range(4):       
        for j in range(3): 
            if mapa[i][j]==int(consulta):
                print(f"El sensor {consulta} está en la posición ({i+1},{j+1}) y es de tipo {sensores[int(consulta)-1][2]}")
    


sensores=crear_mapa_de_sensores()

consulta=mostar_ubicacionytipo(sensores,mapa)






