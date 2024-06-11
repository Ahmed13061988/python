def average_of_numbers():
    with open("numbers.txt", "r") as file:
        data = file.readlines()
        numbers = data[1:]
        print(numbers)
        x = 0
        for i in numbers:
            x += int(i)
    average = x / len(numbers)
    return average


the_average = average_of_numbers()
print(the_average)
