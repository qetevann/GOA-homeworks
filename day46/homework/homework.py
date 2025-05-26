


# CODEWARS:


# 1)

# INSTRUCTION:

# Nathan loves cycling.

# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.

# For example:

# time = 3 ----> litres = 1

# time = 6.7---> litres = 3

# time = 11.8--> litres = 5


# SOLUTION:


import math

def litres(time):
    return math.floor(time * 0.5)
    


# 2)

# INSTRUCTION:


# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.


# SOLUTION:

def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
    


# 3)

# INSTRUCTION:


# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

# [1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
# [1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
# [] --> []
# You can assume that all values are integers. Do not mutate the input array.


# SOLUTION:


def invert(lst):
    return [-x for x in lst]

