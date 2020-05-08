

def number_of_letters(n):
    # for each 3 number of n
    # 12 345 678
    for i in len(str(n))//3 + (len(str(n)) % 3 > 0):
        
        pass

def count_letters_to(n):
    count = 0
    for i in range(1, n+1):
        count += number_of_letters(i)
    return count

print(count_letters_to(10))