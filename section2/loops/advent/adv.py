
available_exits = ["north", "south", "east", "west"]

# initializes the variable to an empty string
chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose an exit: ")
    
    # casefold for unbiased capital check
    if chosen_exit.casefold() == "quit":
        print("Goodbye!")
        break
        

# if the chosen exit is out of it then print this
print("Sheesh, you got out of it!")
