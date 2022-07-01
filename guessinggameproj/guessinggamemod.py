import random
import os
import sys
import subprocess

# dot notation
highest = 100
answer = random.randint(1, highest)

guesses_left = 10 

guess = int(input(f"Enter a number between 1 and {highest}: "))

# while the guess is not equal to the answer
while guess != answer:

    # check for two conditions - and then ask again
    if guess < answer:
        guess = int(input("Please guess higher: "))
    elif guess > answer: 
        guess = int(input("Please guess lower: "))
        
    
    if guess == answer:
        print("Correct!")
        break
    else:
        if guesses_left == 1:
            opw = int(input("You have no guesses left!"))
            break
        else:# output this if the guess is not the answer - regardless of less or greater than answer
            guesses_left-=1
            print(f"You have {guesses_left} guess left")    

