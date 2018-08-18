import random

words = ["camping", "sweden", "bicycle", "programming", "sunshine"]
word, secret = "", ""
tries = 5
used = []

def inWord(letter):
    global tries, secret
    used.append(letter)
    if word.count(letter) == 0:
        tries = tries - 1
        return False
    else:
        for i, l in enumerate(word):
            if l == letter:
                secret[i] = letter
        return True

def printSuccess():
    print("Yeay! The letter exist")
    printStatus()


def printFail():
    print("Nooo! The letter does not exist")
    printStatus()

def printStatus():
    global secret, tries, used
    print("{} - guesses left {} - Already guessed {}".format(secret, tries, used))
    print()

def setup():
    global secret, word, used
    word = random.choice(words)
    secret = ["_"] * len(word)
    tries = 5
    used = []

    print("The word has {} letters and you have {} guesses".format(len(word), tries))
    print(secret)
    print()

def play():
    guess = input("Guess a letter: ")
    if inWord(guess):
        printSuccess()
    else:
        printFail()

def again():
    again = int(input("Do you want to play again type 1, if you want to exit type 2: "))

    if again == 1:
        setup()
    else:
        exit()


print("Welcome to Hangman Simone edition!")
setup()

while True:
    play()

    if "_" not in secret:
        print("Word is completed! You won the game!!")
        again()
    elif tries == 0:
        print("You have no more guesses! Better luck next time")
        again()
