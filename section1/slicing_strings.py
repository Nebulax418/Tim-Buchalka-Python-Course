"""
You can produce slices by providing three things

start stop and step values

"""

parrot = "Norwegian Blue"

# slice up to but not including 6 - start:stop
print(parrot[0:6])  # equivalent to [0:6:1] slice

# printing from element 3 to element 5 slice using step of 1
print(parrot[3:5])

# printing from element 0 to 9
print(parrot[0:9])  # default could also be print(parrot[:9])

print(parrot[10:])

print(parrot[:6] + parrot[6:])

print(parrot[:])
