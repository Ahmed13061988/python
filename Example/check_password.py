password = input("Enter the password: ")

x = False
if len(password) >= 8:
    for i in password:
        if i.isdigit():
            for j in password:
                if j.isupper():
                    x = True
    if x:
        print("Strong password")

else:
    print("Weak password")
