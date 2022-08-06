empty_list = []

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]

new_list = [even, odd]
print(new_list)

for n_list in new_list:
    print(n_list)
    for value in n_list:
        print(value)