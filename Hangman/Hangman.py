import csv
import random
with open('Dictionary.csv') as f:
    again = 'y'
    print("----------WELCOME TO THE HANGMAN GAME----------")

    def figure(guesses):
        if (guesses == 0):
            print("_____________")
            print("|	 |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|________")
        elif (guesses == 1):
            print("_____________")
            print("|	 |")
            print("|         O")
            print("|")
            print("|")
            print("|")
            print("|________")
        elif (guesses == 2):
            print("_____________")
            print("|	 |")
            print("|         O")
            print("|         |")
            print("|         |")
            print("|")
            print("|________")
        elif (guesses == 3):
            print("_____________")
            print("|	 |")
            print("|         O")
            print("|        \|")
            print("|         |")
            print("|")
            print("|________")
        elif (guesses == 4):
            print("_____________")
            print("|	 |")
            print("|         O")
            print("|        \|/")
            print("|         |")
            print("|")
            print("|________")
        elif (guesses == 5):
            print("_____________")
            print("|	 |")
            print("|         O")
            print("|        \|/")
            print("|         |")
            print("|        / ")
            print("|________")
        elif (guesses == 6):
            print("_____________")
            print("|	 |")
            print("|         O")
            print("|        \|/")
            print("|         |")
            print("|        / \ ")
            print("|________")

    while again == 'y' or again == 'Y':
        reader = csv.reader(f)
        row = random.choice(list(reader))
        word = row[0]
        allowed_errors = 6
        guesses = []
        found = False

        while not found:
            for letter in word:
                if letter.lower() in guesses:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
            print("")
            if allowed_errors == 6:
                figure(6-allowed_errors)
            guess = input(f"\nGuesses left: {allowed_errors}, Next letter: ")
            print("")
            guesses.append(guess.lower())
            if guess.lower() not in word.lower():
                allowed_errors -= 1
                figure(6-allowed_errors)
                if allowed_errors == 0:
                    break

            found = True
            for letter in word:
                if letter.lower() not in guesses:
                    found = False

        if found:
            again = input(f"Alas! You win. The word is {word}. \nPlay again(y/n): ")
        else:
            again = input(f"Sorry, Game Over! The word is {word}.\nTry again(y/n): ")

    print("Thank you !")
