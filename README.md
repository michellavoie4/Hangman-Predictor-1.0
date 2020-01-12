# Hangman-Predictor-1.0

#########################################################################################
####################### READ ME FOR THE HANGMAN PREDICTOR ###############################
#########################################################################################

The python script "Hangman_Predict_Input.py" allows winning all the time when playing the popular game Hangman!

###############
# Description #
###############
This program "Hangman_Predict_Input.py" suggest a best guest letter given a word length, the letters already guessed and the letters wrongly guessed. It also computes the more probable words given a known sequence of letters in a word and thus allows winning the simple game Hangman when playing in English. 

Note that the script "Hangman_Predicted.py" computes the number of iteration needed to find the most probable possibilities for a randomly selected word. It helps determine the efficiency of the algorithm to narrow down word possibilities for a given word length for instance.

###############

################################
# Software and module required #
################################
- If necessary, download and install or update your system with the latest version of Python 3. This code has been tested with the version 3.7.1 (default, Dec 14 2018). 
- This code needs the following modules : re, copy, operator, nltk, random, sys

################################

#############
# Procedure #
#############
1- Run the file "Hangman_Predict_Input.py"

2-You are asked : "How many letters does your word have?".
Type the number of letter of the word you have to find when asked.

3-You are then asked: "What are the letters you already wrongly guessed"
Type the letters you wrongly guessed if you already began to play Hangman before starting this program. Otherwise, just type : 0

4-We now see the best guess letter. Try this best guess letter in Hangman and type if this letter was in the word (y) or not (n).

5- You are now asked : "What are the letters (a-z) and blank space (0)?
Type the letters of the word you already guessed (if any) while separating letters by 0 when you do do not know the letter. Do not use spaces.

6-You can see the number of remaining possible words. If the number of possibilities is smaller than the threshold for printing all words, you will see a list of all possible words. 

7-Repeat the process above until we reached the threshold of word possibility (here defined to 20) after which the program end and tells us the probable answers as well as the number of iterations.

########################################################################################
