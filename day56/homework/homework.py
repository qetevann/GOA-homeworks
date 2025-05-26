


# CODEWARS

# 1)

# INSTRUCTION:


# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

# If you want to know more: http://en.wikipedia.org/wiki/DNA

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

# Example: (input --> output)

# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"


# SOLUTION:


def DNA_strand(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in dna)




# 2)

# INSTRUCTION:


# You might know some pretty large perfect squares. But what about the NEXT one?

# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on your language. You may assume the argument is non-negative.

# Examples ( Input --> Output )
# 121 --> 144
# 625 --> 676
# 114 --> -1  #  because 114 is not a perfect square


# SOLUTION:


import math

def find_next_square(sq):

    root = math.isqrt(sq)
    if root * root == sq:
        return (root + 1) ** 2
    else:
        return -1



# 3)

# INSTRUCTION:


# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"


# SOLUTION:


def reverse_words(text):
    words = text.split(' ')
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


# 4)

# INSTRUCTION:

# Write a function that doubles every second integer in a list, starting from the left.

# Example:

# For input array/list :

# [1,2,3,4]
# the function should return :

# [1,4,3,8]



# SOLUTION:


def double_every_other(lst):
    
    
    for i in range(1, len(lst), 2):
        
        lst[i] *= 2
    return lst
