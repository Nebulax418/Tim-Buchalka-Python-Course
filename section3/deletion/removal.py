data = [100, 103, 4, 89, 92, 192,
        2, 2222, 23, 93, 9299, 123, 999924]


min_valid  = 100
max_valid = 200

for value in data:
    if value < max_valid and value > min_valid:
        data.remove(value)
        
print(data)