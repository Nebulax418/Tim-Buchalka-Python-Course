l = 1
h = 10000

n_search = 7834

# if num is less than mid
# h bound = mid - 1
# if num is greater than mid
# lower bound = mid + 1
# if 
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 

# reembmer this if teh number to search is less than the mid point - then that would mean that it is also less than teh high bound
# remember this that if the number to search is greater than the mid point, it is also greater than teh lower bound

while l <= h:
    # keep finding the midpoint
    mid = (l + h) // 2
    
    if n_search < mid:
        h = mid - 1 # index would be one less than mid
    elif n_search > mid:
        # index would be one more than mid
        l = mid + 1
    else:
        # two things - found or not found
        print("Found")
        break

print("Not found")
    
