# computer will guess the number that the person thinks
low = 1
high = 1000

print(f"Please think of a number between {low} and {high}: ")
# wait to press enter
input("Press enter to start: ")

guesses = 1

# we want to stop the loop when the computer gets the right answer
while True:
    # half it first
    print(f"\tGuessing in the range of {low} and {high}")
    guess = (low + high) // 2
    high_low = input(f"My guess is {guess} - Should it be high (enter h) or low (enter l) or is it correct (press c)?:  ").casefold()
    
    if high_low == "h":
        # Guess higer. The lower end of the range becomes 1 greater than teh guess
        # if my guess if 50 and the person says high - then 51 becomes the lower range
        low = guess+1 
    elif high_low == "l":
        # you must have code inside a code block
        # specific keyword is to have pass
         
        # pass is just like a visual comment to the developer that "we dont do anything here"
        # pass is like a #TODO but syntaxically correct
        # pass == "Python pass to the next line"
        
        # Can't have a comment here because python does not allow comments under conditions
        # Guess lower. The high of the range becomes 1 less than the guess
        high = guess - 1
        
        # its literally just narrowing down the search
    elif high_low == "c":
        print(f"I got the correct answer in {guesses} guesses!")
        break
    else:
        print("Please enter h, l, or c")
        
    guesses+=1
    
        
# swtich and case dont exist in python! hahah 

"""You can think pass statement as of telling python to pass on to the next line and to do nothing.

You cannot have an empty code block in python, 
so at the least you have to write one line inside a block 
(like a conditional or loop as you will learn later), 
so pass statement is used."""