from wonderwords import RandomWord
import hangman_art

print(hangman_art.logo)
print(hangman_art.stages[-1])

num_of_lives = 6

# Get random word
rw = RandomWord()
word = rw.word().lower()

print(word)
# print(hangman_art.stages[0])
# print(len(hangman_art.stages))


# Get length of word and have underscore
blank_word = ['_'] * len(word)

while num_of_lives > 0:
    # Get users guess for the letter
    user_guess = input("Guess a letter: ").lower()

    #   If the users guess is incorrect deducte from the life
    if user_guess not in word:
        num_of_lives -= 1

    #   Else the user guess is correct replace the correct underscores with the correct letter
    else:
        print('correct')
        for index, letter in enumerate(word):
            if user_guess == letter:
                blank_word[index] = letter

    print(hangman_art.stages[num_of_lives])
    print(blank_word)

    if '_' not in blank_word:
        print(hangman_art.win)
        exit()


print(hangman_art.loose)