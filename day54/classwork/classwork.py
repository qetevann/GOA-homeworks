

# CODEWARS:

# 1)

# INSTRUCTION:


# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F


# SOLUTION:

def abbrev_name(name):
    first, last = name.split()
    return f"{first[0].upper()}.{last[0].upper()}"



# 2)

# INSTRUCTIONS:


# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

# Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

# Create a function which translates a given DNA string into RNA.

# For example:

# "GCAT"  =>  "GCAU"
# The input string can be of arbitrary length - in particular, it may be empty. All input is guaranteed to be valid, i.e. each input string will only ever consist of 'G', 'C', 'A' and/or 'T'.



# SOLUTION:


def dna_to_rna(dna):
    dna_rna = ""
    for i in dna:
        if i == 'T':
            dna_rna += 'U'
        else:
            dna_rna += i
    return dna_rna

