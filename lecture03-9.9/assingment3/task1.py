
length=float(input("How many centimeters is the zender?: "))
legal_limit = 42
if length < legal_limit:
    short_by = legal_limit - length
    print(f"you need to release that zender because it is {legal_limit-length} cm shorter than legal limit")
else:
    print("you can keep the zender.")