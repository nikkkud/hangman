# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_secret_word = set(secret_word)
    if (letters_secret_word & set(letters_guessed) == letters_secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_secret_word = set(secret_word)
    not_guessed_letters = letters_secret_word - set(letters_guessed)
    guessed_word = secret_word

    for letter in not_guessed_letters:
        guessed_word = guessed_word.replace(letter, '_ ')

    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    available_letters = string.ascii_lowercase
    for letter in letters_guessed:
        available_letters = available_letters.replace(letter, '')
    return available_letters


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    vowels = {'a', 'e', 'i', 'o'}
    count_guesses = 6
    all_input_letters = []
    letters_guessed = []
    get_word_output = get_guessed_word(
        secret_word, letters_guessed)
    count_warning = 3
    letters_secret_word = set(secret_word)
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print(f'You have {count_warning} warnings left.')

    while count_guesses > 0 and is_word_guessed(secret_word, letters_guessed) != True and count_warning > -1:

        available_letters = get_available_letters(all_input_letters)

        print(f'You have {count_guesses} guesses left.')
        print(f'Available letters: {available_letters}')
        input_letter = input('Please guess a letter: ').lower()

        if (len(input_letter) == 1):
            all_input_letters.append(input_letter)
            if (input_letter in available_letters):
                if (input_letter in letters_secret_word):
                    letters_guessed.append(input_letter)
                    get_word_output = get_guessed_word(
                        secret_word, letters_guessed)
                    print(f'Good guess: {get_word_output}')
                    print('----------')
                else:
                    if (input_letter in vowels):
                        count_guesses -= 2

                    else:
                        count_guesses -= 1
                        print(
                            f'Oops! That letter is not in my word: {get_word_output}')
                        print('----------')
            else:
                count_warning -= 1
                if (count_warning <= -1):
                    print(
                        f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {get_word_output}")
                else:
                    print(
                        f'Oops! That is not a valid letter. You have {count_warning} warnings left: {get_word_output}')
                    print('----------')
        else:
            print(
                f"Oops! You can write only one letter from the English alphabet: {get_word_output}")
            print('----------')

    if (is_word_guessed(secret_word, letters_guessed)):

        print('Congratulations, you won!')
        print(
            f'Your total score for this game is: {count_guesses * len(letters_secret_word)}')
    elif (count_guesses <= 0):
        print("Sorry, you ran out of guesses. The word was else.")


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    list_other_word = list(other_word)
    list_word = list(my_word.replace(" ", ""))

    # This code checks that the numbers of letters was the same.
    # Without this code it might happen that in hints words will be word with more numbers of the same letters than in a guessed string.
    # For example, if we have '_ _ ee' and ask for a hint than we'll get 'epee'. This isn't correct hint cause we showed all available 'e' in word in the guessed string.
    # To avoid it i wrote the func below.
    def check_letters(guessed_word, hint_word):
        guessed_word_set = set(guessed_word)
        guessed_word_set.discard('_')
        for letter in guessed_word:
            if letter in string.ascii_lowercase:
                if guessed_word.count(letter) != hint_word.count(letter):
                    return False

    if (len(list_word) == len(list_other_word)):
        for idex, letter in enumerate(list_word):
            if (letter in list(string.ascii_lowercase)):
                if (letter != list_other_word[idex]):
                    return False
        return False if check_letters(my_word, other_word) == False else True
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    coincidences = []
    for word in wordlist:
        if (match_with_gaps(my_word, word)):
            coincidences.append(word)
    if (len(coincidences) != 0):
        for word in coincidences:
            print(word, end=" ")
    else:
        print('No matches found')


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    vowels = {'a', 'e', 'i', 'o'}
    count_guesses = 6
    all_input_letters = []
    letters_guessed = []
    get_word_output = get_guessed_word(
        secret_word, letters_guessed)
    count_warning = 3
    letters_secret_word = set(secret_word)
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print(f'You have {count_warning} warnings left.')

    while count_guesses > 0 and is_word_guessed(secret_word, letters_guessed) != True and count_warning > -1:

        available_letters = get_available_letters(all_input_letters)

        print(f'You have {count_guesses} guesses left.')
        print(f'Available letters: {available_letters}')
        input_letter = input('Please guess a letter: ').lower()

        if (len(input_letter) == 1):
            all_input_letters.append(input_letter)
            if ((input_letter in available_letters) or input_letter == '*'):
                if (input_letter == '*'):
                    show_possible_matches(get_word_output)
                    print(' ')
                    print(('----------'))
                else:
                    if (input_letter in letters_secret_word):
                        letters_guessed.append(input_letter)
                        get_word_output = get_guessed_word(
                            secret_word, letters_guessed)
                        print(f'Good guess: {get_word_output}')
                        print('----------')
                    else:
                        if (input_letter in vowels):
                            count_guesses -= 2

                        else:
                            count_guesses -= 1
                            print(
                                f'Oops! That letter is not in my word: {get_word_output}')
                            print('----------')
            else:
                count_warning -= 1
                if (count_warning <= -1):
                    print(
                        f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {get_word_output}")
                else:
                    print(
                        f'Oops! That is not a valid letter. You have {count_warning} warnings left: {get_word_output}')
                    print('----------')
        else:
            print(
                f"Oops! You can write only one letter from the English alphabet: {get_word_output}")
            print('----------')

    if (is_word_guessed(secret_word, letters_guessed)):

        print('Congratulations, you won!')
        print(
            f'Your total score for this game is: {count_guesses * len(letters_secret_word)}')
    elif (count_guesses <= 0):
        print("Sorry, you ran out of guesses. The word was else.")


if __name__ == "__main__":

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
