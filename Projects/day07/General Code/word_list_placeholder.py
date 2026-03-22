import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

guess = input("Guess a letter: \n").lower()

# store len of chosen word
chosen_word_len = int(len(chosen_word))

placeholder = ''

for number in range(chosen_word_len):
    placeholder += '_'

print(f'\nHint: {placeholder}\n')

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

display = ''

for letter in chosen_word:
    if letter == guess:
        display += letter
        print(f'Display print for right: {display}')
    else:
        display += '_'
        print(f'Display print for wrong: {display}')


print(f'\nFinal display print: {display}')

