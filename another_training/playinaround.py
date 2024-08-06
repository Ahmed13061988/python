first = ["ali", "hassan"]
second = ["ali", "jasim", "3abas"]

new_list = [name for name in second if name in first]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 12, 23, 43, 432, 25321, 222, 3553232, 85423, 0]

even_numbers = [even for even in numbers if even % 2 == 0]

odd_numbers = [odd for odd in numbers if odd % 2 != 0]

print("even numbers: ", even_numbers)

print("odd numbers: ", odd_numbers)


