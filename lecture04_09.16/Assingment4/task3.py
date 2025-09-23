user_input = input("Enter a number: ")

if user_input == "":
    print("Execution stopped.")
else:
    number = float(user_input)
    smallest = largest = number

    while True:
        user_input = input("Enter a number: ")
        if user_input == " ":
            break

        number = float(user_input)
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
