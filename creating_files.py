date = input("Enter today's date: ")
rate = input("How do you rate your day from 1-10? ")

thoughts = input("Let your thoughts flow: ")

with open(f"{date}.txt", "w") as file:
    file.write(thoughts + "\n")
    file.write(rate)
