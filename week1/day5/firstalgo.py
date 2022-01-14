# def reverseList(listGiven):
#     theResult = ""
#     for element in listGiven:
#         theResult = element + theResult
#         print(theResult)

# list = [1,2,3,4]

# def reverseList(listGiven):
#     list
#     print(l[::-1])

myList = [1,2,3,4]
def swappedList(listGiven):
    # replaceThis = listGiven[0]
    # withThis = listGiven[-1]
    # listGiven = listGiven.replace(replaceThis, withThis)
    listGiven[0],listGiven[-1] = listGiven[-1],listGiven[0]
    print(listGiven)

swappedList(myList)
