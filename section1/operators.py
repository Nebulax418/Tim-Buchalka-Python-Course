a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)  # floating division
print(a // b)  # integer division - rounded down towards minus infinity
print(a % b)

print()

for i in range(1, 4):
    print(i)

# numbers and variables are expressions

# this will give an error because floating point division is not allowed for | for loops
# for i in range(1, a / b):
#     print(i)

# this will work!
for i in range(1, a // b):
    print(i)
    

