#if

age = int(input("Enter the age:"))

if age >= 18 and age <100:
    print("You are an adult")
elif age < 0:
    print("you haven't even born yet")
elif age >=100:
    print("You are too old")
else:
    print("You are a kid")