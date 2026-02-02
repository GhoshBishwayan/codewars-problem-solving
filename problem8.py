'''
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''

# My solution
def high(x):
    
    arrx = x.split()
    sum = 0
    h_s = {}
    for i in arrx:
        for j in i:
            sum += (ord(j) -96)
        h_s.update({i: sum})
        sum = 0
        
    
    return max(h_s, key=h_s.get)

# Flex
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

# Alternative
def high(x):
    highest_score = 0
    for word in x.split(' '):
        score = sum(ord(c)-96 for c in word)
        if score > highest_score:
            highest_score = score
            highest_word = word
            
    return highest_word