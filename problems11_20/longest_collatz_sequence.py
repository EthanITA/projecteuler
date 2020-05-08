#   Longest Collatz sequence

"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import time

start = time.time()

# Problema: definire la regola di Colatz


def colatz(n):
    def __even(n):
        return n // 2

    def __odd(n):
        return 3 * n + 1

    if n % 2 == 0:
        return __even(n)
    else:
        return __odd(n)

    """   
    # Invece di if-else
    return _even(n) * (1 - (n % 2)) + _odd(n) * (n % 2)
    return _even(n) - ((n % 2) * _even(n)) + (_odd(n) * n % 2)
    return _even(n) + (n % 2) * (_odd(n) - _even(n)) 
    """


# Problema: funzione che genera la sequenza di Colatz partendo da n

def colatz_generator(n):
    result = []
    while n > 1:
        n = colatz(n)
        result.append(n)
    return result


# Problema: funzione che restituisce il numero di inizio della catena più lunga della sequenza di Colatz sotto n
# 40.3s
def longest_colatz_sequence_under(n):
    result = []
    for i in range(0, n):
        result.append(len(colatz_generator(i)))
    return result.index(max(result))


# 21.88s
def longest_colatz_sequence_under_optimized_1(n):
    result = []
    for i in range(0, n):
        if i % 2 is 0 and i > 1:
            result.append(result[i//2] + 1)
        else:
            result.append(len(colatz_generator(i)))
    return result.index(max(result))


# 2.26s
def longest_colatz_sequence_under_optimized_2(n):
    result = [0, 0]
    for i in range(2, n):
        j = i
        array = []
        while j > 1:
            j = colatz(j)
            if j < i:
                array = result[j] + len(array) + 1
                break
            else:
                array.append(j)

        if type(array) is int:
            result.append(array)
        else:
            result.append(len(array))
    return result.index(max(result))


print(longest_colatz_sequence_under_optimized_2(1000000))

end = time.time()
print(end - start)
