# ps4pr3.py (Problem Set 4, Problem 3)
#
# Functions that process binary numbers
#

def double_rec(binvals):
    '''takes in a list of bits and returns the binary code for those bits doubled using recursion'''
    doubled = [binvals[0]+ '0']
    if binvals == []:
        return binvals
    elif len(binvals) == 1:
        return doubled
    else:
        bin_rest = double_rec(binvals[1:])
        #print(doubled)
        return doubled + bin_rest
    
def double_lc(binvals):
    '''takes in a list of bits and returns the binary code for those bits doubled using lc'''
    doubled = [x+'0' for x in binvals]
    return doubled

def add_bitwise(b1, b2):
    """ adds two bits"""
    if b1=='' and b2=='':
        return ''
    elif len(b1)>=1 and b2== '':
        return b1
    elif len(b2)>=1 and b1== '':
        return b2
    else:
        bit_rest = add_bitwise(b1[:-1],b2[:-1])
        if (b1[-1]== '1' and b2[-1]== '0') or (b2[-1]== '1' and b1[-1]== '0'):
            #print(bit_rest)
            return bit_rest + '1'
        elif b1[-1]== '0' and b2[-1]== '0':
            return bit_rest + '0'
        elif b1[-1]== '1' and b2[-1]== '1':
            bit_rest = bit_rest + '0'
            #print(bit_rest)
            carrybit = add_bitwise(bit_rest[:-1], b1[-1])
            #print(carrybit)
            return carrybit + bit_rest[-1]
                
            
            
                
            
                
                
            