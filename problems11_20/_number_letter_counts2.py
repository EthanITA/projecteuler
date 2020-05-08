""" 
If the numbers 1 to 5 are written out in words: 
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""

# definizione di numeri in lettere per quelli che non sono ripetuti (es. one hundred)
one_to_ninety = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eigthy",
    90: "ninety"
}


# problema: dato n unità, restituire il numero in centinaia espresso in lettere
def getHundredOf(n):
    return one_to_ninety[n] + "hundred"


# Dato n intero sotto 1000, restituisce il numero espresso in lettere (inglese)
def getLettersOf(n):
    n = str(n)
    result = ""
    if len(n) is 3:
        result += getHundredOf(int(n[0])) + "and"
        n = n[1] + n[2]
    if len(n) is 2:
        if int(n[0]) > 1:
            result += one_to_ninety[int(n[0]) * 10] + one_to_ninety[int(n[1])]

            n = n[1]
        else:
            key = int(n[0] + n[1])
            result += one_to_ninety[key]
            n = []
    if len(n) is 1:
        result += one_to_ninety[int(n[0])]

    print(result)
    return result

# Dato n intero, restituisce il numero di lettere per esprimere n (inglese)


def NumberLettersCount(n):
    return len(getLettersOf(n))


count = 0
for num in range(1, 1000):
    print(num)
    count += NumberLettersCount(num)

print(count + len("onethousand"))
