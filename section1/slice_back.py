letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]

print(backwards)

backwards = letters[::-1]  # this is how we reverse a string in python
print(backwards)

# this is a python idiom [::-1]

# create a slice to produce qpo

qpoSlice = letters[-10:-13:-1]

print(qpoSlice)

# print edcba

edcbaSlice = letters[-22::-1]

print(edcbaSlice)

# last 8 characters in reverse order

reversedEight = letters[:-9:-1]
print(reversedEight)