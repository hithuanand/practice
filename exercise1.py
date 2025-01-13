#area of a rectangle

length = float(input("Enter the length:"))
width = float(input("Enter the width:"))
area = length*width  #TypeError
print(f"Area is {area} sq-cm")

#shopping cart
item = input("What item would you like to buy?")
price = float(input("What is the price?"))
quatity = int(input("How many would you like?"))
total = price*quatity
print(f"You have bought {item} items, your total is ${total}")


