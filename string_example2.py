#validate user input exercise
# 12 chare
# no space
# no digit

username = input("Enter a username: ")

if len(username) > 12:
    print("Username has more than 12 chara")
elif not username.find(" ") == -1:
    print("username has spaces")
elif not username.isalpha():
    print("cant contain numbers")
else:
    print(f"welcome {username}")