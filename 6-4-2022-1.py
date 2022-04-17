# Dados dos valores numéricos enteros, informar su producto calculándolo
# mediante sumas sucesivas.
# 1. Considerando que los valores ingresados serán números positivos o cero.
# 2. Considerando que los valores ingresados también podrían ser negativos.

print("Ingrese un numero")
a: int = int(input())

print("otro numeritooooo, el anterior no me gusto")
b: int = int(input())

n = 0
suma = 0
while n < b:
    n = n + 1
    suma = suma + a

print(suma)

