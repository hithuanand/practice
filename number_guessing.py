import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)

guesses = 0
is_running = True

print ("python number guessing game")
print(f"select a number between {lowest_num} and {highest_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess:")
    if guess.isdigit():
        guess = int(guess)
        guesses+= 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
        elif guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too high! Try again")
        else:
            print(f"correct the answer {answer}")
            is_running = False
    else:
        print("invalid guess")
        print(f"pls select a number between {lowest_num} and {highest_num}")
