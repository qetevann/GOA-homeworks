




# CODEWARS:

# 1)

# INSTRUCTION:


# Create a function that accepts an array of names, and returns an array of each name with its first letter capitalized and the remainder in lowercase.

# Examples
# ['jo', 'nelson', 'jurie'] -->  ['Jo', 'Nelson', 'Jurie']
# ['KARLY', 'DANIEL', 'KELSEY'] --> ['Karly', 'Daniel', 'Kelsey']


# SOLUTION:


def cap_me(arr):
    
    res = []
    for name in arr:
        res.append(name.capitalize())
    
    return res


# 2)

# INSTRUCTION:



# Given 2 strings, a and b, return a string of the form: shorter+reverse(longer)+shorter.

# In other words, the shortest string has to be put as prefix and as suffix of the reverse of the longest.

# Strings a and b may be empty, but not null (In C# strings may also be null. Treat them as if they are empty.).
# If a and b have the same length treat a as the longer producing b+reverse(a)+b


# SOLUTION:

def shorter_reverse_longer(a,b):    
    if len(a) >= len(b):
        longest = a
        shortest = b
        return shortest + longest[::-1] + shortest
    else:
        longest = b
        shortest = a
        return shortest + longest[::-1] + shortest
    


# 3)

# INSTRUCTION:


# There is an array of strings. All strings contains similar letters except one. Try to find it!

# find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
# find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
# Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

# It’s guaranteed that array contains more than 2 strings.

# This is the second kata in series:

# Find the unique number
# Find the unique string (this kata)
# Find The Unique


# SOLUTION:


def find_uniq(arr):
    
    symbols = ""
    
    first_word = arr[0].lower()
    second_word = arr[1].lower()
    third_word = arr[2].lower()
    
    for char in first_word:
        if char not in symbols:
            symbols += char
    
    for char in second_word:
        if char not in symbols:
            for i in third_word:
                if i not in symbols:
                    return first_word
            return second_word
         
    for word in arr:
        for char in word.lower():
            if char not in symbols:
                return word






