talents=int(input("Enter talents: "))
pounds=int(input("Enter pounds: "))
lots=int(input("Enter lots: "))

grams=(talents*20*32*13.3)+(pounds*32*13.3)+(lots*13.3)

kilograms=int(grams/1000)
grams=grams%1000

print(f"The weight in modern units: {kilograms} kilograms and {grams:.2f} grams.")