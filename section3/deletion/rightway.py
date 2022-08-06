# data = [2, 4, 5, 22, 33, 99, 100, 223, 783, 822, 934, 988, 2221, 3000, 4000, 7000]
# data = [2, 4, 5, 22, 33, 99, 100, 223, 783, 822, 934, 988, 2221, 3000]
# data = [5, 22, 33, 99, 100, 223, 783, 822, 934, 988, 2221, 3000]
# data = [99, 100, 223, 783, 822, 934, 988]
data = [9999, 10000, 12000, 50000, 8000]


min_valid = 50 # less than 50
max_valid = 1000 # greater than 1000

# processing the low values in the list

# creting a variable stop
stop = 0

# only works in sorted lists
for index, value in enumerate(data):
    
    # if this condition is met - stop the loop when the value at index i is greater than OR equal to the min value
    if value >= min_valid:
        # stop at this index
        stop = index
        break

# delete the data up to stop
del data[:stop]    
print(data)

# ----------------------------------------------------------------
start = 0

# range(last data)
for index in range(len(data)-1, -1, -1):
    if data[index] <= max_valid:
        # delete the next element so that we keep this one
        # we have the index of the item which is either greater or equal to the max vaild
        # we know that the next element is the one to delete and all those after
        start = index + 1
        break

del data[start:]
print(data)