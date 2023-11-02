
import time

# welcoming the user
name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")

# wait for 1 second
time.sleep(1)

print("The game is starting...")
time.sleep(0.5)

#You can select any word to play with.
word = ("Python")

# creates an variable with an empty value
guesses = ''

# determine the number of attempts
attepmts = 10

# Create a while loop

# check if the turns are more than zero
while attepmts > 0:

    # make a counter that starts with zero
    failed = 0

    # for every character in secret_word
    for char in word:
        if char in guesses:
            print(char, end=""),

        else:
            # if not found
            print("_", end=""),
            failed += 1

    if failed == 0:
        print(" You won :) CONGRATULATIONS!!")
        # exit the script
        break
        # ask the user go guess a character
    guess = input(" Guess a Character: ")

    # set the players guess to guesses
    guesses += guess

    if guess not in word:
        # attempts counter decreases with 1 (now 9)
        attepmts -= 1
        print("Wrong Guess!!!")

        # how many turns are left
        print("You have", + attepmts, 'more guesses')

        # if the turns are equal to zero
        if attepmts == 0:
            print(" You lost :(")