fruits = ["apple", "orange", "banana", "coconut"]
vegitables = ["celery", "carrots", "potatos"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegitables, meats]

print(groceries[1][1])

for collections in groceries:
    for food in collections:
        print(food, end=" ")

