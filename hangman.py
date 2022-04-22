import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly choose something from list of file name word.py
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # a letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    lives = 6

    # get the user input
    while len(word_letters) > 0 and lives > 0:
        # letter used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        # what the current word is i.e W - R D
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")
            else:
                lives = lives - 1 # take away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print("You have already used that character.Please try again")
        else:
            print("Invalid character. Please try again")

    # get here when len(word_letters ==0) or lives == 0
    if lives == 0:
        print("You died, Sorry. The word was", word)
    else:

        print("You have guessed the word", word,'!!')


if __name__ == '__main__':
    hangman()