from functools import reduce

numbers = [1, 2, 3, 4, 5]



def recursive_subtraction(n):
    if n <= 0:
        return 0
    return n + recursive_subtraction(n-1)

product = recursive_subtraction(5)
print(product)




"""
The following is Senait Abate's work in our group:


def recursive_subtract(num):
    print(num)
    if num > 0:
        return recursive_subtract(num -1) - num
    else:
        return num
recursive_subtract(5)

"""