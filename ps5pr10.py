#
# ps5pr10.py (Problem Set 5, Problem 10)
#
# Choosing the correct type of loop
#

def add_odds(n):
    ''' takes in an integer n and returns the sum of the first n odd numbers '''
    sum = 0
    ranges = (n*2)+1
    for i in range(ranges):
        if i % 2 == 1:
            print(sum, "+", i, "=", sum + i)
            sum += i
    return sum
            

def get_mult(n):
    '''takes in an integer n and asks user to input a int that is a mult of n until they're correct'''
    multiple = int(input("Enter a multiple: "))
    count = 1
    while count > 0:
        if multiple % n == 0:
            count -= 1
            return multiple
        else:
            multiple = int(input("Invalid input. Try again: "))
        
    
        
       
        
        
        