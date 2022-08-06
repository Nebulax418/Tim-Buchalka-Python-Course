data = [2, 3, 200, 92, 32, 222, 23]

new_data = []

for index, value in enumerate(data):
    
    if value >= 100:
        new_data.append(value)
        del data[index]


print(new_data) 
print(data)           