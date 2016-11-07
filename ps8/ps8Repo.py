# Problem Set 8

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

## Mechanics: user-defined types, and thinking about them

# [PROBLEM 1]

## We'll go through the process of defining a class to describe a photograph on Flickr.
## We've provided some of the information filled in for this first example.
## Then you'll complete the same structure on your own for a different type of thing.

# The following exercises are a thought exercise to help you think about how you would
# define a class to represent a flickr photo.

# The name of your class will be... 
new_class_name = "Photo"

# An instance of the class will represent one
represents = "photograph on flickr"

# The Photo class should have how many instance variables?
# Let's say you want each Photo to have: a title, an author, and a list of tags.
num_instance_vars = 3 # when you decide this, 
					  # you have to think about what attributes you want to keep track of!

# One method of your class, other than __init__, will be named:
one_class_method = "display_info"

# When invoked, that method will...
method_description = "display all the info about the photo for the user, like the title, author, tags"
also = "There may also be other methods of this class"

total_string = """
The name of my class will be %s. One instance of the class will represent one
%s. The class will have %d instance variables. One method of my class, other 
than __init__, will be named %s. When invoked, that method will 
%s. %s.
""" % (new_class_name, represents, num_instance_vars, one_class_method, method_description, also)
# this line will print out the above paragraph with the information provided above filled in.
print total_string

### Now, do this again by yourself for a car. If you were to define a car class, 
### what might you pick for instance variables and methods?
# The name of your class will be... 
car_class_name = "Vehicle" 
# An instance of the class will represent one
reps = "type of car"
# The class should have how many instance variables?
num_inst_vars = 3
# Write comments noting what some instance variables could represent below -- at least three.
# 1. .make could tell you the make of the car
# 2. .model could tell you the model of the car
# 3. .year could tell you the year your car was made

# One method of your class, other than __init__, will be named...
# Think: anything you want a car to do. 
# Change license registration and print something out? Drive forward? 
car_class_method = "Owner Information"

# When invoked, that method will...
# (Think: How would you represent this method you named above in code or in text 
# for someone to see in a program? 
# Look at the examples given in the textbook and the flickr Photo class above.) 
car_method_description = "display all of the information about the owner of the car like name, age, and gender "

car_str = """The name of this class will be: %s. So you are creating a type %s.
An instance of the class will represent one %s. It should have %d instance
variables. One method of this class will be called %s, which 
will %s.
""" % (car_class_name,car_class_name,reps,num_inst_vars, car_class_method, car_method_description)
print car_str



# [PROBLEM 2]

class Photo():

	def __init__(self, title, author, tags):
		self.title = title
		self.author = author
		self.tags = tags

	def display_info(self):
		retval = "Photo: "
		retval += self.title + "\n"
		retval += "Photographed by: " + self.author + "\n"
		retval += "Tags: "
		for tag in self.tags:
			retval += tag + " "
		return retval
my_photo = Photo(title = "Photo1", author = "Ansel Adams", tags = ["Nature", "Mist", "Mountain"])

## Write code to create an instance of the photo class and store it in the variable my_photo. 
## display_info(my_photo) should produce the following string. HINT: if you just call the constructor 
## for the Photo class appropriately, everything will be taken care of for you. You just have to figure out, 
## from the definition of the class, what to pass to the constructor.


display_string = "Photo: Photo1\nPhotographed by: Ansel Adams\nTags: Nature Mist Mountain "

try:
	test.testEqual(my_photo.display_info(), display_string, "Problem 2")
except:
	print "Failed Test for problem 2; my_photo not bound or code for display_info or display_string was changed"



# ----------------Don't change code in this seciton----------------

## You won't need to change any code below this line. But definitely
## read it and understand it! Hint: Thinking back and looking at the flow chart from
## the first user-played Hangman problem set may help.

# Below is the full set of Hangman code.
# If you run this code without adding or changing anything, 
# the computer will play Hangman on manual mode, so
# if you keep pressing Enter, you can watch it play.

# Try it out! Then you'll build a couple functions that will make this game better.

# this block of code will get a bunch of random words for the computer to choose
# from as the word to guess. Make sure you have the words.txt file downloaded using curl 
# (the UNIX problem last week). Also, make sure you download the 106test.py file, from Canvas.
all_words = []
f = open('words.txt', 'r')
for l in f.readlines():
    all_words.append(l.strip().upper())
f.close()
## just use a subset of the dictionary, to keep the program from running too slow.
random.seed("This is a fixed seed so the random number generator will always pick the same 2000 words. Makes debugging easier.")
all_words = random.sample(all_words, 2000)
# print all_words[0] # should be KEELHAUL


def guess(blanked_word, guesses_so_far, all_words=all_words, version=1, manual=False):
    """Return a single letter (upper case)"""
    # version 1 guesses the letters in alphabetic order
    # version 2 (to be implemented), guesses them in order of frequency of occurrence in the list all_words
    # version 3 (to be implemented), guesses them in order of frequency of occurrence in the list of words that are still possible, given the guesses_made and the current state of the blanked_word
    
    if version == 1:
        guesses = "abcdefghijklmnopqrstuvwxyz".upper()
    elif version == 2:
        guesses = sorted_letters(letter_frequencies(all_words))
    else:
        guesses = sorted_letters(letter_frequencies(possible_words(blanked_word, guesses_so_far, all_words)))
    if manual:
        print "guesses: ", guesses
    for let in guesses:
        if let not in guesses_so_far:
            if manual:
                print "guessing: ", let
            return let
    # if all of the letters to guess have already been guessed, something's gone wrong!
    print "something went wrong! No more letters to guess"
    return None
        
# this function tells you how many guesses you made 
# vs how many guesses you COULD have gotten the word in
def show_results(word, guess_count):
    """Results to show at end of game"""
    print "You got it in " + str(guess_count) + " guesses."
    if guess_count == len(set(list(word))):
        print "Awesome job."
    else:
        print "You could have gotten it in " + str(len(set(list(word)))) + " guesses."

# from ps6        
def blanked(word, revealed_letters):
   blanked_word = "" # assigning the empty string to the blanked_word to be accumulated
   for ch in word:
      if ch in revealed_letters: # if the letter has been revealed
         blanked_word = blanked_word + ch # add that letter to be visible in the blanked word
      else: # otherwise,
         blanked_word = blanked_word + "_" # add a blank
   return blanked_word

# from ps6
def health_prompt(current_health, max_health):
   return "+"*current_health + "-"*(max_health-current_health) # multiplying strings by proper amounts and returning the new, concatenated string

# from ps6
def game_state_prompt(txt, h, m_h, word, guesses):
    """Returns a string showing current status of the game"""
    res = txt + "\n"
    res = res + health_prompt(h, m_h) + "\n"
    if guesses != "":
        res = res + "Guesses so far: " + guesses.upper() + "\n"
    else:
        res = res + "No guesses so far" + "\n"
    res = res + "Word: " + blanked(word, guesses) + "\n"
    return(res)

# Helper function to count how many distinct characters are in the word.
# It is used to determine the minimum number of guesses that are needed
# to guess the word.
def count_distinct_chars(word):
    chars_so_far = ""
    for c in word:
        if c not in chars_so_far:
            chars_so_far = chars_so_far + c
    return len(chars_so_far)
    
#### GAMEPLAY
# This following function makes the computer play the game.
# Note the default parameters, go through the code, and think about what each part means.
def play_game(manual=True, version = 1, max_health = 26):
    """Plays one game"""
    health = max_health
    word = random.choice(all_words)
    word = word.upper() # everything in all capitals to avoid confusion
    guesses_made = ""
    game_over = False

    feedback = "let's get started"

    while not game_over:
        if manual: # if manual is set to true, the user will have to keep pressing enter to keep going with the game
            # now, give the user a chance to see what happened on previous guess
            prompt = game_state_prompt(feedback, health, max_health, word, guesses_made)
            full_prompt = prompt + "Press enter to make the program guess again; anything else to quit\n"
            command = raw_input(full_prompt)
            if command != "":
                # user entered a character, so (s)he wants to stop the game
                return
        # call your function guess to pick a next letter
        next_guess = guess(blanked(word, guesses_made), guesses_made, all_words, version, manual)
        
        # proceed to process the next_guess
        guesses_made = guesses_made + next_guess
        if next_guess in word:
            if blanked(word, guesses_made) == word:
                feedback = "Congratulations"
                game_over = True
            else:
                feedback = "Yes, " + next_guess + " is in the word"
        else: # next_guess is not in the word word
            feedback = "Sorry, " + next_guess + " is not in the word."
            health = health - 1
            if health <= 0:
                feedback = " Waah, waah, waah. Game over."
                game_over= True

    if manual:
        # this is outside the for loop; it happens once game_over is True
        print(feedback)
        print("The word was..." + word)
        if health > 0:
            show_results(word, len(guesses_made))

    return len(guesses_made), count_distinct_chars(word)

# ------------------end of section with code you aren't supposed to change----

## [PROBLEM 3]

play_game(max_health=3)

# Uncomment the line above to make it run the guesser.
# After you've played around with the guesser, change the call to play_game so 
# a game is played with a maximum of 3 wrong guesses before the game ends.
# (Hint: Which parameter affects that?)


# Now, you're going to start making some tools to play Hangman better.

## [PROBLEM 4]

# First, you need to define a function called letter_frequencies.
# This function should take as input:
        # - a list words
# It should return a dictionary whose key value pairs are letters and the number
#   of times each letter appears in the total set of words. For example, {"A":3,"T":6} ...

# NOTE: In the textbook section on training a guesser, we provided a function letter_frequencies
# that takes just a single word as input rather than a list of words. You may want to start with 
# that code and extend it.

# Finish the function definition below, adding parameters and function body.
def letter_frequencies(x):
    d = {}
    for word in x:
        for letter in word:
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1
    return d

# this code helps test whether your letter_frequencies function is working!

test_words = ["HELLO", "GOODBYE"]
r = letter_frequencies(test_words)
try:
    test.testEqual(r['H'], 1, "H occurs once")
    test.testEqual(r['O'], 3, "O occurs three times")
except:
    print "couldn't look up 'H' or 'O' in dictionary r"
    
# --------------

# [PROBLEM 5]

# Now you will define a function sorted_letters.
# It takes a dictionary of the kind returned by
# letter_frequencies(). sorted_letters returns a
# sorted list of the keys, sorted by the associated
# counts, in decreasing order.

def sorted_letters(counts):
    sort_list = counts.keys()
    sorted_list = sorted(sort_list, key = lambda x: counts[x], reverse = True)
    return sorted_list
test_words = ["HELLO", "GOODBYE"]
r = letter_frequencies(test_words)    
try:
    test.testEqual(sorted_letters(r)[:2], ['O', 'E'], "sorted_letters")
except:
    print "sorted_letters is not defined, or there's an error in sorted_letters. Try calling sorted_letters yourself in order to see what the error message is."
 
# Once you pass the tests, make another call to play_game. 
# This time, pass a parameter that tells it to use version 2
# It will call your letter_frequencies function and usually
# guess better than the alphabetic guesser (version 1)
 
# --------------

# [PROBLEM 6]
# Now you will define a function possible that determines
# whether a word is still possible, given the guesses that
# have been made and the current state of the blanked word.
#   If a letter has been guessed but not revealed in the blanked
#   word, that eliminates all words with that letter.
#   If a letter has been guessed and is revealed, that
#   eliminates all words without that letter.

def possible(word, blanked, guesses_made):
    for x in word:
        if x in guesses_made:
            if x not in blanked:
                return False
    for y in guesses_made:
        if y in word:
            if y not in blanked:
                return False
    return True
    

test.testEqual(possible("HELLO", "_ELL_", "ELJ"), True, "possible first test")
test.testEqual(possible("HELLO", "_ELL_", "ELJH"), False, "possible second test")
test.testEqual(possible("HELLO", "_E___", "ELJ"), False, "possible third test")

# --------------

# [PROBLEM 7]

# Now, you should define a function called possible_words.
# This function takes as input 
#    - the blanked word so far,
#    - the string of guesses that have been made so far
#    - the list of all words the game might pick
# It returns a list of words that are still possible to be the word 
#   that needs to be guessed, given this information.

# HINT: You want to return a list of things... what pattern might be useful here?
# HINT 2: make use of the function possible() that you defined in the previous problem

def possible_words(blanked, guesses_made, total_words):
    list_words = []
    for word in total_words:
        if possible(word, blanked, guesses_made):
            list_words.append(word)
    return list_words


test.testEqual(possible_words("_ed", "edj", ["fed", "bed", "led"]), ["fed", "bed", "led"], "possible words")
# if f has been guessed already, then "fed" is no longer one of the possible words
test.testEqual(possible_words("_ed", "edjf", ["fed", "bed", "led"]), ["bed", "led"], "possible words second test")
 
# Once you pass the tests, make another call to play_game. 
# This time, pass a parameter that tells it to use version 3.
# It will call letter_frequencies on only those words that
# are still possible, so it might be a little better than 
# version 2.
    
# --------------

## [PROBLEM 8]

# Now, we are going to see how much better, on average, 
# versions 2 and 3 do.

# play_game returns two values (a tuple):
#   the number of guesses made and 
#   the minimum number of guesses that were required

# To get a sense of the average performance,
# we will have each guesser play the game 30 times. 
# We accumulate the total number of guesses that were made and the
# minimum number that were required, across all 30 games. 
# You'd get really bored having to hit Enter a lot of times.
# To avoid that, we set manual=False in the calls to play_game()
#(Note: it may take a while to complete 30 games on 
# versions 2 and 3, especially if you have an older computer).

# We have provided the code below, commented out. You should first 
# remove all the # signs, so that it runs. 
# The graded part is to comment it, 
# line by line, explaining what each line does.


for v in [1, 2, 3]:
    print "----version", v
    # This line iterates through each version and will print which one we are currently running.
    total_guesses = 0
    # This line creates an accumulation for the total guesses made in the game.
    total_min_guesses = 0
    # This line creates an accumulation for the least amount of total guesses needed.
    
    for i in range(30):
        print i, ".",
        # These two lines iterate though each game play and runs 30 times, each integer followed by a periodrepresents one game play.
        
        (guesses, min_guesses) = play_game(version = v, manual=False)
        # This line is where the game is played.
        
        total_guesses = total_guesses + guesses
        # This line will will give us the total amount of guesses to get the word.
        total_min_guesses = total_min_guesses + min_guesses
        # This line will give us the total minimum amount of guesses needed for the word.
    print
    print "ratio:", total_guesses / float(total_min_guesses), ";total guesses:", total_guesses, ";min needed:", total_min_guesses
    # These two lines print our data output. The ratio is the average amount of incorrect guesses for correct guesses, then it prints the total amount of guesses needed and then the minimum amount of guesses that could have been asked.

# --------------

# Now we're going to ask you to make small extensions to the Tamagotchi program from the textbook. We have reproduced the code for that game here.

from random import randrange

class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = 11
        self.boredom = 6
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print self.sounds[randrange(len(self.sounds))]
        self.update_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.update_boredom()

    def feed(self):
        self.update_hunger()

    def update_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def update_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None # no pet matched

def play():
    animals = []

    option = ""
    while True:
        action = raw_input("""
        Quit
        Adopt <petname_with_no_spaces_please>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>
        Here <petname>

        Choice: """)

        words = action.split()
        if len(words) > 0:
        	command = words[0]
        else:
        	command = None
        if command == "Quit":
            print("Exiting...")
            return
        elif command == "Adopt" and len(words) > 1:
            if whichone(animals, words[1]):
                print "You already have a pet with that name"
            else:
                animals.append(Pet(words[1]))
        elif command == "Greet" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                print "I didn't recognize that pet name. Please try again."
            else:
                pet.hi()
        elif command == "Teach" and len(words) > 2:
            pet = whichone(animals, words[1])
            if not pet:
                print "I didn't recognize that pet name. Please try again."
            else:
                pet.teach(words[2])
        elif command == "Feed" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                print "I didn't recognize that pet name. Please try again."
            else:
                pet.feed()
        elif command == "Here" and len(words) > 1:
            pet = whichone(animals, words[1])
            if pet.hunger >= 10:
                print "You know, you really should feed me!"
            else:
                print "Wow, I'm stuffed!"
            if pet.boredom >= 5:
                print "I wish you would pay attention to me!"
            else:
                print "You know, you don't always have to be around me."
        else:
            print "I didn't understand that. Please try again."

        for pet in animals:
            pet.clock_tick()
            print pet

play()

## [PROBLEM 9]

## First, change the program so that new pets always start out hungry and bored rather than starting out with a random level of hunger and boredom.


## [PROBLEM 10]

## Next, make pets respond to one additional command, of the form "Here <petname>". When given that command, make the pet do something (i.e., print something and/or change its state). Make it do something different depending on whether it is hungry or bored or not. Feel free to be creative here.

