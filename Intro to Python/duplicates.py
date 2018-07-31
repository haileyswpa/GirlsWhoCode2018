# Declare variables
mylist = [2,3,1,3,5]   # Our inputs to the program
has_duplicates = False # initialize as false (why?)

# Sort 'myList' (Why do we sort first?)
mylist.sort()
print(mylist)
# Loop through 'mylist' with a for-Loop
for index in range(len(mylist) - 1):
    print(index)
    print(mylist[index], mylist[index + 1])
    # Check if adjacent elements of 'mylist' are the same
    if mylist[index] == mylist[index + 1]:
        # if they are the same, set has_duplicates to True
        has_duplicates = True
        # Exit out of the for-loop (no need to check rest of list)
        break
print(has_duplicates) # Our outputs of the program
