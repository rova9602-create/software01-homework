numbers = []

while True:
    user_input = input("Enter a number: ")

    if user_input == " ":
        break

    number = float(user_input)
    numbers.append(number)

if numbers:
    smallest = min(numbers)
    largest = max(numbers)
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
else:
    print("Execution stopped.")
