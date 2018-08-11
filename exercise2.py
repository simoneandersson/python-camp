# Exercise 2
# Task 1
def foods(food_one, food_two):
	print("Mm you like {}-{}".format(food_one, food_two))

food_one = input("Enter your favorit food: ")
food_two = input("Enter your second favorit food: ")
foods(food_one, food_two)

# Task 2
cost = int(input("What is the price? "))
if cost < 100:
	tip = cost * 0.1
else:
	tip = cost * 0.05
print("Suggested tip {}, and total sum {}".format(tip, cost + tip))

# Task 3
import random

fortunes = ["Njut av varje dag, man vet aldrig när man får vara med på nästa python läger!", "De ska vara gött å leva", "Du kommer att bli Python pro", "Du kommer bli rik"]
print("Your fortune is: {}".format(random.choice(fortunes)))

# Task 4
start = int(input("Enter a starting number: "))
end = int(input("Enter a endinging number: "))
for i in range(start + 1, end):
	print(i)

# Task 5
word = input("Enter a word: ")
print("The word backward is: {}".format(word[::-1]))
