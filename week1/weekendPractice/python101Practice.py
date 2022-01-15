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