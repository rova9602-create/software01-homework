import math

def pizza_unit_price(diameter_cm, price_euro):
    radius_m = (diameter_cm / 100) / 2
    area_m2 = math.pi * radius_m ** 2
    unit_price = price_euro / area_m2
    return unit_price

def main():
    print("Pizza 1:")
    d1 = float(input("Enter diameter (cm): "))
    p1 = float(input("Enter price (€): "))

    print("Pizza 2:")
    d2 = float(input("Enter diameter (cm): "))
    p2 = float(input("Enter price (€): "))

    unit1 = pizza_unit_price(d1, p1)
    unit2 = pizza_unit_price(d2, p2)

    print(f"Pizza 1 unit price: {unit1:.2f} €/m²")
    print(f"Pizza 2 unit price: {unit2:.2f} €/m²")

    if unit1 < unit2:
        print("Pizza 1 is better value for money.")
    elif unit2 < unit1:
        print("Pizza 2 is better value for money.")
    else:
        print("Both pizzas offer the same value.")

main()
