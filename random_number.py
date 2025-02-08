import random

# print(help(random))

low = 1
high = 100
options = ("rock", "paper", "scissors")
# number = random.randint(low,high)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# option = random.choice(options)
# print(number)
random.shuffle(cards)
# print(option)

print(cards)