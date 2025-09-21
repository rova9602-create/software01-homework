import random

number = random.randint(1, 10)

print("Guess the number between 1 and 10")

while True:
    guess = int(input("Your guess: "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You guessed it.")
        break