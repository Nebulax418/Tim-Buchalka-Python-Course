available_parts = ["Comp",
                   "Pots",
                   "Shit",
                   "Mrek",
                   "lek"]

current_choice = "-"
computer_parts = [] # creating an empty list


#valid_choices = [str(i) for i in range(1, len(available_parts)+1)]
valid_choices = []

for i in range(1, len(available_parts)+1):
    # str(i) for the string numbers not int numbers
    valid_choices.append(str(i))
print(valid_choices)


while current_choice != '0': # program code jumps to the menu because it first doesn't any input
    
    #if current_choice in ["1", "2", "3", "4", "5"]:
    if current_choice in valid_choices:
        print(f"Adding {current_choice}")
        # index of current choice entered by user which needs to be minus oned for indexing.
        index = int(current_choice) - 1
        # the chosen part will be the part at the index
        chosen_part = available_parts[index]
        # add it to the computer parts
        computer_parts.append(chosen_part)
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

   