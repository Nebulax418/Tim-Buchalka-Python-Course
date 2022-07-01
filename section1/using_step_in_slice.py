parrot = "Norwegian Blue"

print(parrot[0:6:3])

number = "9,223,372,036,854,775,807"
# print(number[1::4])

seperator = number[1::4]

values = "".join(char if char not in seperator else " " for char in number).split()
print([int(val) for val in values])

