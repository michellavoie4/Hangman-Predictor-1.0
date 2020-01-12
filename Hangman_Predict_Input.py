#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 22:40:17 2020

@author: mlavoie
"""

####################################################################################################
############ Predicting a word of a given length when we need a hand to win HANGMAN ################
##                                                                                                ##
##                          WELCOME TO THE HANGMAN PREDICTOR 1.0                                  ##
##                                                                                                ##
####################################################################################################
####################################################################################################

# import regex module
import re

# import copy module
import copy

# import operator for the calculations of maximum probability
import operator

# import nltk dictionary
import nltk
from nltk.corpus import words

# import sys
import sys

# Load the word of the dictionary
nltk.download('words')
word_list = words.words()
# print("Total number of words with duplicates and single letters in the dictionary:", len(word_list))

# # We replace 'upper case' for 'lower case' letter in the English dictionary using list comprehension
word_list = [item.lower() for item in word_list]

# Check if there are duplicates in the dictionary
# A set is an ordered list without duplicates
if len(word_list) == len(dict.fromkeys(word_list)):
    print("There are no duplicates in the dictionary")
else:
    # Create a dictionary with the list items as keys. This produce a dictionary of words without duplicates and convert back to list.
    word_list_uniq = list( dict.fromkeys(word_list) )
    #print(word_list_uniq)
    nb_duplicates = len(word_list)-len(word_list_uniq)
    print("Be careful ! We removed", nb_duplicates, "duplicates in the dictionary")

# Remove the single letter (a to z)    
# This create a list of alphabetic letter        
list_letter = [chr(i) for i in range(ord('a'),ord('z')+1)]

word_list_mod = copy.deepcopy(word_list_uniq)   # Create a copy of word_list2 so that we can delete in the for loop
list_letter = [chr(i) for i in range(ord('a'),ord('z')+1)]
for i in word_list_mod:
    for j in list_letter:
        if j == i:
            word_list_uniq.remove(i)

print("Number of single letter removed =", len(word_list) - nb_duplicates - len(word_list_uniq) )

word_list = copy.copy(word_list_uniq)
print("Total number of words in the dictionary:", len(word_list), "words")

# Produce a list of word length and find the maximum word length for later
list_length = []
for i in word_list:    
    list_length.append(len(i))
print("The longest word in the dictionary has", max(list_length), "words \n")

# Greetings
print("###########################################################")
print("\n        WELCOME TO THE HANGMAN PREDICTOR 1.0 \n")
print(" \n                  Language : English         \n")
print("\n You can quit the game at any time by typing : q \n")
print("###########################################################")

# A function testing if a string contains an integer
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

# Enter the length of the word to guess      
while True:
      length_word = input("How many letters does your word have?"  )
      if length_word == 'q':
          sys.exit('Bye Bye')
      if RepresentsInt(length_word) == False: # If it is not an interger in the string
          print("Error: We need an integer")
          continue
      if len(length_word) > 2: # Select only the length between 1 and 99
          print("Error: Only one valid word length is needed")
          continue
      else:
          length_word = int(length_word)
          if length_word > max(list_length): # Select only the length up to the maximum word length
              print('Word length too long! No such word of this length in the dictionary')
              continue
          else:
              break
                
                
## Remove from the word_list all words that did not match this length
word_list2 = []

for i in word_list:
    if len(i) == length_word:
        word_list2.append(i)
        
print("Number of possible words of this length:", len(word_list2))

# Calculate the letter frequency in each word of this given length
f = {}
for i in word_list2:
    for char in i:
       f[char]=f.get(char,0)+1

####################################################################################
# Here is a part in which the user start the program after having started playing Hangman.
# In this case, the user may want to start the program with a few letters already guessed.
# Ask the user the wrong letters.
while True:
    wrong_letter= input("What are the letters you wrongly guessed? (Press zero if no previous guess)")
    if wrong_letter == '0' or RepresentsInt(wrong_letter) == False:
        break
    if wrong_letter == 'q':
          sys.exit('Bye Bye')
    if RepresentsInt(wrong_letter) == True: # or wrong_letter != 0: # If it is not a letter in the string
          print("Error: This is an interger, please type letters")
          continue

# 2-Remove the letters tried (but incorrect) from the dictionary (f) if wrong_letter different from 0.
if wrong_letter != '0': # set object does not support indexing...
    wrong_letter = set(wrong_letter)
    for values in wrong_letter:     
        f.pop(values)
######################################################################################       

'''
# Empirical guess taking into account consonants and vowels is not yet implemented
# Extract consonants and vowels from the dictonary for the next steps
vowels = {key: f[key] for key in f.keys() 
                               & {'a', 'e', 'i', 'o', 'u'}}

import copy
conson = copy.deepcopy(f)  # make a DEEP (indpendant) copy of the 'f' dictionary
for values in vowels:
    conson.pop(values)
'''

prev_guessed = []
nb_iter = 0

while len(word_list2) > 20:
    letter_guess = 0
    
    '''
    if nb_iter in range(1,3):
        vowels = {key: f[key] for key in f.keys() 
                               & {'a', 'e', 'i', 'o', 'u'}}
        letter_guess = max(vowels.items(), key=operator.itemgetter(1))[0]
        # After that, look in consonants
    if nb_iter > 3 and nb_iter < 7:
        letter_guess = max(conson.items(), key=operator.itemgetter(1))[0] ()
       # After that look in any letters
    if nb_iter > 6:
    '''
    
    # Find out the most frequent letter that we have not already guessed
    letter_guess = max(f.items(), key=operator.itemgetter(1))[0]
    
    # Say to user the best guess letter !!!
    print("Your best guess letter is:", letter_guess)
    
    # store the previously guessed letter in 'prev_guessed'
    #prev_guessed = []
    prev_guessed.append(letter_guess)
    f.pop(letter_guess)
    #vowels.pop(letter_guess)
    #conson.pop(letter_guess)
    
    # Ask the user if he guessed correctly this letter.
    while True:
        answer = input("Did you guess correctly?, press y (for yes) or n (for no)  ")
        if answer == 'y' or answer == 'n':
            break
        if answer == 'q':
            sys.exit("Bye Bye!")
        else:
            print("Error : invalid key")
    
    # If we guessed correctly, remove all words from the dictionary that don't match the revealed letters.
    word_list_copy = copy.deepcopy(word_list2)
    
    if answer == "y":   # if letter_guess in rand_word:
        print("Our guess:", letter_guess, "match letter(s) in the word")
        # Check for the presence of letter_guess in each word
        for num, i in enumerate(word_list_copy):
            if word_list_copy[num].find(letter_guess) == -1: # If the letter is not in the list
                #print(i)
                word_list2.remove(i)
                
    print("The total number of possible word is:", len(word_list2))
   
        
    # If we guessed incorrectly, remove all words that contain the incorrectly guessed letter
    # i.e., if letter_guess is not in the word we are looking for
    if answer == "n":  # if letter_guess not in rand_word:
        print("The letter we guessed, i.e., ", letter_guess, "was not in the word")
        # Check for the presence of letter_guess in each word
        for num, i in enumerate(word_list_copy):
            if word_list_copy[num].find(letter_guess) != -1: # If the letter is not in the list
                word_list2.remove(i)
            
    print("The total number of possible word is:", len(word_list2))
    
    
    # Ask and print the word, i.e., the guessed letter and the unknown letters:
    # This loop ensure we enter a valid word length and can print the word list
    while True:
        rand_word_list = list(input("What are the letters (a-z) and blank space (0)?  " ))
        if rand_word_list == ['q']:
            sys.exit("Bye Bye!")
        if len(rand_word_list) != length_word:
            print("Error, there is a mistake in the word length")
        #if rand_word_list == ['p', 'r', 'i', 'n', 't', 'w', 'o', 'r', 'd']:
        #    print(word_list2)
        if len(word_list2) < 200:
            print(word_list2)
        if len(rand_word_list) == length_word:
            break
        
        
    # Create the regex pattern
    print("Here is the list for regex definition with zeros when letters are not guessed and with letters:", rand_word_list)
    rand_word_list.count(0) # Count the number of letter remaining to find
    
    counter = 0
    nb_empty_list = []
    list_open = False
    for num, i in enumerate(rand_word_list):
        if i == "0":
            counter += 1
            list_open = True
        else:
            if list_open:
                nb_empty_list.append(counter)
            counter = 0
            list_open = False
            nb_empty_list.append(rand_word_list[num])
    
    if counter !=0:
        nb_empty_list.append(counter)
    print("This is a list with the number of letters to guess and of the letter guessed:", nb_empty_list) 
    
    # if we have a number of zeros, we plug '%r' in the regular expression
    # If we have a letter, we plus '%s' in the regular expression
    
    # Create the regex
    # regex1 = re.search(r'\w{%r}%s\w{%r}' % (nb1, nb2, nb3), rand_word)
    
    # look for the pattern in all the remaining words.
    # Create a new smaller dictionary with potential words.
    word_list_copy2 = copy.deepcopy(word_list2)   # Create a copy of word_list2 so that we can delete in the for loop
    x = 0
    
    for i in word_list_copy2:
        if len(nb_empty_list) == 1 and type(nb_empty_list[0]) == int:
            continue # Nothing to do, we did not guess any letters
        
        string = ''
        string2 = ''
        for num, j in enumerate(nb_empty_list):
            if type(nb_empty_list[num]) == int:
                string += '\\w{%r}'
            if type(nb_empty_list[num]) == str:
                string += '%s'
        x = re.search(string % tuple(nb_empty_list), i)
        
        if all(isinstance(x, str) for x in nb_empty_list) == True:
            word_list2 = ''.join(nb_empty_list)
            print(word_list2)
            break # only one possible word left
        if len(nb_empty_list) == 1 and type(nb_empty_list[0]) == str:
            word_list2 = ''.join(nb_empty_list)
            print(word_list2)
            break    
        # if x exists, do nothing, # keep the words in the dictionary (word_list2)
        if not x:
            word_list2.remove(i) # remove the word from the dictionary  
    
    print("Total number of possible words:", len(word_list2))
    
    # rand_word_list
    # find the blank spaces indices in the rand_word_list (position to be filled in the word)
    blank = [i for i in range(len(rand_word_list)) if rand_word_list[i] == "0"] 
    
    # Calculate the letter frequency in each word at the blank position of 'nb_empty_list'
    f_blank = {}  # a counting dictionary
    for i in word_list2:
        for num, letter in enumerate(i):  # iterate over each character in the sentence
            if num in blank:
                f_blank[letter] = f_blank.get(letter, 0) + 1  # get the current value and increase by 1
    
    for i in prev_guessed:
        if i in f_blank:
            f_blank.pop(i) # Remove the letter already guessed
    
    f = copy.deepcopy(f_blank)
    nb_iter += 1

print("Number of iterations needed :", nb_iter)    

if len(word_list2) < 200:
    print("The answer is: ", word_list2)

###########################################################################




'''
############################################################################
# The HANGMAN GAME
############################################################################
# Welcoming the user
name = input("What is your name? ")

print("Hello " + name + "!", "Time to play hangman!")

print("")

#wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

# here we set the secret
# word = "secret"


# Here I choose a randomly selected word within the dictionary
word = random.choice(word_list)

#creates an variable with an empty value
guesses = ''

#determine the number of turns
# Here we set 10 tries
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print(char)    

        else:
    
        # if not found, print a dash
            print("_")     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print("You won")  

    # exit the script
        break              

    #print

    # ask the user go guess a character
    guess = input("guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print("Wrong")    
 
    # how many turns are left
        print("You have", + turns, 'more guesses') 
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Lose"
            print("You Lose")  
            
            
            key = input("Do you want to play again? (type yes or no)")   
            if key == "yes":
                print("Good, we will play again")
                guesses = ""
                turns = 10
            elif key == "no":
                print("Good Bye, See you next time")
                sys.exit("The program has ended")
            
'''                  
                