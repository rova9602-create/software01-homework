user = input("enter your cabin class on a cruise ship: ")
if user=="LUX" :
    print("Upper-deck cabin with a balcony.")
elif user=="A" :
    print("Cabin above the car deck with a window.")
elif user=="B" :
    print("Windowless cabin above the car deck.")
elif user=="C" :
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")