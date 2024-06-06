content = ["This is first file", "This is second file", "This is third file"]

files = ["first.txt", "second.txt", "third.txt"]

for i in range(len(files)):
    file = open(f"files/{files[i]}", "w")
    file.write(content[i])
