# 1.2.1.17. Múltiplos
# Dificultad: básica, Requerido: Indispensable.
# Dado un valor numérico entero positivo n, informar los primeros n múltiplos de 5
# que no sean múltiplos de 3.
# Por ejemplo: si n fuera 6, la salida deberá ser: 5, 10, 20, 25, 35, 40.

from utils import read_int

n = read_int("Ingrese un número entero positivo: ")

cantMultiplosEncontrados : int = 0
i : int = 1

# Cuando "cantMultiplosEncontrados" sea igual a N hay que cortar
# while cantMultiplosEncontrados < n:
#     print("Se hizo una vuelta")
#     esIMultiplo = i % 5 == 0 # Si I es multiplo o no de 5
#
#     if esIMultiplo:
#         if not (i % 3 == 0):
#             cantMultiplosEncontrados = cantMultiplosEncontrados + 1
#             print(i)
#
#     i = i + 1

while cantMultiplosEncontrados < n:
    print("Se hizo una vuelta")
    multiploDe5 = i * 5 # voy calculando los múltplos


    if not (multiploDe5 % 3 == 0):
        cantMultiplosEncontrados = cantMultiplosEncontrados + 1
        print(multiploDe5)

    i = i + 1

