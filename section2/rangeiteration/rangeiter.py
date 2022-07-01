# python for loops are quite different which make them very powerful
# python brings for loops with ranges as the c style and java style for loops

# printing the values from 1-20

# 1 to not including 20
for i in range(1, 20):
    print(f"I is now {i}")

# we can also do it this way (0, 20) = (20) - no need to provide a start value
# it always will default to 0
for i in range(20):
    print(f"I is {i}")