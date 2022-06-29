splitString = "This string has been split over\n several\n lines"
print(splitString)

tabbedString = "This is a \t tabbed\t string\t 4 spaces~!\t"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh, ,.... he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh, ... he's resting\".")

# by using triple quotes we do not need to escape any quotes here
print(""" The pet shop owner said "No, no, 'e's uh,... he's resting". """)

anotherSplitString = """\nThis string has been \
split over \
several \
lines"""

# the empty escape reverts the string to one line

print(anotherSplitString)

print(""" \nThe pet shop owner said "No, no, 'e's \
uh,... he's resting". """)

# how to print the escape characters as string too

# print("C:\Users\ARCHISMANNATH\notes.txt")

# prefixing using raw strings
print("\nC:\\Users\\ARCHISMANNATH\\notes.txt")

# using r is also possible - raw strings - usable with regex
print(r"C:\Users\ARCHISMANNATH\notes.txt")

