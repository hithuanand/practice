
principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount"))
    if principle <= 0:
        print("Principle cant be less than equal to zero")

while rate <= 0:
    rate = float(input("Enter the rate"))
    if rate <= 0:
        print("rate cant be less than equal to zero")

while time <= 0:
    time = int(input("Enter the rate"))
    if time <= 0:
        print("time cant be less than equal to zero")


print(principle)
print(rate)
print(time)

total = principle * pow((1+rate/100), time)

print(f"Balance after {time} years : $ {total:.2f}")