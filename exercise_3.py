# In-Class Exercise #3

# Filter out all the numbers that are below the mean of the list.
# Hint: Import the 'statistics' module
import statistics

numbers = [1,2,3,4,5,20,10,17]

meanish = statistics.mean(numbers)

above = list(filter(lambda a: a > meanish, numbers))
below = list(filter(lambda b: b < meanish, numbers))

print(below)

print(above)

print(meanish)