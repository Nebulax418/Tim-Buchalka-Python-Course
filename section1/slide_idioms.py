# python idioms

letters = "abcdefghijklmnopqrstuvwxyz"

# reversing a string
print(letters[::-1])

# return the "last" n items of a sequence in string - using negative indexing
print(letters[-4::])

# return the "first" n items of a sequence in string - using positive/normal indexing
print(letters[4::])

# last character in string
print(letters[-1:])

# first character in string
print(letters[:1])  # this works too but this does not give error if string is empty
print(letters[0])  # this is good too - but will give error if string is empty
