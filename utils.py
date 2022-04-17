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