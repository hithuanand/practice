#
# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}")
#     print(f"You are {age} years old")
#     print(f"Happy birthday to {name}")
#     print()
#
# happy_birthday("Bro", 20)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"your bill of ${amount:.2f} is due: {due_date}")

display_invoice("JoeSchmo", 100.01, "01/02")