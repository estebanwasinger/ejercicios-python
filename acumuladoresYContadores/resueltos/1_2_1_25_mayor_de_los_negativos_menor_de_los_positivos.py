# 1.2.1.25. Mayor de los negativos, menor de los positivos
# Dificultad: moderada, Requerido: Indispensable.
# Dado un conjunto de valores numéricos que finaliza con el ingreso de un 0 (cero),
# informar cuál es el mayor de los negativos, y cuál el menor de los positivos.
from utils import read_int

mayorNegativo: int
menorPositivo: int
mayorWasDefined: bool = False
menorWasDefined: bool = False

num = read_int("Ingrese un número: \n")

if num > 0:
    menorPositivo = num
    menorWasDefined = True
elif num < 0:
    mayorNegativo = num
    mayorWasDefined = True
while num != 0:

    if num > 0:
        if menorWasDefined == False or num < menorPositivo:
            menorPositivo = num
            menorWasDefined = True
    else:
        if mayorWasDefined == False or num > mayorNegativo:
            mayorNegativo = num
            mayorWasDefined = True

    num = read_int("Ingrese un número: \n")

if mayorWasDefined:
    print(f"El mayor negativo es: {mayorNegativo}")
else:
    print("No se ingresaron valores negativos")

if menorWasDefined:
    print(f"El menor positivo es: {menorPositivo}")
else:
    print("No se ingresaron valores positivos")
