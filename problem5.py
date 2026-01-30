'''
Implement a function that computes the difference between two lists. The function should remove all occurrences of elements from the first list (a) that are present in the second list (b). The order of elements in the first list should be preserved in the result.

Examples
If a = [1, 2] and b = [1], the result should be [2].

If a = [1, 2, 2, 2, 3] and b = [2], the result should be [1, 3].
'''

# My solution

def array_diff(a, b):
    res = []
    
    for item in a:
        if item in b:
            continue
        else:
            res.append(item)
    return res

# Short

def array_diff(a, b):
    return [x for x in a if x not in b]

# Smart

def array_diff(a, b):
    #your code here
    for i in range(len(b)):
        while b[i] in a:
            a.remove(b[i])
    return a

# 2

def array_diff(a, b):
    new_list = []
    for val in a:
        if val not in b:
            new_list.append(val)
            
    return new_list 