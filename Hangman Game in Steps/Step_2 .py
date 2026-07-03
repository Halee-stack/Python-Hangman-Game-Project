import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

# Step-1: Here we will generate a placeholder with the same number of blank spaces as the letters in chosen_word.
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
guess = input("Guess a letter: ").lower()
# Step-2: Here we will create a display that shows the guessed letter in its correct positions and uses _ for all other letters.
display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)