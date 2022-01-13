# How to create functions in python

# print("""

#                                ,----.
#                               ( WOW! )                         .-.
#                                `----' _                         \ \
#                                      (_)                         \ \
#                                          O                       | |
#                     |\ /\                  o                     | |
#     __              |,\(_\_                  . /\---/\   _,---._ | |
#    ( (              |\,`   `-^.               /^   ^  \,'       `. ;
#     \ \             :    `-'   )             ( O   O   )           ;
#      \ \             \        ;               `.=o=__,'            \
#       \ \             `-.   ,'                  /         _,--.__   \
#        \ \ ____________,'  (                   /  _ )   ,'   `-. `-. \
#         ; '                ;                  / ,' /  ,'        \ \ \ \
#         \                 /___,-.            / /  / ,'          (,_)(,_)
#          `,    ,_____|  ;'_____,'           (,;  (,,)      jrei
#        ,-" \  :      | :
#       ( .-" \ `.__   | |
#        \__)  `.__,'  |__)  SSt
# """)

# catImage = """
#       _._     _,-'""`-._
#      (,-.`._,'(       |\`-/|
#          `-.-' \ )-`( , o o)
#      -bf-      `-    \`_`"'-
# """

# print("Welcome to my cat's hangout spot")
# choice = input("Would you like to see my cat? (y/n)")
# while choice != "n":
#     print(catImage)

# def printCat():
#     mouse = "squeek"
#     print("""
#          _._     _,-'""`-._
#      (,-.`._,'(       |\`-/|
#          `-.-' \ )-`( , o o)
#      -bf-      `-    \`_`"'-
#      """)
#     return

# while choice != "n":
#     printCat()
#     choice

# def printMenu():
#     return print("""
#     1. print my name
#     2. print my city
#     3. print my favorite food
#     4.quit
#     """)

# print("Welcome to Joe's Portfolio!")
# choice = input("Would you like to the see menu y/n \n")
# while choice != "n" and choice != "Q":
#     printMenu()
#     choice = input("What would you like to do? \n")
#     if choice == "1":
#        printName()
#     elif choice == "2":
#        printCity()
#     elif choice == "3":
#        printFood()
#     elif choice == "4":
#        printCity()
#        printName()
#     else:
#         print("Please choose between 1-4!")
#     if choice == "4":
#         print("4")
#     else:
#         print("No valid choice")

def tenPercent():
    tip = billAmount *0.1
    return print ("Your tip would be", tip)

# def fifteenPercent():
#     tip = billAmount *0.15
#     return print("Your tip would be", tip)

# def twentyPercent():
#     tip = billAmount *0.2
#     return print("Your tip would be", tip)
# def calculateTip():
#     if tipAmount == "A":
#         tenPercent()
#     elif tipAmount == "B":
#         fifteenPercent()
#     elif tipAmount == "C":
#         twentyPercent()

# billAmount = int(input ("How much is your bill?"))
# tipAmount = input("""
#     How much would you like to tip?
#     A. 10%
#     B. 15%
#     C. 20%
#     """)

# while tipAmount != "A" and tipAmount != "B" and tipAmount != "C":
#     print ("Choose A B or C")
#     tipAmount = input("""
#     How much would you like to tip?
#     A. 10%
#     B. 15%
#     C. 20%
#     """)

# calculateTip()



# sortlist = [5,10,20,22,6,23,9,0,1]

# print(sortlist.sort())
# print(sortlist)

# print("This is the largest number", list[-1])

# print(list.sort())

myString = "SWEET"

finishedStatement = ""

for letter in myString:
    if letter == "S":
        numberFive = "5" 
        finishedStatement = finishedStatement + numberFive
    elif letter == "E":
        numberThree = "3"
        finishedStatement = finishedStatement + numberThree
    elif letter == "T":
        numberSeven = "7"
        finishedStatement = finishedStatement + numberSeven
    elif letter == "A":
        letterFour = "4"
        finishedStatement = finishedStatement + numberFour
    elif letter == "G":
        numberSix = "6"
        finishedStatement = finishedStatement + numberSix
    elif letter == "O":
        numberZero = "0"
        finishedStatement = finishedStatement + numberZero
    else:
        finishedStatement = finishedStatement + letter
print(finishedStatement)
    