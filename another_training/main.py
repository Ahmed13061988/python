import my_functions


mylist = ["a", 'b', "c"]
indexed_list = []
for index, item in enumerate(mylist):
    indexed_list.append((item, index))

print(indexed_list)

