current_choice = "-"

computer_parts = [] # creating an empty list

while current_choice != '0': # program code jumps to the menu because it first doesn't any input
    
    if current_choice in ["1", "2", "3", "4", "5"]:
        if current_choice == "1":
            print(f"Adding {current_choice}")
            computer_parts.append(current_choice)
        elif current_choice == "2":
            print(f"Adding {current_choice}")
            computer_parts.append(current_choice)
        elif current_choice == "3":
            print(f"Adding {current_choice}")
            computer_parts.append(current_choice)
        elif current_choice == "4":
            print(f"Adding {current_choice}")
            computer_parts.append(current_choice)
        elif current_choice == "5":
            print(f"Adding {current_choice}")
            computer_parts.append(current_choice)    
    else:
        # because program doesn't first have input it will print this
        print("Please add options from the list below: ")
        print("1: Computer")
        print("2: monitor")
        print("3: gopro")
        print("4: upir")
    
    current_choice = input() # needs to ge in 1,2,3,4,5
    
    
