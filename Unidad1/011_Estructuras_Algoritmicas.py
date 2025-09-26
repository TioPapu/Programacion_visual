#1 Control de temperatura en un microcontrolador
estadoVenti=False
while True:
    sensor=input("Introduce la temperatura del sensor en °C:")
    tempe=sensor
    if tempe=='KILL': quit()   ###KILL CODE 

    if tempe >'70':
        estadoVenti=True
        print(f"Ventilador Encendido. Temp= {tempe}°C")
    else: 
        if tempe <'65':
            estadoVenti=False
            print(f"Ventilador Apagado. Temp= {tempe}°C")


#2 Revisión de Voltaje de Baterías
baterias=[]
k=3
while k<=3:
    for i in range(5):
        bateria=input(f"Introduce el valor del voltage de la bateria {i}: ")
        baterias.append(bateria)
    
    for j in range(5):
        if baterias[j]<'3.3':
            print(f"Bateria {j}  baja")
        elif baterias[j]>='4.0':
                print(f"Bateria {j}  Optima")
        else:
            print(f"Bateria {j}  ADVERTENCIA")
    k+=1


#3 Contador de Señales Digitales Recibidas
señal=0
registro=[]
while True:
    bajas=0
    altas=0
    for i in range(20):
        señal=input("Introduce la señal en 0 o 1:")
        if señal=='1': 
            altas+=1
            print(f"a={altas}")
        if señal=='0': 
            bajas+=1
            print(f"b={bajas}")
    if altas>bajas:
        print("Alto flujo de datos")
    break


