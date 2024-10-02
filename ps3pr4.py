#
# ps3pr4.py (Problem Set 3, Problem 4)
#
# More algorithm design!
#

def first_occur(elem, seq):
    ''' takes in an element and sequence and returns the index of the 1st time the element
    shows up in the sequence'''
    previous = 0
    if seq == [] or seq=='':
        return -1
    else:
        rest = first_occur(elem, seq[1:])
        if elem == seq[0]:
            return previous 
        if rest != -1:
            previous += 1
            return previous + rest
        elif rest == -1:
            return -1
            
        
def rem_first(c, s):
    '''takes in a string s and returns a new string without the first appearance of the char c'''
    if s == '':
        return s
    elif len(s)==1:
        if s[0]==c:
            return ''
        else:
            return s
    else:
        rest = rem_first(c, s[1:])
        if s[0]==c:
            return s[1:]
        else:
            return s[0] + rest

def jscore(s1, s2):
    """ takes in 2 strings and returns the number of letters in both strings """
    if s1 == '' or s2 == '':
        return 0
    if len(s1)==1 and len(s2)==1 and s1[0] != s2[0]:
        return 0
    else:
        if s1[0] in s2:
            jscore_rest = jscore(s1[1:], rem_first(s1[0], s2))
            return 1 + jscore_rest
        else:
            jscore_rest = jscore(s1[1:], s2)
            return jscore_rest
        
def negate_last(n, values):
    ''' takes in a number and a list and negates the last occurence of that number in the list'''
    if values == []:
        return values
    elif n not in values:
        return values
    elif values[-1]==n:
        return values[:-1] + [values[-1]*-1]
    else:
        before = negate_last(n, values[:-1])
        return before + [values[-1]]
       



    