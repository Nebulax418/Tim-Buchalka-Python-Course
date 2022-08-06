data = [100, 103, 4, 89, 92, 192,
        2, 2222, 23, 93, 9299, 123, 999924]

min_valid  = 100
max_valid = 200

# # i -= 1 - is what happens in the step
# for index in range(len(data) - 1, -1, -1):
#     if data[index] < max_valid and data[index] > min_valid:
#         # print index and the data
#         print(f"|Index No. {index} - Value {data[index]}|", data)
#         print(f"Deleted {data[index]}... new list below after deletion")
        
#         # delete the data at the index
#         del data[index]
        
#         # this is happening in real time as we speak
#         # we see this happening becasue we are printing the data out
#         # each time it deletes

# works best with sorted data
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]

print(data)
