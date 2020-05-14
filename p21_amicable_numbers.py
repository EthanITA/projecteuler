""" Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000. """


def divisors(n):
    result = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            result.append(i)
    return result

def sum_of_divisors(n):
    return sum(divisors(n))

def amicable(a, b):
    if a != b and sum_of_divisors(b) == a:
        return True
    else:
        return False



def amicable_numbers_under(n):
    amicable_numbers = []
    for a in range(1, n):
        if a not in amicable_numbers:
            b = sum_of_divisors(a)
            if amicable(a, b):
                amicable_numbers.append(a)
                amicable_numbers.append(b)
    return amicable_numbers

if __name__ == "__main__":
    
    #print(amicable(284, 220))
    print(sum(amicable_numbers_under(10000)))