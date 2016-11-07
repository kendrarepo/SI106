# Problem Set 7

## NOTE: Be sure to download the file test106.py into the same directory where you have this file saved
import test106 as test
import random

sname = "Kendra Repo"
print sname # this is a helpful double-check for us when we are grading

## NOTE: All places where you have to do work/write a comment/change code/add code
##       in this problem set are marked with the word "PROBLEM". If you're looking
##       for where you need to add code and get confused, search for that, and read
##       the code and directions around it to understand the context of what you need
##       to do!

##########

## [PROBLEM 1] - Unix problems

# Run the unix curl program to download the
# list of all valid scrabble words by typing:
# curl http://www.puzzlers.org/pub/wordlists/ospd.txt
# Then run it again and save the output to a file called words.txt:
# curl http://www.puzzlers.org/pub/wordlists/ospd.txt > words.txt
#Be sure to save the file in the same directory where you have this file saved.
#You do not need to submit words.txt, but will use the file later in this problem set.

# ----------------

## SORTING EXERCISES

# ----------------

## [PROBLEM 2] 

fall_list = ["leaves","apples","autumn","bicycles","pumpkin","squash","excellent"]

# Write code to sort the list fall_list in reverse alphabetical order. 
# Assign the sorted list to the variable sorted_fall_list.
sorted_fall_list = sorted(fall_list, reverse = True)
# Now write code to sort the list fall_list by length of the word, longest to shortest.
# Assign this sorted list to the variable length_fall_list.
length_fall_list = sorted(fall_list, key = lambda x: len(x), reverse = True)
#NOTE: Please do not adjust any of the try/except code.
try:
    test.testEqual(sorted_fall_list[0], 'squash', "squash first")
    test.testEqual(length_fall_list[0], 'excellent', "excellent first")
except:
    print "sorted_fall_list or length_fall_list don't exist or have no items"

# -----------------

## [PROBLEM 3]

food_amounts = [{"sugar_grams":245,"carbohydrate":83,"fiber":67},{"carbohydrate":74,"sugar_grams":52,"fiber":26},{"fiber":47,"carbohydrate":93,"sugar_grams":6}]

# Write code to sort the list food_amounts by the key "sugar_grams", from lowest to highest.
# Assign the sorted list to the variable sorted_sugar.

sorted_sugar = sorted(food_amounts, key = lambda x: x["sugar_grams"])

# Now write code to sort the list food_amounts by 
# the value of the key "carbohydrate" minus the value of the key "fiber" in each one, from lowest to highest.
# Assign this sorted list to the variable raw_carb_sort.

raw_carb_sort = sorted(food_amounts, key = lambda x: (x["carbohydrate"]-x["fiber"]))

try:
    test.testEqual(sorted_sugar[0], food_amounts[2], "sorted_sugar test")
    test.testEqual(raw_carb_sort[0], food_amounts[0], "raw_carb_sort test")
except:
    print "sorted_sugar or raw_carb_sort don't exist or have no items"

# -------------------

## [PROBLEM 4]

# There are 19 3-letter words in the Scrabble dictionary that contain the letter 'z'.
# Write code to generate a list of them, sorted in reverse alphabetic order (i.e., 'zoo' first and 'adz' last)
# Save that list in a variable called 'short_z_words'.
# Use the words.txt file that you downloaded using the curl command.
# NOTE: to get rid of the blank line character at the end of each line in the file, use the .strip() method.
scrabble = open("words.txt","r")
scrabblelst = scrabble.readlines()
p = []
for line in scrabblelst:
    p.append(line.strip())
u = []
for word in p:
    if len(word) == 3 and 'z' in word:
        u = u + [word]
short_z_words = sorted(u, reverse = True)  
scrabble.close()    
try:
    test.testEqual(short_z_words[0:2], ['zoo', 'zoa'], "short_z_words")
except:
    print "Couldn't test short_z_words because it's not defined or has less than 2 items"

# --------------------

## [PROBLEM 5]

# Write code to generate a list of the 10 highest-scoring words from the Scrabble dictionary that contain the
# letter 'z'. Save it in the variable best_z_words.
# You may assume there are no bonuses that double or triple letter values or entire words.
# HINT: In the textbook section on Accumulating Results from a Dictionary, there is code that computes
# the scrabble score for the entire text of "A Study in Scarlet". You may want to adapt that.

letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10}

y = {}
for word in p:
    if 'z' in word:
        y[word] = 0

n = {}
score = 0
for key in y:
    for char in key:
        score = score +letter_values[char]
    n[key] = score 

ordered = sorted(n, reverse = True)
best_z_words = ordered[0:10]
try:
    test.testEqual(best_z_words[0:2], ['zyzzyvas', 'zyzzyva'], "best_z_words")
except:
    print "Couldn't test best_z_words because it's not defined or has less than 2 items"