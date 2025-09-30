cities = []

for i in range(5):
    city = input(f"Enter city {i+1}: ")
    cities.append(city)

print("\nThe cities you entered are:")
for c in cities:
    print(c)
