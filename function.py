#
# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}")
#     print(f"You are {age} years old")
#     print(f"Happy birthday to {name}")
#     print()
#
# happy_birthday("Bro", 20)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"your bill of ${amount:.2f} is due: {due_date}")
#
# display_invoice("JoeSchmo", 100.01, "01/02")


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("spongebob", "squarepants")

print(full_name)