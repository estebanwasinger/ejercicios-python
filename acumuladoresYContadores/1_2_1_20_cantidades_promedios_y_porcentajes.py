# 1.2.1.20. Cantidades, promedios y porcentajes
# Dificultad: básica, Requerido: Indispensable.
# Se ingresan varios valores numéricos enteros, finalizando la carga de datos al ingresar
# un 0 (cero). Se pide informar:
# 1. Cantidad positivos. *
# 2. Cantidad de negativos. *
# 3. Porcentaje de números pares. *
# 4. Promedio de los positivos. *
# 5. Porcentaje de negativos.

from utils import read_int

num = read_int("Ingrese números enteros. Ingrese 0 para finalizar.")
# Contadores
cantidadPositivos : int = 0
cantidadNegativos : int = 0
cantidadPares : int = 0

#Acumulador
totalPositivos : int = 0

while num != 0:
    if(num % 2 == 0):
        cantidadPares = cantidadPares + 1

    if(num > 0):
        cantidadPositivos = cantidadPositivos + 1
        totalPositivos = totalPositivos + num

    if(num < 0):
        cantidadNegativos = cantidadNegativos + 1

    num = read_int("Ingrese otro número:")

print("La cantidad de positivos es: ")
print(cantidadPositivos)
print("La cantidad de negativos es: ")
print(cantidadNegativos)
print("El porcentaje de pares es:")
print(cantidadPares / (cantidadNegativos + cantidadPositivos) * 100)
print("El promedio de positivos es:")
print(totalPositivos / cantidadPositivos)
print("El porcentaje de negativos es:")
print(cantidadNegativos / (cantidadNegativos + cantidadPositivos) * 100)


