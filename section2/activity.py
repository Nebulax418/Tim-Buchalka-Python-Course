activity = input("What would you like to do today? ")


# caseless comparison of strings such as in java string.equalsIgnoreCase()
# best for this
if "cinema" not in activity.casefold():
    print("But why not the cinema?")
else:
    print("Okay let's go!")

# python has a very big library of string functions