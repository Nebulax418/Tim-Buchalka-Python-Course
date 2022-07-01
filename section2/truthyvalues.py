# if 0:
#     print("True") # not executable because 0 is False
# else:
#     print("False")

# empty sets, and sequences are also False

name = input("Please enter your name: ")


if name: # any name - not empty string
    print(f"Hello {name}")
else: # empty input - empty string
    print("Are you a man with no name?")

# quick way to check if user inputs nothing

# this is the better way

# does the same thing
if name != "":
    print(f"Yay {name}")
else:
    print("Noooo")

# does the same thing
if name == "":
    print("Nooo")
else:
    print(f"Woohoo {name}")