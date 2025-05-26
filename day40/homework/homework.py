

# CODEWARS:

# 1)

# INSTRUCTION:

# Write a function that removes the spaces from the string, then return the resultant string.

# Examples (Input -> Output):

# "8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
# "8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
# "8aaaaa dddd r     " -> "8aaaaaddddr"


# SOLUTION:

def no_space(x):
    result = x.replace(" ", "")
    return result



# 2)

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
    


# 3)

# INSTRUCTION:


# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

# Task
# Given a year, return the century it is in.

# Examples
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20
# 2742 --> 28


# SOLUTION:

def century(year):
    return (year - 1) // 100 + 1



# 4)

# INSTRUCTION:


# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example (Input => Output):
# 35231 => [1,3,2,5,3]
# 0     => [0]


# SOLUTION:


def digitize(n):
    reversed1 = []
    reversed2 = []
    
    for num in str(n):
        reversed1.append(int(num))
        
    for i in range (len(reversed1) -1, -1, -1 ):
        reversed2.append(reversed1[i])
        
    return reversed2



# 5)

# INSTRUCTION:


# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.


def are_you_playing_banjo(name):
    
    name1 = ['R', 'r']

    if name[0] == 'R' or name[0] == 'r':

        return name + ' plays banjo'
    elif len(name) != 'R' and len(name) != 'r':
        return name + ' does not play banjo'
