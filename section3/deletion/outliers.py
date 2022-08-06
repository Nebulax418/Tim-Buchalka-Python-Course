# best practice
data = [2, 4, 5, 22, 33, 99, 100, 223, 783, 822, 934, 988, 2221, 3000, 4000, 7000]


# data = sorted([2, 4, 5, 22, 33, 99, 100, 223, 783, 822, 934, 988, 2221])
# makes a new copy of the list which we do not want

del data[0:2]
print(data)

del data[12:]
print(data)

# values should be 100 and 200 inclusive

min_valid = 100
max_valid = 200

for index, value in enumerate(data):
    if (value < min_valid) or (value > max_valid):
        # delets the data at the index
        del data[index]

print(data)

# deleting items from a list while iterating forward over it will cause problems
# due to the index replacmeentns being messed up

# be careful when changing the size of an iterable in a for loop