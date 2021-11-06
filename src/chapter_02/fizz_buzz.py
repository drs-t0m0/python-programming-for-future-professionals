def fizz_buzz(n: int) -> str:
    if n % 15 == 0:
        return "Fizz Buzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


if __name__ == '__main__':
    print(fizz_buzz(1))
    print(fizz_buzz(2))
    print(fizz_buzz(3))
    print(fizz_buzz(4))
    print(fizz_buzz(5))
    print(fizz_buzz(6))
    print(fizz_buzz(7))
    print(fizz_buzz(8))
    print(fizz_buzz(9))
    print(fizz_buzz(10))
    print(fizz_buzz(11))
    print(fizz_buzz(12))
    print(fizz_buzz(13))
    print(fizz_buzz(14))
    print(fizz_buzz(15))
