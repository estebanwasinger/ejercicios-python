# 1.2.1.20. Cantidades, promedios y porcentajes
# Dificultad: básica, Requerido: Indispensable.
# Se ingresan varios valores numéricos enteros, finalizando la carga de datos al ingresar
# un 0 (cero). Se pide informar:
# 1. Cantidad positivos.
# 2. Cantidad de negativos.
# 3. Porcentaje de pares.
# 4. Promedio de los positivos.
# 5. Porcentaje de negativos.
from utils import read_int

num = read_int("Ingrese un número: \n")

cantPositivos : int = 0
totalPositivos : int = 0
negativos : int = 0
pares : int = 0

while num != 0:

    if(num % 2 == 0):
        pares += 1

    if(num > 0):
        cantPositivos = cantPositivos + 1
        totalPositivos += num
    else:
        negativos = negativos + 1
    num = read_int("Ingrese un número:\n")

print("Resultados:")
print("===============================")
print("Cantidad positivos: " + str(cantPositivos))
print("Cantidad negativos: " + str(negativos))
print("Porcentajes de pares: % " + str((pares / (cantPositivos + negativos)) * 100))
print("Promedio de positivos: " + str(totalPositivos / cantPositivos))
print("Porcentaje de negativos: % " + str((negativos / (cantPositivos + negativos)) * 100))
print("===============================")
