


# CODEWARS

# 1)

# INSTRUCTION:


# Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (word) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.

# Example (Input --> Output)
# "CodEWaRs" --> [0,3,4,6]


# SOLUTION:


def capitals(word):
    return [i for i, char in enumerate(word) if char.isupper()]




# 2)

# INSTRUCTION:

# There is a war and nobody knows - the alphabet war!
# There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.

# Task
# Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.

# The left side letters and their power:

#  w - 4
#  p - 3
#  b - 2
#  s - 1
# The right side letters and their power:

#  m - 4
#  q - 3
#  d - 2
#  z - 1
# The other letters don't have power and are only victims. Sum up each side's letters' power values to determine which side wins.

# Example
# AlphabetWar("z");        //=> Right side wins!
# AlphabetWar("zdqmwpbs"); //=> Let's fight again!
# AlphabetWar("zzzzs");    //=> Right side wins!
# AlphabetWar("wwwwwwz");  //=> Left side wins!




# SOLUTION:


def alphabet_war(fight):
    left = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    
    left_score = sum(left.get(c, 0) for c in fight)
    right_score = sum(right.get(c, 0) for c in fight)

    if left_score > right_score:
        return "Left side wins!"
    elif right_score > left_score:
        return "Right side wins!"
    else:
        return "Let's fight again!"
