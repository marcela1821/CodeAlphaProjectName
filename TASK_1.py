#list of words

import random # we need this to draw a word from the list 
words = ["cat", "dog", "bee", "rabbit", "horse"]

#random word

word_to_guess = random.choice(words) # we choose a random word from the list
guessed_letters = [] # the list of letters that the player already guessed 
wrong_guesses = 0 # how many times the player got sth wrong
max_wrong = 6 # max number of errors

#the hidden word we disply as "_ _ _ _"

display_word = ["_"] * len(word_to_guess)

print("Welcome to Hangman!")
print("Guess the word, one letter at a time")

# the main loop - until the player looses or guess the word 

while wrong_guesses < max_wrong and "_" in display_word:
    print("\nWord:",  " ".join(display_word)) #the current state of the owrd 
    print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
    guess = input("Enter a letter: "). lower()

#we check if the player provided ONE letter 
    if not guess.isalpha() or len(guess) !=1:
        print("Please enter a single ltter.")
        continue

#we check if the letter was already guessed
    if guess in guessed_letters: 
        print("You have already guesses that letter.")
        continue
#we add the letter to the list of used letters 
    guessed_letters.append(guess)

#is the letter in the word?
    if guess in word_to_guess:
        print("Good!")
        #if so, we show it in the correct place
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong!")
        wrong_guesses += 1 #we make the number of mistakes bigger 

if "_" not in display_word:
    print("\n Congratulations! You guessed the word:!", word_to_guess)
else:
    print("\n You loose! The correct word is: ", word_to_guess)    
                           


