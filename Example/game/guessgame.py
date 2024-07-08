import random
import json

with open("questions.json", "r") as file:
    content = file.read()
data = json.loads(content)

points = 0
while True:
    for item in data:
        print(item["body"])
        for index, option in enumerate(item["options"]):
            print(index + 1, "-", option)
        answer = int(input("What is the answer?: ").strip())
        item["answer"] = answer
        print(item)
        if answer == item["correct"]:
            print("You are correct!")
            points += 1
        else:
            print("Wrong answer!")
            print(f"You got {points}")
            break
