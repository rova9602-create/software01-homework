names=[]

while True:
    name=input("Enter a name: ")
    if name =="":
        print("Goodbye")
        break
    if name in names:
        print("the name exist")
    else:
        print("New name")
        names.append(name)

print("\nUnique name:")
for n in names:
    print(n)