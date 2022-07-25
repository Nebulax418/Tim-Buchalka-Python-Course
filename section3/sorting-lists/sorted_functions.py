pangram = "The quick brown fox jumps over the lazy dog"

# sorts in alphabetical order
letters = sorted(pangram)

# prints letters
print(letters)

numbers = [2.4, 3.5, 3.8, 92.7, 9.6, 2.9, 4.2, 2.6]

# sorting the numbers with sorted function by creating a new list
sorted_numbers = sorted(numbers)

# printing the sorted numbers
print(sorted_numbers)

# prints the numbers list unchanged with sort
print(numbers)

# difference between sorted and sort function

# the difference is that the .sort() sorts the a list and does not make a new copy
# to make a new copy, the sorted list does the same thing as .sort but with any list inside its function ()

# sorted(list) -> will not work
# print(sorted(list)) will work

numbers.sort()
print(numbers)

# will return none - because it modifies in place

# another_sorted_numbers = numbers.sort() - you can't do this

# not a pangram because s is not included
missing_letter = sorted("The quick brown fox jumps over the lazy dog"
                        , key=str.casefold)

# key=str.casefold case sensitive sort
print(missing_letter)

    













