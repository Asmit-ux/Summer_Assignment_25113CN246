score = 0

print("Simple Quiz")

answer = input("1. What is the capital of India? ")

if answer == "Delhi":
    score = score + 1

answer = input("2. How many days are there in a week? ")

if answer == "7":
    score = score + 1

answer = input("3. What is 5 + 3? ")

if answer == "8":
    score = score + 1

print("Your Score is:", score, "out of 3")