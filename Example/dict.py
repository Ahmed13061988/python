b = {}

is_true = False

is_false = True

name = "Ahmed"


if not is_true:
    is_true = True

if not is_false:
    is_false = False

b["True"] = is_true
b["False"] = is_false
b["name"] = name
print(b)

name1 = b["name"]

print(name1)

