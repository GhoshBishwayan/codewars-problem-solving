'''
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
4 --> 0 (because 4 is already a one-digit number, there is no multiplication)
'''

def persistence(n):
    count = 0
    def circus(n, count):
        r = 1
        if len(str(n)) > 1:
            count += 1
            
            for i in str(n):
                r = r * int(i)
            
            if len(str(r)) > 1:
                n = int(r)
                r = 1
                return circus(n, count) # Recursion
            else:
                return count
        else:
            return count
    res = circus(n, count)
    return res