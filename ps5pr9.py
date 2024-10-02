#
# ps5pr9.py (Problem Set 5, Problem 9)
#
# Processing sequences with loops
#

def cube_all(vals):
    """ takes in a list and returns a new list of each element cubed """
    result = []
    
    for num in vals:
        num **= 3
        result += [num]
    return result


def add_stars(s):
    """ takes in a string and returns a string wit astericks btwn each character """
    result = ''
    
    for i in range(len(s)):
        if i == len(s)-1:
            result += s[i]
        else:
           result += s[i] + "*"
    return result


def compare(s1, s2):
    """takes in 2 strings and returns the # of times they are different """
    result = 0
    
    len_shorter = min(len(s1), len(s2))
    len_longer = max(len(s1), len(s2))
    
    result = len_longer - len_shorter
    
    for i in range(len_shorter):
        if s1[i] != s2[i]:
            result += 1 
    return result

s
def weave(vals1, vals2):
    ''' takes in 2 lists and returns a list of the 2 lists weaved together'''
    result = []
    # finding the longer and shorter lists
    if len(vals1) > len(vals2) or len(vals1) == len(vals2):
        len_longer = vals1
        len_shorter = vals2
    elif len(vals1) < len(vals2):
        len_longer = vals2
        len_shorter = vals1
        
    count = 0
    for i in range(len(len_shorter)):
        count += 1
        result += [vals1[i]] + [vals2[i]]
        
    result += len_longer[count:]
    return result


    
            