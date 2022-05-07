# 1.2.1.22. Primeros múltiplos flexible
# Dificultad: básica, Requerido: Indispensable.
# Dados tres valores numéricos enteros positivos: n, a y b, informar el n-ésimo múltiplo
# de a que no es múltiplo de b.
# Por ejemplo: si n=10, a=5, b=3 entonces el n-ésimo múltiplo de 5 que no es
# múltiplo de 3 es: 70; y surge de la siguiente lista:
# Múltiplos de 5 = { 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70 }

from utils import read_int

multiplosDe = read_int("Ingrese el número al cual buscar múltiplos: ")
canMultiplos = read_int("Ingrese cuantos multiplos buscar: ")
noMultiplosDe = read_int("Ingrese el número del cual no buscar multiplos: ")

cantMultiplesEncontrados : int = 0
i : int = 1

if noMultiplosDe % multiplosDe:
    print(f"Imposble encontrar múltiplos de {multiplosDe} que no sean múltiplos de {noMultiplosDe}, ya que {noMultiplosDe} es divisor de {multiplosDe}")

else:
    print(f"Estos son los primeros {canMultiplos} multiplos de {multiplosDe} que no son multiplos de {noMultiplosDe}:")
    while cantMultiplesEncontrados < canMultiplos:
        multiplo = i * multiplosDe

        if multiplo % noMultiplosDe != 0:
            cantMultiplesEncontrados += 1
            print(multiplo)

        i += 1

