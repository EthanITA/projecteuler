#   Large sum

# Note for me: I could have used only 11 digits, instead of adding big numbers together

""" 
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

37107287533902102798797998220837590246510135740250
20849603980134001723930671666823555245252804609722
... (skipped 97 numbers)
53503534226472524250874054075591789781264330331690
"""


def firsts(array, n):
    """ Given an array of strings and an integer, the function will return the first n element of array """
    result = ""
    for i in range(n):
        result += array[i]
    return result


def array_to_int(array):
    """ Given an array, the function will return the array converted to integer """
    return [int(i) for i in array]


def strings_sum(s):
    """ Given an array of strings of integers, the function will return their sum in string """
    s = array_to_int(s)
    # result = 0
    # for i in s:
    #     result += i
    # return str(result)
    return str(sum(s))


if __name__ == "__main__":
        
    # Numbers of the problem are stored in Problem_13.txt
    f = open("txt/large_sum.txt", "r")
    digits = f.read().split()

    print(strings_sum(digits))
