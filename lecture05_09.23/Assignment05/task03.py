num = int(input("Enter an integer: "))

if num < 2:
    print(f"{num} is not a prime number.")
else:

    divisors = list(range(2, num))

    is_prime = True

    for i in divisors:
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
