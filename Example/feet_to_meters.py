feet_inches = input("Enter feet and inches: ")


def parse(users_input):
    new_data = users_input.split(" ")
    feets = float(new_data[0])
    inches = float(new_data[1])
    return {"feets": feets, "inches": inches}


def convert(feets, inches):
    meters = feets * 0.3048 + inches * 0.0254
    return meters


parsed = parse(feet_inches)
print(convert(parsed['feets'], parsed["inches"]))


