# python weight converter

weight = float(input("Enter your weight"))
unit = input("Kilograms or pounds? (k or L):")

if unit == "k":
    weight = weight*2.205
    unit = "Lbs"
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs"
else:
    print(f"your {unit} is not valid")

print(f"Your weight is {weight} {unit}")