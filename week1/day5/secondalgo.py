# Input : list = [12, 45, 2, 41, 31, 10, 8, 6, 4]
# Output : 
# Largest element is: 45
# Smallest element is: 2
# Second Largest element is: 41
# Second Smallest element is: 4

# Input : list = [22, 85, 62, 40, 55, 12, 39, 2, 43]
# Output :
# Largest element is: 85
# Smallest element is: 2
# Second Largest element is: 62
# Second Smallest element is: 12

myList = [12, 45, 2, 41, 31, 10, 8, 6, 4]

def printCertainElements(listGiven):
    listGiven.sort()
    print("The smallest element is: ", listGiven[0])
    print("The largest element is:", listGiven[-1])
    print("The second largest element is: ", listGiven[-2])
    print("The second smallest element is: ", listGiven[1])

printCertainElements(myList)