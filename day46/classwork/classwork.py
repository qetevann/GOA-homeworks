


# CODEWARS:

# 1)

# INSTRUCTION:

# In this simple exercise, you will write a function that takes two integers; n and limit; and returns a list of the multiples of n up to and possibly including limit.

# It is guaranteed that n > 0 and limit >= n.

# For example, if the parameters passed are (2, 6), the function should return [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.

# Examples
# n = 2; limit = 6 --> [2, 4, 6]
# n = 2; limit = 5 --> [2, 4]


# SOLUTION:


def find_multiples(integer, limit):
    return list(range(integer, limit + 1, integer))
    
    



# 2)

# INSTRUCTION:


# Create a function with two arguments that will return an array of the first n multiples of x.

# Assume both the given number and the number of times to count will be positive numbers greater than 0.

# Return the results as an array or list ( depending on language ).

# Examples
# x = 1, n = 10 --> [1,2,3,4,5,6,7,8,9,10]
# x = 2, n = 5  --> [2,4,6,8,10]


# SOLUTION:


def count_by(x, n):
    return [x * i for i in range(1, n + 1)]



