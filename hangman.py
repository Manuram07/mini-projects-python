import random

from art import hangman_word_list
from art import hangstages,hanglogo
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
print(hanglogo)
display = []
lives=6
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
chosen_word = random.choice(hangman_word_list)
word_length = len(chosen_word)
for position in range(word_length):
    display.append("_")
print("Word to guess: "+"".join(display))
game=0
while(game==0):
    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    flag=0
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.
    if guess in display:
        print("You've already guessed " + guess)

    for letter in range(len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter]=guess
            flag=1
    if flag != 1 :
        if guess not in display:
            lives-=1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

    print("Word to guess: "+"".join(display))

    # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
    if "_" not in display:
        game = 1
        print("****************************YOU WIN****************************")
    elif lives == 0:
        game = 1
        print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")



    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(hangstages[lives])