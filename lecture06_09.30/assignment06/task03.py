airports={}

while True:
    print("\noptions:")
    print("1. Enter a new airport")
    print("2. Fetch existing airport")
    print("3. Quit")

    number=input("Choose number: ")
    if number=="1":
        icao=input("Enter ICAO code: ")
        name=input("Enter airport name: ")
        airports[icao]=name
        print("Airport Saved!")

    elif number=="2":
        icao=input("Enter ICAO code: ")
        if icao in airports:
            print(airports[icao])
        else:
            print("Invalid ICAO code")

    elif number=="3":
        print("Goodbye")
        break

    else:
        print("Invalid number")

