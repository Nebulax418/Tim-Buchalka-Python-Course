age = 26

# (start, stop, step)
for i in range(0, 10, 2):
    print(i)

# spacing
print("-" * 20)

# going backwards - negative step
for i in range(10, 0, -2):
    print(i)

# using a range for some if statments

# 16-65 - but 66 for not including
if age in range(16, 66):
    print(f"Yes {age}")
else:
    print(f"No {age}")