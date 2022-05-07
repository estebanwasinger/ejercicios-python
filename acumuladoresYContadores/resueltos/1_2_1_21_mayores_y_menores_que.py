# 1.2.1.21. Mayores y menores que
# Dificultad: básica, Requerido: Indispensable.
# Dados 10 valores numéricos enteros, que se ingresan de a uno por vez, se pide
# informar el promedio de los mayores que 100, y la suma de los menores que -10.

from utils import *

cantNumerosMayores100 : int = 0
sumMayores100 : int = 0
sumMenoresMenos10 : int = 0

for n in range(10):
    num = read_int("Ingrese un número: ")
    if num > 100:
        cantNumerosMayores100 += 1
        sumMayores100 += num
    elif num < -10:
        sumMenoresMenos10 += num

promedioMayoresA100 : float = 0

if cantNumerosMayores100 == 0:
    promedioMayoresA100 = 0
else:
    promedioMayoresA100 = sumMayores100 / cantNumerosMayores100
print("Resultados:")
print("===============================")
print("Promedio mayores a 100: " + str(promedioMayoresA100))
print("Sum menores a -10: " + str(sumMenoresMenos10))
print("===============================")
