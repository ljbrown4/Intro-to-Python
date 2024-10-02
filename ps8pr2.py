#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
# Markov text generation    
#
import random

def create_dictionary(filename):
    '''takes in a file and returns a dictionary of key values where each key is a word and each 
    value is the words following the key'''
    file = open(filename, 'r')
    text = file.read()
    file.close()
    
    words = text.split()
    d = {}
    current_word = '$'
    for next_word in words:
        if current_word not in d:
            d[current_word] = [next_word]
        else:
            d[current_word] += [next_word]
        if next_word[-1] in '.,?!':
            current_word = '$'
        else: current_word = next_word
    return d

def generate_text(word_dict, num_words):
    '''takes in a dictionary of word transitions, word_dict, and a pos int, num_words, and prints
    num_words generated words using the word_dict'''
    current_word = '$'
    for nextword in range(num_words):
        wordlist = word_dict[current_word]
        next_word = random.choice(wordlist)
        print(next_word, end=' ')
        if next_word[-1] in '.,?!':
            current_word = '$'
        else: current_word = next_word
    print()