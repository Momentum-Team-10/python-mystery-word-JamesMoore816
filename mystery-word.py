import random
import string

def initialize_game():
    """This function initializes all game variables."""
    # Boolean flag for starting/stopping the game
    global playing_game
    playing_game = True
    # Boolean flag for winning the game
    global win_flag
    win_flag = False
    # List for storing letters that have been guessed
    global letters_graveyard
    letters_graveyard = []
    # Int for storing number of guesses remaining
    global guesses_remaining
    guesses_remaining = 8
    # String for storing the random mystery word
    global mystery_word
    mystery_word = choose_mystery_word()
    # List for storing the individual letters of the mystery word
    global mystery_word_as_list
    mystery_word_as_list = list(mystery_word)
    # List filled with blank spaces (underscores) to be filled in
    # with letters from the mystery word.
    global mystery_word_blank
    mystery_word_blank = []
    for char in mystery_word_as_list:
        mystery_word_blank.append("_")

def choose_mystery_word():
    """This function returns a random word from text file and
    makes all letters uppercase."""
    with open("words.txt") as file:
        word_bank = file.read()
        word_bank_list = (word_bank.upper()).split()
        return random.choice(word_bank_list)

def guess_letter(letter):
    """This function checks the letter given as an argument to see
    if it is present in the mystery word. If it is, the enumerated list
    version of mystery word provides all indeces of that letter and uses
    those indeces to replace the underscores in the mystery word with
    its respective letter. If the letter is not in the word, it is added
    to the letter graveyard, and the remaining guesses are decremented."""
    if letter in mystery_word_as_list:
        for index, char in enumerate(mystery_word_as_list):
            if char == letter:
                mystery_word_blank[index] = letter
    else:
        if letter not in letters_graveyard:
            letters_graveyard.append(letter)
            global guesses_remaining
            guesses_remaining -= 1
    display()
    if (mystery_word_blank == list(mystery_word)):
        print("Congratulations--you win!")
        global win_flag
        win_flag = True


def prompt_guess():
    """This function takes a user input only if it is a letter, then
    converts that letter to uppercase. If the input is successful, it
    then uses that letter as an argument for the guess_letter function"""
    guessed_letter = input("Please guess a letter: ").upper()
    if guessed_letter in string.ascii_uppercase:
        guess_letter(guessed_letter)
    else:
        print("Please enter one letter.")
        print("")

def initial_display():
    print("Welcome to the mystery word game!")
    print(' '.join(mystery_word_blank))
    print(f"You have {guesses_remaining} guesses remaining")
    print("")

def display():
    print("")
    print(' '.join(mystery_word_blank))
    if len(letters_graveyard) > 0:
        print(f"You have already guessed: {' '.join(letters_graveyard)}")
    print(f"You have {guesses_remaining} guesses remaining")
    print("")

def prompt_to_continue():
    print("")
    player_input = input("Would you like to play again? ")
    if player_input.upper() == 'YES':
        play_game()
    elif player_input.upper() == 'NO':
        global playing_game
        playing_game = False
    else:
        print(player_input)
        print("Please respond with \'YES\' or \'NO\'")

def play_game():
    initialize_game()
    initial_display()
    while guesses_remaining > 0 and win_flag == False:
        prompt_guess()
    if guesses_remaining == 0:
        print(f"You lose! Your mystery word was: {mystery_word}")

def main():
    play_game()
    while playing_game == True:
        prompt_to_continue()
    print("")
    print("Thank you for playing!")

main()