# sequence - ordered set of items
# list is also a sequence types

# you can have sequences and call them by sequence[]
# also you can get the letters form sequence[word][letter]

# everything you can do with the str sequence type can also be done
# with other sequence types

# everything with one exception. Not all sequence types can be concatenated or multiplied
# range is an example of a sequence that cannot be concatenated

string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords "

print(string1 + string2 + string3 + string4 + string5)

# you can concatenate strings using this
print("he's " "probably" " pining " "for the " "fjords")

# you can multiply string too - so useful! instead of boring for loops :O
print("Hello" * 5)

# you can also multiply list and tuples

# can't concatenate or multiply a range - wouldn't want to do that anyway
# can't add strings with numbers too

print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

# there is an operator to check if a substring is in a string

# so useful
today = "friday"
print("day" in today)  # true
print("fri" in today)  # true
print("thur" in today)  # false
print("parrot" in "fjord")  # false
