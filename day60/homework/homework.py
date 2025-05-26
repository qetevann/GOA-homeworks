



# CODEWARS:

# 1)

# INSTRUCTION


# Recreation of Project Euler problem #6

# Find the difference between the square of the sum of the first n natural numbers (1 <= n <= 100) and the sum of their squares.

# Example
# For example, when n = 10:

# The square of the sum of the numbers is:

# (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)² = 55² = 3025
# The sum of the squares of the numbers is:

# 1² + 2² + 3² + 4² + 5² + 6² + 7² + 8² + 9² + 10² = 385
# Hence the difference between square of the sum of the first ten natural numbers and the sum of the squares of those numbers is: 3025 - 385 = 2640


# SOLUTION:

def difference_of_squares(n):
    sum_n = n * (n + 1) // 2
    square_of_sum = sum_n ** 2
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    return square_of_sum - sum_of_squares




# 2)

# INSTUCTION:

# Given a 2D ( nested ) list ( array, vector, .. ) of size m * n, your task is to find the sum of the minimum values in each row.

# For Example:

# [ [ 1, 2, 3, 4, 5 ]        #  minimum value of row is 1
# , [ 5, 6, 7, 8, 9 ]        #  minimum value of row is 5
# , [ 20, 21, 34, 56, 100 ]  #  minimum value of row is 20
# ]
# So the function should return 26 because the sum of the minimums is 1 + 5 + 20 = 26.

# Note: You will always be given a non-empty list containing positive values.

# ENJOY CODING :)



# SOLUTION:

def sum_of_minimums(numbers):

    return sum(min(row) for row in numbers)



#  3)

# INSTRUCTIONS:

# Complete the function which takes a non-zero integer as its argument.

# If the integer is divisible by 3, return the string "Java".

# If the integer is divisible by 3 and divisible by 4, return the string "Coffee"

# If one of the condition above is true and the integer is even, add "Script" to the end of the string.

# If none of the condition is true, return the string "mocha_missing!"

# Examples
# 1   -->  "mocha_missing!"
# 3   -->  "Java"
# 6   -->  "JavaScript"
# 12  -->  "CoffeeScript"


# SOLUTION:

def caffeine_buzz(n):
    if n % 3 == 0 and n % 4 == 0:
        result = "Coffee"
    elif n % 3 == 0:
        result = "Java"
    else:
        return "mocha_missing!"
    
    if n % 2 == 0:
        result += "Script"
    
    return result



# 4)

# INSTRUCTION:

# Your task is to rotate a matrix 90 degree to the left. The matrix is an array of integers with dimension n,m. So this kata checks some basics, it's not too difficult.

# There's nothing more to explain, no tricks, no "bad cases";-). Perhaps you take a look at the testcases...

# One easy example:

# Input: {{-1, 4, 5},
#         { 2, 3, 4}}

# Output: {{ 5, 4},
#          { 4, 3},
#          {-1, 2}}
# First there are some static tests, later on random tests too...


# SOLUTION:

def rotate_matrix(arr):
    return [list(row) for row in zip(*arr)][::-1]


