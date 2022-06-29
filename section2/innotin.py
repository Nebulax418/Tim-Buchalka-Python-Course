# string is a sequence type of characters
parrot = "Norweigan Blue"

letter = input("Enter a character: ")

# characters are also like string - literally no difference - uses both double quotes ""
if letter in parrot:
    print(f"Your {letter} is in the parrot {parrot}")
else:
    print(f"Sorry no letter found in the parrot {parrot}")
