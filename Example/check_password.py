def strength(password):
    digit = False
    upper = False
    for i in password:
        if i.isupper():
            upper = True
        elif i.isdigit():
            digit = True
    if digit and upper and len(password) >= 8:
        print("Strong password")
    else:
        print("Weak password")


strength("Ahmeal1ihuss")
