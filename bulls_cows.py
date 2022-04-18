#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 19:43:04 2022

@author: vpk9x3
"""
import sys
import random

def is_isogram(word):
    s = set(word)
    if (len(s) == len(word)):
        return True
    return False


print("Hello!\nWelcome to my Bulls and Cows game.")

word = random.choice(open("words.txt","r").readline().split())
start = input("Are you ready to play? [Y|N] - ")

if start in ['Y', 'y', 'yes', 'YES', 'Yes']:
    count = 0
    print("You have to guess a {} letter isogram.".format(len(word)))
    guess = ""
    
    while(guess != word):
        
        guess = input("Try {}: ".format(count))
        bulls = 0
        cows = 0
        try_again = False
        
        
        if len(guess) != len(word):
            print("Wrong length. Try again.")
            #count -=1
            try_again = True
            
        if not is_isogram(guess):
            print("Your guess must be an isogram.")
            #count-=1
            try_again = True
        
        if not try_again:
            index_list = []
            for i in range (len(guess)):
                for j in range(len(word)):
                    if guess[i] == word[j]:
                        if i == j:
                            bulls += 1
                        else:
                            cows += 1
            if bulls == 1:
                b = 'bull'
            else:
                b = 'bulls'
                
            if cows == 1:
                c = 'cow'
            else:
                c = 'cows'
            if bulls != len(word):
                print('You have {} {} and {} {}.'.format(bulls, b, cows, c))
                
            if not try_again:
                count += 1
          
    print('Good job! You guessed the word in {} tries.'.format(count))
else:
    print("OK. Bye.")
    input()
    sys.exit()
    