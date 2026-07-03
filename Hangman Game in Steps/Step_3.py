import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)


# Step 1 Instructions:
# Here we will use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word.
# At the point display has no more balnks("_"). Then you can tell the user thye have won the game. 
# Step-1: - Use a while loop to let the user guess again.

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""




# Step 2 Instructions:
# Update the for loop so that previous guesses are added to the display String.
# At the moment, when the user makes a new guess, the previous guess gets replaced by a "_". We need to fix that by updating the for loop. 
# Step-2: Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    
    if "_" not in display:
        game_over = True
        print("You win.")

