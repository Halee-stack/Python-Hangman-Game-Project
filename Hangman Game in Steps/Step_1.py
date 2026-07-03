# How to Build Hangman game using just Python. 

import random
word_list = ["aardvark", "baboon", "camel"]

# Step-1 -  Here we will use a random choice from word_list, store it in chosen_word, and print the value of chosen_word.
chosen_word = random.choice(word_list) 
print(chosen_word)

# Step-2 - Here we will get a letter guess from the user, assign it to the variable guess, and convert the input to lowercase before storing it.
guess = input("Guess a letter: ").lower()
print(guess)

# Step-3 - Verify whether the letter stored in guess exists in chosen_word. Display "Right" when the guess is correct, and "Wrong" when it is not.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")