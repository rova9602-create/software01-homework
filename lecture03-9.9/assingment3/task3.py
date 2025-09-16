gender = input("Enter your biological gender: ")
hemoglobin = float(input("Enter your hemoglobin level: "))

if gender =="female":
    if hemoglobin < 117:
        print("Hemoglobin level is low.")
    elif hemoglobin <= 155:
        print("Hemoglobin level is normal.")
    else:
        print("Hemoglobin level is high.")

elif gender =="male":
    if hemoglobin < 134:
        print("Hemoglobin level is low.")
    elif hemoglobin <= 167:
        print("Hemoglobin level is normal.")
    else:
        print("Hemoglobin level is high.")

else:
    print("Invalid gender.")