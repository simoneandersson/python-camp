

print("Welcome to this awesome game")
answer = input("Do you like apples? (Answer yes or no)" ).lower()

if answer == "yes":
    print("You like apples!")
elif answer == "no":
    print("You do not like Apples!")
    answer = input("Do you hate apples? (Answer yes or no) ").lower()
    if answer == "yes":
        print("You hate apples!")
    elif answer == "no":
        print("You do not hate Apples! You just dont like them")
    else:
        print("You did not answer with a yes or no!")
else:
    print("You did not answer with a yes or no!")