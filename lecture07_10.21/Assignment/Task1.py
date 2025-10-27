import random

def roll_dice():
    result = random.randint(1, 6)
    return result

def main():
    print("Rolling the dice until we get 6...")
    result = 0
    while result != 6:
        result = roll_dice()
        print("You rolled:", result)

main()
