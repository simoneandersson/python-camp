#Exercises 1
# Task 1
print("Hello, Human!")

# Task 2
name = "Simone"
print("Hello, {}!".format(name))

# Task 3
name = input("What is your name? ")
print("Hello, {}!".format(name))

# Task 4
raining = False
if raining:
	print("It's raining! Stay in, code some python")
else:
	print("Sun is shining! Go outside, bring a beer and play some minigolf")

# Task 5
words = ["Hip", "Hip", "Hurray"]
for i in range(3):
	for word in words:
		print(word)

# Task 6
hobby = input("What is your hobby? ")
hobbies = []
while hobby.lower() != "stop":
	hobbies.append(hobby)
	hobby = input("What is your hobby? ")
print("Your hobbies are {}".format(hobbies))

# Task 7
word = input("Enter a word: ")
for i, w in enumerate(word):
	if word.count(w) == 1:
		print(i)
		exit()
print(-1)
