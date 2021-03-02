from my_libs.my_funcs import perfect_square


def fermat(n):
    """
    Fattorizzazione metodo Fermat
    :param n: n deve essere dispari
    :return: x, y: tale che n = x²-y² = (x-y)² × (x+y)²
    """
    assert n % 2 == 1
    k = int(n ** (1 / 2))
    if perfect_square(n):
        x = k
        y = 0
        return x, y
    while True:
        k += 1
        y_sqr = k ** 2 - n
        if perfect_square(y_sqr):
            print(k - int(n ** (1 / 2)) + 1, "passi")
            x = k
            y = int(y_sqr ** (1 / 2))
            return x, y


if __name__ == '__main__':
    print(fermat(13111))
