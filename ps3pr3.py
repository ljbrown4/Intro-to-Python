#
# ps3pr3.py (Problem Set 3, Problem 3)
#
# Caesar cipher / decipher
#

# A template for the first function that you are required to write.
def rotate(c, n):
    """ takes in a character and shifter (postitive num from 1-25) and returns a character
    based on the shift"""
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    # Put the rest of your code for this function below.
    if 'a' <= c <= 'z':
        new_ord = ord(c) + n
        if new_ord > ord('z'):
            new_ord = new_ord - 26
            
    elif 'A' <= c <= 'Z':
        new_ord = ord(c) + n
        if new_ord > ord('z'):
            new_ord = new_ord - 26
            
    else:
        new_ord = ord(c)
    return chr(new_ord)


#### Put your code for the encipher function below. ####
def encipher(s, n):
    """ takes in a string and shifter (postitive num from 1-25) and returns a string
    based on the shift"""
    if s == '':
        return s
    elif len(s)== 1:
        return rotate(s, n)
    else:
        char_left = encipher(s[1:],n)
        shift_chr = rotate(s[0],n)
        return shift_chr + char_left


# A helper function that you will use in implementing your 
# string_score function.
# You should *NOT* modify this function.
def letter_score(c):
    """ takes a single character c and returns a numeric score that 
        is based on how frequently that character appears in 
        English-language text documents.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    if c == ' ': 
        return 0.1904
    elif c == 'e' or c == 'E': 
        return 0.1017
    elif c == 't' or c == 'T': 
        return 0.0737
    elif c == 'a' or c == 'A': 
        return 0.0661
    elif c == 'o' or c == 'O': 
        return 0.0610
    elif c == 'i' or c == 'I': 
        return 0.0562
    elif c == 'n' or c == 'N': 
        return 0.0557
    elif c == 'h' or c == 'H': 
        return 0.0542
    elif c == 's' or c == 'S': 
        return 0.0508
    elif c == 'r' or c == 'R': 
        return 0.0458
    elif c == 'd' or c == 'D': 
        return 0.0369
    elif c == 'l' or c == 'L': 
        return 0.0325
    elif c == 'u' or c == 'U': 
        return 0.0228
    elif c == 'm' or c == 'M': 
        return 0.0205
    elif c == 'c' or c == 'C': 
        return 0.0192
    elif c == 'w' or c == 'W': 
        return 0.0190
    elif c == 'f' or c == 'F': 
        return 0.0175
    elif c == 'y' or c == 'Y': 
        return 0.0165
    elif c == 'g' or c == 'G': 
        return 0.0161
    elif c == 'p' or c == 'P': 
        return 0.0131
    elif c == 'b' or c == 'B': 
        return 0.0115
    elif c == 'v' or c == 'V': 
        return 0.0088
    elif c == 'k' or c == 'K': 
        return 0.0066
    elif c == 'x' or c == 'X': 
        return 0.0014
    elif c == 'j' or c == 'J': 
        return 0.0008
    elif c == 'q' or c == 'Q': 
        return 0.0008
    elif c == 'z' or c == 'Z': 
        return 0.0005
    else:
        return 0.0



#### Put your code for string_score and decipher below. ####

def string_score(s):
    '''takes in a word/string and returns the score of it'''
    score = sum([letter_score(letter) for letter in s])
    return score

def decipher(s):
    ''' deciphers the taken in string and returns the best option'''
    #options = [ encipher(s,n) for n in range(26)]
    #print(options)
    scoreoption = [[string_score(encipher(s,n)), encipher(s,n)] for n in range(26)]
    #print(scoreoption)
    bestdecipher = max(scoreoption)
    return bestdecipher[1]










