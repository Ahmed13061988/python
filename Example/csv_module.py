import csv

with open("files/weather.csv", "r") as file:
    data = list(csv.reader(file))

city = input("Enter a city: ").strip().title()

for row in data:
    if row[0] == city:
        try:
            print(row[1])
        except IndexError:
            print("The index is out of bound")



