answer = 5

question = int(input("Please guess a number between 1 and 10: "))

while question != answer:
    
    # the question has to be asked again until the question == answer
    question = int(input("Please guess a number between 1 and 10: "))
    
    if(question == answer):
        print("Correct!")
        break;

    
        