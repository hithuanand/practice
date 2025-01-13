#variables - string, integer, float and boolean

first_name ="Hithu"
print(first_name)
food = "pizza"
email = "hithuanand@gmail.com"

print(f"Hello {first_name}") # f- format
print(f"Hello {first_name}, you like {food}. your email is {email}")

#Integers

age = 25  #note no quotes
quatity = 3
num_of_students = 45
print(f"you are {age} years")
print(f"you are buying {quatity} items")
print(f"your class has {num_of_students} students")

#float
price = 10.99
gpa = 9.8
distance =8.5
print(f"The price is ${price}")
print(f"your gpa is {gpa}")
print(f"you have run {distance}kMs")

#Boolean
#is_studnt = True
is_studnt = False
#print(f"Are you a student?")
if is_studnt:
    print(f"you are a student")
else:
    print(f"you are not a student")

for_sale = True

if for_sale:
    print(f"That item is for sale")
else:
    print(f"That item is not for sale")

is_online = True

if is_online:
    print(f"You are online")
else:
    print(f"you are offline")
    