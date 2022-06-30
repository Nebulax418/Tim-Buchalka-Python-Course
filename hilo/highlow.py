"""Program outline:

My guess is 500

h == higher
l == lower
c == correct
"""

# low bound
low = 1

# high bound
high = 1000

guesses = 0

while True:
    print(f"Guessing from {low} to {high}")
    guess = low + ((high - low) // 2)    
    ex = input(f"My guess is {guess} - enter h for higher, l for lower, or c for correct: ").casefold()
    
    if ex == 'h':
        # should be higher than the lower bound/midpoint/guess
        low = guess + 1
    elif ex == 'l':
        # should be lower than the upper bound - and the midpoint/guess
        high = guess - 1
    elif ex == 'c':
        print(f"Yes! I found it! in {guesses} guesses")
        break         

    guesses += 1