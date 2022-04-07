import random
import time
from words_list import words # IMPORTING THE LIST OF WORDS

def hangman():
    word = random.choice(words)
    letters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = '' # LETTERS THE PLAYER HAS TRIED
    while True:
        main = "" # THE OUTPUT EACH ROUND, GUESSED LETTERS AND UNDERSCORES

        #THE VARIABLE main WILL BE BUILT EVERY ROUND
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You Won!")
            break
        print("Guess the word:", main)
        guess = input().casefold()

        if guess in guessmade:
            print("You Have Tried This Letter Already")
            time.sleep(1)
        if guess in letters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()
        if guess not in word:
            turns = turns - 1
        if turns == 9:
            print("9 turns left")
            print("  --------  ")
        if turns == 8:
            print("8 turns left")
            print("  ---------  ")
            print("      O      ")
        if turns == 7:
            print("7 turns left")
            print("  ---------  ")
            print("      O      ")
            print("      |      ")
        if turns == 6:
            print("6 turns left")
            print("  ---------  ")
            print("      O      ")
            print("      |      ")
            print("     /       ")
        if turns == 5:
            print("5 turns left")
            print("  ---------  ")
            print("      O      ")
            print("      |      ")
            print("     / \     ")
        if turns == 4:
            print("4 turns left")
            print("  ---------  ")
            print("    \ O      ")
            print("      |      ")
            print("     / \     ")
        if turns == 3:
            print("3 turns left")
            print("  ---------  ")
            print("    \ O /    ")
            print("      |      ")
            print("     / \     ")
        if turns == 2:
            print("2 turns left")
            print("  ---------  ")
            print("    \ O /|   ")
            print("      |      ")
            print("     / \     ")
        if turns == 1:
            print("1 turns left")
            print("Last breaths counting. Take care!")
            print("  ---------  ")
            print("    \ O_|/   ")
            print("      |      ")
            print("     / \     ")    
        
        if turns == 0:    
            print("Game Over")
            print("You let a kind man die")
            print("  ---------  ")
            print("      O_|    ")
            print("     /|\     ")
            print("     / \     ")
            print("The Word Was:", word)
            break

name = input("Enter Your Name: ")
time.sleep(1)
print(f"Welcome {name}")
time.sleep(1)
print("=====================")
time.sleep(1)
print("Try To Guess The Word")
hangman()
