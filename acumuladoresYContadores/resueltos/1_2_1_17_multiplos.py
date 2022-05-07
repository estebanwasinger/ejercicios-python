# 1.2.1.17. Múltiplos
# Dificultad: básica, Requerido: Indispensable.
# Dado un valor numérico entero positivo n, informar los primeros n múltiplos de 5
# que no sean múltiplos de 3.
# Por ejemplo: si n fuera 6, la salida deberá ser: 5, 10, 20, 25, 35, 40.
from utils import read_int

num = read_int("Ingrese un número entero positivo: ")

cantMultiplesEncontrados : int = 0
i : int = 1

print(f"Estos son los primeros {num} multiplos de 5 que no son multiplos de 3:")
while cantMultiplesEncontrados < num:
    multiplo = i * 5

    if multiplo % 3 != 0:
        cantMultiplesEncontrados += 1
        print(multiplo)

    i += 1

