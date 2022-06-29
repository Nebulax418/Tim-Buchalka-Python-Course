name = input("Please enter your name: ")

# passing the name as a variable to ask the user for their age while
# printing their name

# this returns a str datatype, so we need to convert it to an int to have the int datatype
age = int(input(f"How old are you {name}?\n"))

# ^^^ using int() converts it to an int


# checking for voting
if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print(f"You are not old enough to vote, please come back in {18-age} years")
