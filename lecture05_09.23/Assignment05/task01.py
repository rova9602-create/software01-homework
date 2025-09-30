import random
user = int(input("How many dice do you want to roll?: "))

rolls = []
for i in range(user):
    roll = random.randint(1, 6)
    rolls.append(roll)

total = sum(rolls)
print("Dice rolls: ", rolls)
print("sum:", total)