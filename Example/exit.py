try:
    width = float(input("Enter the width: "))
    length = float(input("Enter the length: "))

    if width == length:
        exit("This is a square")
except ValueError:
    print("The input is invalid")
