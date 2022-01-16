#small #1
# name = input("What is your name?")
# print("Hello, " + name.capitalize() + "!")

#small #2
# name = input("What is your name?")
# print("HELLO, ", name.upper(), "! YOUR NAME HAS", len(name), "LETTERS IN IT! AWESOME!")

#small #3
# print("Please fill in the blanks below: \n ___(name)___'s favorite subject in school is ___(sibject)___.")
# name = input("What's your name?")
# subject = input("What's your favorite subject in school?")
# print(name.capitalize(), "'s favorite subject in school is", subject.lower(), ".")

#small #4
# daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# userDay = int(input("Which day of the week? (0-6)"))
# print("The day of the week is", daysOfWeek[userDay])

#small #5
# daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# userDay = int(input("Which day of the week? (0-6)"))
# print("The day of the week is", daysOfWeek[userDay])
# if userDay == 0 or userDay == 6:
#     print("Sleep in!")
# else:
#     print("Go to work!")

#small #6
# userTemp = int(input("What is the temperature in C?"))
# print("The temperature in Farenheight is: ", ((userTemp * (9/5)) + 32))

#small #7(for loop)
# listOfNumbers = [1,2,3,4,5,6,7,8,9,10]
# for number in listOfNumbers:
#     print(number)

#small #7(while loop)
# listOfNumbers = [1,2,3,4,5,6,7,8,9,10]
# counter = 0
# while counter < len(listOfNumbers):
#     print(listOfNumbers[counter])
#     counter += 1

#small #8
# userNumber1 = int(input("What number would you like to start with?"))
# userNumber2 = int(input("What number would you like to end with?"))
# for eachNumber in range(userNumber1,userNumber2 + 1):
#     print(eachNumber)

#small #8 - another test
# userNumber1 = int(input("What number would you like to end with?"))
# for eachNumber in range(-10,userNumber1):
#     print(eachNumber)

#small #9
# myList = [1,2,3,4,5]
# for number in myList:
#     print(5 *"*")

#small #10
# squareSize = int(input("What size would you like your square sides to be? "))
# for eachStar in range(squareSize):
#     print(squareSize * "*")

# medium #1
# userBill = float(input("How much was your bill today? "))
# userServiceOpinion = input("How was the level of service? \n Amazing \n Fair \n or Poor \n")
# if userServiceOpinion == "Amazing" or userServiceOpinion == "amazing" or userServiceOpinion == "AMAZING":
#     tipTotal = userBill * 0.20
#     print("The tip you are giving today is: $%.2f" % tipTotal)
# elif userServiceOpinion == "Fair" or userServiceOpinion == "fair" or userServiceOpinion == "FAIR":
#     tipTotal = userBill * 0.15
#     print("The tip you are giving today is: $%.2f" % tipTotal)
# elif userServiceOpinion == "Poor" or userServiceOpinion == "poor" or userServiceOpinion == "POOR":
#     tipTotal = userBill * 0.10
#     print("The tip you are giving today is: $%.2f" %tipTotal)
# else:
#     print("Please choose from the following options: Amazing, Fair, or Poor \n Thank you!")
# print("Have a great day!")

#medium #2
# userBill = float(input("Hello, how much is your bill?"))
# userServiceOpinion = input("How was the level of service? (Amazing, Fair, or Poor)")
# userSplitAmount = int(input("How many ways would you like to split the bill?"))
# if userServiceOpinion == "Amazing" or userServiceOpinion == "amazing" or userServiceOpinion == "AMAZING":
#     tipTotal = userBill * 0.20
#     print("The tip you are giving today is: $%.2f" % tipTotal)
# elif userServiceOpinion == "Fair" or userServiceOpinion == "fair" or userServiceOpinion == "FAIR":
#     tipTotal = userBill * 0.15
#     print("The tip you are giving today is: $%.2f" % tipTotal)
# elif userServiceOpinion == "Poor" or userServiceOpinion == "poor" or userServiceOpinion == "POOR":
#     tipTotal = userBill * 0.10
#     print("The tip you are giving today is: $%.2f" %tipTotal)
# else:
#     print("Please choose from the following options: Amazing, Fair, or Poor \n Thank you!")
# userTotalAmount = float(userBill + tipTotal)
# print("Your total amount is: $%.2f" %userTotalAmount)
# userEachPersonTotal = userTotalAmount/userSplitAmount
# print("Each person owes: $%.2f" % userEachPersonTotal)
# print("Have a great day!")

#medium #3
# counter = 0
# print("You currently have %d coins." % counter)
# userAnswer = input("Do you want another coin? ")
# while userAnswer == "yes":
#     counter += 1
#     print(f"You now have {counter} coins!")
#     userAnswer = input("Do you want another coin? ")
#     if userAnswer == "no":
#         print("Bye")
        
#medium #4
# print("Let's make a hollow square with a star border!")
# userWidth = int(input("What would you like the width to be? "))
# userHeight = int(input("What would you like the height to be? "))
# print(userWidth * "*")
# counter = 0
# newHeight = int(userHeight - 2)
# newWidth = int(userWidth - 2)
# amountOfSpaces = newWidth * " "
# for row in range(newHeight):
#     print(f"*", amountOfSpaces, "*")
# print(userWidth * "*")

# print("Let's make a hollow square with a star border!")
# userWidth = int(input("What would you like the width to be? "))
# userHeight = int(input("What would you like the height to be? "))
# print(userWidth * "*")
# counter = 0
# newHeight = int(userHeight - 2)
# newWidth = int(userWidth - 2)
# myList = range(userWidth)
# for row in range(newHeight):
#     for space in myList:
#         print("4")
# print(userWidth * "*")

# print("Let's make a hollow square with a star border!")
# userWidth = int(input("What would you like the width to be? "))
# userHeight = int(input("What would you like the height to be? "))
# print(userWidth * "*")
# newHeight = int(userHeight - 2)
# newWidth = int(userWidth - 2)
# for row in range(newHeight):
#     myList = range(1,newWidth)
#     for myList[0]:
#         print("*")
#     for myList[-1]:
#         print("*")
# print(userWidth * "*")

# for row in range(userWidth):
#     for column in range(userHeight):
#         if 

# userHeight = int(input("What would you like the height to be?"))
# userWidth = int(input("What would you like the width to be?"))
# for element in range(userWidth):
#     print("*",end="")
#     for element in range(userHeight):
#         print("*")
# print()

# for indexNumber in range(5):
#     print("*",end="")

# print()

# print("Let's create a hollow square with a star border!")
# userHeight = int(input("How tall would you like the square to be? "))
# userWidth = int(input("How wide would you like the square to be? "))
# for element in range(userHeight):
#     for element in range(userWidth):
#         print("*",end="")
#     print()

# for element in range(4):
#     if element == 0:
#         print("*")
#     elif element == 1:
#         print("**")
#     elif element == 2:
#         print("***")
#     elif element == 3:
#         print("****")
# print()

#the correct answer for medium #4:
# userWidth = int(input("How wide would you like the square to be? "))
# userHeight = int(input("How tall would you like the square to be? "))
# for rowNumber in range(userHeight):
#     for elementInRow in range(userWidth):
#         if elementInRow == 0 or elementInRow == userWidth - 1 or rowNumber == 0 or rowNumber == userHeight - 1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

#medium #5
# counter = 1
# while counter < 8:
#     print(counter * "*")
#     counter += 2

#first attempt works:
# for elementInRow in range(7):
#     if elementInRow == 0 or elementInRow == 1 or elementInRow == 2 or elementInRow == 4 or elementInRow == 5 or elementInRow == 6:
#         print(" ",end="")
#     else:
#         print("*",end="")
# print()

# for elementInRow in range(7):
#     if elementInRow == 0 or elementInRow == 1 or elementInRow == 5 or elementInRow == 6:
#         print(" ",end="")
#     else:
#         print("*",end="")
# print()

# for elementInRow in range(7):
#     if elementInRow == 0 or elementInRow == 6:
#         print(" ",end="")
#     else:
#         print("*",end="")
# print()

# for elementInRow in range(7):
#         print("*",end="")
# print()

#trying another attempt, but with nested loops:

# counter = 0
# for row in range(userRow-1):
#     for elementInRow in range(userRow+counter):

#         if elementInRow == userRow + counter)/2:
#             print("*",end="")
#         else:
#             print(" ",end=" ")
#         counter += 1
#     print()

# userRow = int(input("How many rows would you like the star pyramid to be?"))
# for row in range(userRow):
#     newRange = int(userRow + (userRow -1))
#     for elementInRow in range(newRange):
#         if elementInRow == (userRow-1):
#             print("*", end="")
#         elif elementInRow <= (userRow-1):
#             print("5",end="")
#         elif elementInRow >= (userRow-1):
#             print("4",end="")
#     print()

userRow = int(input("How many rows would you like the star pyramid to be?"))
for row in range(userRow):
    newRange = int(userRow + (userRow -1))
    for elementInRow in range(newRange):
        counter = 1
        if elementInRow < (userRow-counter) or elementInRow > (userRow):
            print(" ",end="")
        else:
            print("*",end="")
        counter += 1
    print()