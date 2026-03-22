word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
import random

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input(f'Guess a letter: ').lower()


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

# check if match
letter_match = guess in chosen_word

# loop
for letter_check in chosen_word:
    if letter_check == guess:
        print(f'The chosen word has "{letter_check}", which compared to your letter guess of "{guess}" was: Right')
    if letter_check != guess:
        print(f'The chosen word has "{letter_check}", which compared to your letter guess of "{guess}" was: Wrong')



