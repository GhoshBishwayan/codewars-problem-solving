'''
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

Example 1:
a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

Example 2:
a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []

Notes:
- Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
- In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
- Beware: In some languages r must be without duplicates.
'''

# My Solution - while doing it I learn that python can check if 'arp' in 'sharp' which is not possible in C
def in_array(array1, array2):
    # your code
    arr = []
    for word1 in array1:
        for word2 in array2:
            if word1 in word2:
                arr.append(word1)
    return sorted(set(arr))

# without set
def in_array(array1, array2):
    # your code
    res = []
    for a1 in array1:
        for a2 in array2:
            if a1 in a2 and not a1 in res:
                res.append(a1)
    res.sort()
    return res

#short
def in_array(a1, a2):
    return sorted(set(s1 for s1 in a1 if any(s1 in s2 for s2 in a2)))