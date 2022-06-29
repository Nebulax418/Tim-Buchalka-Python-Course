number = input("Please enter a string of numbers using only commas, colons, or semicolons: ")
seperators = ""
seperated_numbers = ""
result = 0;

for char in number:
    # if the character in the string is not numeric
    if not char.isnumeric():
        # append to the empty string - add it up
        seperators+=char
    else:
        # append the numbers to another string
        seperated_numbers+=char

# adding up all the things in the string
for number in seperated_numbers:
    result+=int(number)
            
# print both the strings that we've already appended to
print(seperators)
print(seperated_numbers)
print(f"The addition result of {seperated_numbers} is {result}")