#1 Registro de consumo eléctrico por electrodoméstico
electrodomesticos = {}

while True:
    nombre = input("Nombre del electrodomestico: ")
    
    if nombre == 'fin':
        break
    
    consumo = float(input("Consumo en kWh: "))
    electrodomesticos[nombre] = consumo
    


total = 0
for consumo in electrodomesticos.values():
    total += consumo

print(f"Consumo total de la casa: {total} kWh")


for nombre, consumo in electrodomesticos.items():
    porcentaje = (consumo / total) * 100
    
    if porcentaje > 30:
        print(f"{nombre}: {porcentaje:.1f}% (Alto consumo)")
    else:
        print(f"{nombre}: {porcentaje:.1f}%")


#2 Seguimiento de averías eléctricas
averias = []

fecha1 = input("Fecha de la primera averia: ")
tipo1 = input("Tipo de averia: ")
averias.append((fecha1, tipo1))


fecha2 = input("Fecha de la segunda averia: ")
tipo2 = input("Tipo de averia: ")
averias.append((fecha2, tipo2))


mas = input("¿Hay más averías? (s/n): ")
if mas == 's':
    fecha3 = input("Fecha: ")
    tipo3 = input("Tipo: ")
    averias.append((fecha3, tipo3))


contador = {}
for fecha, tipo in averias:
    if tipo not in contador:
        contador[tipo] = 0
    contador[tipo] += 1

print("Resumen:")
for tipo, cantidad in contador.items():
    print(f"{tipo}: {cantidad} veces")

mas_frecuente = ""
max_veces = 0
for tipo, cantidad in contador.items():
    if cantidad > max_veces:
        mas_frecuente = tipo
        max_veces = cantidad

if mas_frecuente:
    print(f"La averia mas comun es: {mas_frecuente}")




#3 Contador de señales digitales recibidas ------------------------------------------------------------------------
señales = []

i = 0
while i < 20:
    señal = input(f"Señal {i+1} (0=baja, 1=alta): ")
    
    if señal == '0' or señal == '1':
        señales.append(señal)
        i += 1
    else:
        print("Solo puede ser 0 o 1")

altas = 0
bajas = 0

for señal in señales:
    if señal == '1':
        altas += 1
    else:
        bajas += 1

print(f"Resultado:")
print(f"Señales altas (1): {altas}")
print(f"Señales bajas (0): {bajas}")

if altas > bajas:
    print("Las señales altas son mas")
else:
    print("Las señales bajas son mas")
 
 
 
#4  Revisión de instalaciones eléctricas por departamento -----------------------------------------------------------------
estados = []

print("Opciones: apto, correcto, reparar")

while True:
    estado = input("Ingrese el estado (o 'fin' para terminar): ")
    
    if estado == 'fin':
        break
    
    if estado == 'apto' or estado == 'correcto' or estado == 'reparar':
        estados.append(estado)
        print("Estado guardado")
    else:
        print("Estado no valido")


contador_reparar = 0
for e in estados:
    if e == 'reparar':
        contador_reparar += 1


print(f"Total: {len(estados)} instalaciones")
print(f"Necesitan reparación: {contador_reparar}")
if contador_reparar > 2:
    print("Alerta! Muchas reparaciones")


#5 Listado único de suministros eléctricos--------------------------------------------------------------------------
suministros = []

suministros.append("cable")
suministros.append("interruptor")
suministros.append("bombillo")
suministros.append("cable")  # duplicado
suministros.append("tomacorriente")
suministros.append("interruptor")  # duplicado

print(f"Lista original: {suministros}")

lista_unica = set(suministros)

print(f"Lista sin duplicados: {lista_unica}")

#6 Historial de interrupciones de energía -----------------------------------------------------------------------------
cortes_por_dia = {}

while True:
    fecha = input("Fecha (DD/MM o 'fin'): ")
    if fecha == 'fin':
        break
    
    inicio = input("Inicio (HH:MM): ")
    fin = input("Fin (HH:MM): ")
    
    h1, m1 = map(int, inicio.split(':'))
    h2, m2 = map(int, fin.split(':'))
    
    duracion = (h2 - h1) + (m2 - m1) / 60
    
    if fecha in cortes_por_dia:
        cortes_por_dia[fecha] += duracion
    else:
        cortes_por_dia[fecha] = duracion
    
    print(f"Agregado: {duracion:.2f} horas el {fecha}\n")

print("resumen por día:")
for fecha, total in cortes_por_dia.items():
    print(f"{fecha}: {total:.2f} horas")
    if total > 3:
        print(" Mucho tiempo sin energía")

total_general = sum(cortes_por_dia.values())
print(f"TOTAL GENERAL: {total_general:.2f} horas")


#7 Agenda de mantenimientos eléctricos-------------------------------------------------------------

agenda = set()

print("Agenda de mantenimientos eléctricos")

agenda.add("15/05/2024")
agenda.add("20/05/2024")
agenda.add("15/05/2024")  

print(f"Fechas únicas: {agenda}")

lista_ordenada = sorted(agenda)
print(f"Agenda ordenada: {lista_ordenada}")

print("\nMantenimientos programados:")
for fecha in lista_ordenada:
    print(f"- {fecha}")


#8 Cálculo de potencia por habitación-------------------------------------------------------------------------

habitaciones = {}

habitacion = "Sala"
dispositivos_sala = [100, 60, 500, 200]  
habitaciones[habitacion] = dispositivos_sala

habitacion = "Cocina" 
dispositivos_cocina = [800, 1200, 150]
habitaciones[habitacion] = dispositivos_cocina

print("Potencias por habitación:")
for habitacion, potencias in habitaciones.items():
    total = sum(potencias)
    print(f"{habitacion}: {total}W")
    
    if total > 1500:
        print("  ALERTA Potencia muy alta")

total_casa = sum(sum(potencias) for potencias in habitaciones.values())
print(f"Potencia total de la casa: {total_casa}W")

#9 Alarmas por fuga eléctrica--------------------------------------------------------------------------------
fugas = {}

print("Registro de fugas eléctricas por fecha")

fecha1 = "15/05/2024"
fecha2 = "16/05/2024"
fecha3 = "15/05/2024"  

for fecha in [fecha1, fecha2, fecha3]:
    if fecha in fugas:
        fugas[fecha] += 1
    else:
        fugas[fecha] = 1

print("Todas las fugas:", fugas)

print("Días con más de una fuga:")
for fecha, cantidad in fugas.items():
    if cantidad > 1:
        print(f"{fecha}: {cantidad} fugas")


#10 Distribución de carga en fases-------------------------------------------------------------------


fase_a = []
fase_b = [] 
fase_c = []


cargas = [10, 15, 20, 25, 30, 5]

for carga in cargas:
    total_a = sum(fase_a)
    total_b = sum(fase_b)
    total_c = sum(fase_c)
    
    menor = min(total_a, total_b, total_c)
    
    if menor == total_a:
        fase_a.append(carga)
        print(f"Carga {carga}A - Fase A")
    elif menor == total_b:
        fase_b.append(carga)
        print(f"Carga {carga}A - Fase B")
    else:
        fase_c.append(carga)
        print(f"Carga {carga}A - Fase C")

print(f"Fase A: {sum(fase_a)}A - {fase_a}")
print(f"Fase B: {sum(fase_b)}A - {fase_b}")
print(f"Fase C: {sum(fase_c)}A - {fase_c}")

promedio = (sum(fase_a) + sum(fase_b) + sum(fase_c)) / 3
if sum(fase_a) > promedio * 1.2:
    print("Fase A sobrecargada")