fibSequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
choice = int(input("what number would you like to use?"))


# while fibSequence[-1] > fibSequence[-2]:
#     nextElement = fibSequence[-1] + fibSequence[-2]
#     fibSequence.append(nextElement)
#     print(fibSequence)
# print(fibsequence[choice])


#still working on this:    
while fibSequence[-1] > fibSequence[-2]:
    nextElement = fibSequence[-1] + fibSequence[-2]
    fibSequence.append(nextElement)
    print(fibSequence)
    
for element in fibSequence:
    if element > choice or element < choice:
        print("")
    else:
        print(fibSequence[choice])

