'''
Implement the function unique_in_order which takes as argument a 
sequence and returns a list of items without any elements with 
the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
'''

# My solutions

def unique_in_order(sequence):
    
    arr = []
    
    if len(sequence) > 1 :
        u = sequence[0]
        arr.append(u)
        
    elif len(sequence) == 1:
        u = sequence[0]
        arr.append(u)
        return arr
        
    else:
        return arr
    
    
    for i in sequence:
        if i != u:
            arr.append(i)
            u = i
    
    return arr

# Best solution1

def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

# Best solution 2

def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res
            
            
# short 
def unique_in_order(iterable):
    return [ ch for i, ch in enumerate(iterable) if i == 0 or ch != iterable[i - 1] ]
