#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 22:44:55 2023

@author: leeboun
"""

def main():
    '''starts the program'''
    enterfile = input("Enter the name of data file: ")
    while True:
        entercity = input('city: ')
        if entercity == 'quit':
            break
        enterstateabbr = input('state abbreviation: ') 
        file_read(enterfile,entercity,enterstateabbr)
        
        

def file_read(filename,city,stateabbr):
    '''takes in 3 parameters, filename, the name of the file, city and stateabbr, returns
    a formatted list of all of the information for that city in that state'''
    file = open(filename, 'r')
    count = 0
    for line in file:
        line = line.strip()
        fields = line.split(',')
        #print(fields)
        if city == fields[2] and stateabbr == fields[3]:
            count += 1
            #converting population
            converted = float(fields[-1])
            converted *= 1000
            converted = int(converted)
            converted = format(converted, '10,d')
            
            print(fields[0] + '\t' + fields[1] + '\t' + converted)
            
    if count == 0:
        print("no results found for " + city + ", " + stateabbr)
    file.close()
            
            

            