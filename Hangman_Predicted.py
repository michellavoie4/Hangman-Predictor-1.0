#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:28:55 2019

@author: mlavoie
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 22:55:39 2019

@author: Michel Lavoie

"""
####################################################################################################
# A code to predict the actual randomly selected word by using letter frequency in words, word length, vowel occurence
####################################################################################################
# The choice of vowels, consonants over iterations could be implemented

#importing the time module
import time

# I added the importation of the random library (ML)
import random

# import regex module
import re

# import copy module
import copy

# import operator
import operator

# I added a full list of english names (ML)
from nltk.corpus import words
import nltk
nltk.download('words')
word_list = words.words()
# prints 236736
print("Total number of words in the dictionary with duplicates:", len(word_list))

# type(word_list)

# # We replace 'upper case' for 'lower case' letter in the English dictionary using list comprehension
word_list = [item.lower() for item in word_list]

'''
# Define the word length you would like to test
wl = int(input("What is the word length you would like to test?") )
word_list3 = []
for i in word_list:
    if len(i) == wl:
        word_list3.append(i)
word_list = word_list3
'''

# This could have been also done with a long loop and a counter
'''
word_list_lower = [None] * len(word_list)
count = 0
for item in word_list:
    word_list_lower[count] = item.lower()
    count += 1
'''
# Or with enumerate
'''
for num, item in enumerate(word_list):
    word_list[num] = item.lower()
'''

# Check if there are duplicates in the dictionary
# A set is an ordered list without duplicates
if len(word_list) == len(dict.fromkeys(word_list)):
    print("There are no duplicates in the dictionary")
else:
    # Create a dictionary with the list items as keys. This produce a dictionary of words without duplicates and convert back to list.
    word_list_uniq = list( dict.fromkeys(word_list) )
    print(word_list_uniq)
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
print("Total number of words in the dictionary:", len(word_list))

# Greetings
print("WELCOME TO THE HANGMAN PREDICTOR 1.0")

'''
# Enter the length of the word to guess
length_word = int(input("How many letters does your word have?"))

## Remove from the word_list all words that did not match this length
word_list2 = []

for i in word_list:
    if len(i) == length_word:
        word_list2.append(i)
        
print(len(word_list2))
'''

# Or pick a word randomly
rand_word = random.choice(word_list)
print("The random word, which we have to find is : ", rand_word)

# Determine word length
length_word = len(rand_word)
print("Number of letters in the word to guess:", length_word)

# Remove from the word_list all words that did not match this length
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
#print(f)


# Extract consonants and vowels from the dictonary for the next steps
vowels = {key: f[key] for key in f.keys() 
                               & {'a', 'e', 'i', 'o', 'u'}}

conson = copy.deepcopy(f)  # make a DEEP (indpendant) copy of the 'f' dictionary
for values in vowels:
    conson.pop(values)

# Find out the most frequent letter that we have not already guessed

# For the three first iterations, look for vowels only
# if i == 1:3:
#letter_guess = max(vowels.items(), key=operator.itemgetter(1))[0]
# After that, look in consonants
# if i > 3 and < 7:
#    letter_guess = max(conson.items(), key=operator.itemgetter(1))[0] ()
# After that look in any letters
# if i > 6:

prev_guessed = []
nb_iter = 0

####### BIG LOOP...####
while len(word_list2) > 25:
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
    
    letter_guess = max(f.items(), key=operator.itemgetter(1))[0]
    
    # store the previously guessed letter in 'prev_guessed'
    #prev_guessed = []
    prev_guessed.append(letter_guess)
    f.pop(letter_guess)
    #vowels.pop(letter_guess)
    #conson.pop(letter_guess)
    
    # If we guessed correctly, remove all words from the dictionary that don't match the revealed letters.
    word_list_copy = copy.deepcopy(word_list2)
    
    if letter_guess in rand_word:
        print("Our guess:", letter_guess, "match letter(s) in the word")
        # Check for the presence of letter_guess in each word
        for num, i in enumerate(word_list_copy):
            if word_list_copy[num].find(letter_guess) == -1: # If the letter is not in the list
                #print(i)
                word_list2.remove(i)
                
    print("The total number of possible word is:", len(word_list2))
    
        
    # If we guessed incorrectly, remove all words that contain the incorrectly guessed letter
    # i.e., if letter_guess is not in the word we are looking for
    if letter_guess not in rand_word:
        print("The letter we guessed, i.e., ", letter_guess, "was not in the word")
        # Check for the presence of letter_guess in each word
        for num, i in enumerate(word_list_copy):
            if word_list_copy[num].find(letter_guess) != -1: # If the letter is not in the list
                word_list2.remove(i)
            
    print("The total number of possible word is:", len(word_list2))
    
    
    # Print the word, the guessed letter and the unknown letters:
    # for every character in the secret word    
    good_count_rep = 0
    rand_word_list = []
    for char in rand_word:      
    
        # see if the character is in the players guess
        if char in prev_guessed:    
        
        # print then out the character
            print(char)
            good_count_rep += 1
            rand_word_list.append(char)
    
        else:
        
            # if not found, print a dash
            print("_")   
            rand_word_list.append(0)
    
    # Print the number of letter we found out
    print("The total number of letter to guess in the word is:", length_word)
    # print("The number of letter (witout repetitions) we guessed :", good_count)
    print("The TOTAL number of letter (with repetitions) we guessed :", good_count_rep)
    
    # Create the regex pattern
    print("Here is the list for regex definition with zeros when letters are not guessed and with letters:", rand_word_list)
    rand_word_list.count(0) # Count the number of letter remaining to find
    
    counter = 0
    nb_empty_list = []
    list_open = False
    for num, i in enumerate(rand_word_list):
        if i == 0:
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
    blank = [i for i in range(len(rand_word_list)) if rand_word_list[i] == 0] 
    
    # Calculate the letter frequency in each word at the blank position of 'nb_empty_list'
    f_blank = {}  # a counting dictionary
    for i in word_list2:
        for num, letter in enumerate(i):  # iterate over each character in the sentence
            if num in blank:
                f_blank[letter] = f_blank.get(letter, 0) + 1  # get the current value and increase by 1
    print(f_blank) # This is a dictionary of letter frequency taking into account the new position
    
    for i in prev_guessed:
        if i in f_blank:
            f_blank.pop(i) # Remove the letter already guessed
    
    f = copy.deepcopy(f_blank)
    nb_iter += 1

print("Number of iterations needed :", nb_iter)    
print("The answer is: ", word_list2)

###########################################################################


'''
############################################################################
# The GAME
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
                