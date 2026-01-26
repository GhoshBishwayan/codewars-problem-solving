"""
Reverse every word in the sentence that has 5 or more characters,
while keeping shorter words unchanged. Return the final sentence
with words separated by single spaces.
"""
#solution
def spin_words(sentence):
    res = ''
    if len(sentence):
        w_arr = sentence.split()
        for i in w_arr:
            if len(i) >= 5:
                i = i[::-1]
            res += i + " "
        return res.strip()
    return ""

