import random
import hangman_words
import hangman_art

stages = hangman_art.stages

print(hangman_art.logo)

end_of_game = False
word_list = hangman_words.word_list

# TODO-1.1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_len = len(chosen_word)
print(chosen_word)
guess_list = []

# TODO-2.1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = ['_'] * word_len
# print(display)

# TODO-4.1: - Create a variable called 'lives' to keep track of the number of lives left.
lives = 6

# TODO-1.2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-3.1: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word and
# 'display' has no more blanks ("_"). Then you can tell the user they've won.

print(stages[lives])

while not end_of_game:

    guess = input('Guess a letter: ').lower()
# TODO-1.3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# TODO-2.2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    if guess in display or guess in guess_list:
        print(f"You've already guessed {guess}")
        print(stages[lives])

    elif guess in chosen_word:
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                # print('Right')
                display[index] = guess
        print(stages[lives])
    # else:
        # print('Wrong')

# TODO-4.2: - If guess is not a letter in the chosen_word,
# Then reduce 'lives' by 1.
# If lives goes down to 0 then the game should stop and it should print "You lose."
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print(hangman_art.loose)
            end_of_game = 'True'

    # keep track of letters guessed by player
    guess_list.append(guess)
# TODO-2.3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = 'True'
        print(hangman_art.win)
