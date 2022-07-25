available_parts = ["Computer",
                   "Monitor",
                   "HDMI Cable",
                   "Mouse",
                   "Mousepad",
                   "Gaming headset",
                   "Keyboard",
                   "Gaming char"]

# defining current_choice
current_choice = "-"

computer_parts = [] # creating an empty list


#valid_choices = [str(i) for i in range(1, len(available_parts)+1)]
# defining valid choices
valid_choices = []

for i in range(1, len(available_parts)+1):
    # str(i) for the string numbers not int numbers
    valid_choices.append(str(i))

while current_choice != '0': # program code jumps to the menu because it first doesn't any input
    
    #if current_choice in ["1", "2", "3", "4", "5"]:
    if current_choice in valid_choices:
        
        # index of current choice entered by user which needs to be minus oned for indexing.
        index = int(current_choice) - 1
        # the chosen part will be the part at the index
        chosen_part = available_parts[index]
            
        choice = input(f"Are you certain of selection of {chosen_part}? enter y/n: ")
        if choice.casefold() == "y":
             # add the chosen part
            print(f"Adding {chosen_part}")
            computer_parts.append(chosen_part)
        else:   
            try: 
                # remove the chosen part
                print(f"Removing {chosen_part}")
                computer_parts.remove(chosen_part)
            except ValueError:
                print(f"Cannot remove item from empty list")
                exit(0)
        # print the list
        print(f"Your list now contains {computer_parts}")
    else:
        # because program doesn't first have input it will print this
        print("Please add options from the list below: ")
        for index, part in enumerate(available_parts):
            print(f"{index+1} {part}")
            
            # use enumerate function instead
            # index = number of each part and the part corresponding to the index
            # print(f"{available_parts.index(part) + 1} {part}")   
            
            # enumerate gets the index and object of each occurence
            # one or more can be in the for loop to print with enumerate 
    # asks for input here after printing options
    current_choice = input() # needs to ge in 1,2,3,4,5 

print(computer_parts)

   