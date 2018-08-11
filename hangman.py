word = "camping" #select randomly
tries = 5
secret = list("_______") # Create based on word
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

print("Welcome to Hangman Simone edition!")
print("The word has {} letters and you have {} guesses".format(len(word), tries))
print(secret)

while True:
    guess = input("Guess a letter: ")

    if inWord(guess):
        printSuccess()
    else:
        printFail()

    if "_" not in secret:
        print("Word is completed! You won the game!!")
        exit()
    elif tries == 0:
        print("You have no more guesses! Better luck next time")
        exit()
