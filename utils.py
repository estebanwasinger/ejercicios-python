def fact(num: int) -> int:
    factorial: int
    if num == 0:
        factorial = 1
    else:
        factorial = num
        while num != 1 and num > 0:
            factorial = factorial * (num - 1)
            num = num - 1

    return factorial


def read_int() -> int:
    int_value = input()
    return int(int_value)


def read_int(mensaje: str) -> int:
    int_value = input(mensaje)
    return int(int_value)


def read_float() -> float:
    return float(input())


def read_string() -> str:
    return input()
