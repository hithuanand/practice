# while loop
from defer import return_value

#name = input("Enter your name: ")

#if name == "":

#while name == "":
#    print("You did not enter your name")
#    name = input("Enter your name: ")

#print(f"Hello {name}")




#age = int(input("Enter your age: "))

#while age < 0:
#    print("Age cant be negative")
#    age = int(input("Enter your age: "))

#print(f"You are {age} years old")



food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"you like {food}")
    food = input("Enter a food you like (q to quit): ")
print("bye")