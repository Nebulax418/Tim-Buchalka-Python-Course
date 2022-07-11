available_exits = ["north", "south", "east", "west"]

# initializes the variable to an empty string
chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose an exit: ")
    
    # casefold for unbiased capital check
    if chosen_exit.casefold() == "quit":
        print("Goodbye!")
        break

# only executed if the loop terminates normally - not if it breaks out of the loop   
else:
    # if the chosen exit is out of it then print this
    print("Sheesh, you got out of it!")
