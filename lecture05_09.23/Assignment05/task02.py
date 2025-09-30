numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    numbers.append(int(user_input))
numbers.sort(reverse=True)

top5 = numbers[:5]
print("The five greatest numbers are:", top5)
