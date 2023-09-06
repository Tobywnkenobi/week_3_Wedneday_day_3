# In-Class Exercise #1

# # Write an anonymous function that cubes the arguments passed in and assign the anonymous function to a variable 'f'

# a = lambda x: x**3

# print(a(3))


#exercise 2

numbers = [11, 2, 3, 14, 5]
           
double_n_sub = list(map(lambda n: 2*n - 1, numbers))
print(double_n_sub)