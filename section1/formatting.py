# formatting

# {number:spacing} - reserving spacing - adding spacing before the value
for i in range(1, 13):
    print("No. {0:2}^2 squared is {1:3} and cubed is {2:4}".format(
        i, i ** 2, i ** 3))

print("\n")

# this is the alignment symbol - {number:>spacing} - is just spacing BEFORE (LEFT)
# the value making it left right aligned
# this is the alignment symbol - {number:<spacing} - is just spacing AFTER (RIGHT)
# the value making it left aligned

for i in range(1, 13):
    print("No. {0:2}^2 squared is {1:<3} and cubed is {2:<4}".format(
        i, i ** 2, i ** 3))

print("\n")

# we can center it too - using the ^ symbol
for i in range(1, 13):
    print("No. {0:2}^2 squared is {1:^2} and cubed is {2:^}".format(
        i, i ** 2, i ** 3))

print("\n")

# general format - prints 15 decimals

# the number after the colon is the field width
print("Pi is approximately {0:.2f}".format(22 / 7))

# using f we get 6 digits after the decimal
print("Pi is approximately {0}".format(22 / 7))

print("Pi is approximately {0:12.50f}".format(22 / 7))

print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))

# max precision is 50 digits
print("\n")
print("Pi is approximately {0:<72.54f}".format(22 / 7))

print("\n")
for i in range(1, 13):
    print("No. {}^2 squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
