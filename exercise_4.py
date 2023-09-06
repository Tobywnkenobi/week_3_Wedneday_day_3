'''
In-Class Exercise #4

Use the reduce function to multiply the numbers in the list below together with a lambda function.
'''


from functools import reduce

numbers = [1,2,3,3,4,5]

ans_list = reduce(lambda x, y:x * y,numbers)
