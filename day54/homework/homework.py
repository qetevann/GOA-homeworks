

# CODEWARS


# 1)

# INSTRUCTIONS:

# What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

# Example(Input --> Output)

# "apple ban" --> ["apple 5", "ban 3"]
# "you will win" -->["you 3", "will 4", "win 3"]
# Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .

# Note: String will have at least one element; words will always be separated by a space.



# SOLUTION:

def add_length(str):
    words = str.split()
    
    result = [f"{word} {len(word)}" for word in words]
    
    return result



# 2)

# INSTRUCTIONS:

# I would like to be able to pass an array with two elements to my swapValues function to swap the values. However it appears that the values aren't changing.

# Can you figure out what's wrong here?



# SOLUTION:

def swap_values(args):
    swap_values = args[0]
    args[0] = args[1]
    args[1] = swap_values



# INSTRUCTIONS:

# You are given two sorted arrays that contain only integers. 
# These arrays may be sorted in either ascending or descending order. Your task is to merge them into a single array, ensuring that:

# The resulting array is sorted in ascending order.

# Any duplicate values are removed, so each integer appears only once.

# If both input arrays are empty, return an empty array.

# No input validation is needed, 
# as both arrays are guaranteed to contain zero or more integers.



# SOLUTION:

def merge_arrays(arr1, arr2):
    combined = arr1 + arr2

    return sorted(set(combined))