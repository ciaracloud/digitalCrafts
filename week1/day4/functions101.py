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

print("Welcome to Joe's Portfolio!")
choice = input("Would you like to the see menu y/n \n")
while choice != "n" and choice != "Q":
    printMenu()
    choice = input("What would you like to do? \n")
    if choice == "1":
       printName()
    elif choice == "2":
       printCity()
    elif choice == "3":
       printFood()
    elif choice == "4":
       printCity()
       printName()
    else:
        print("Please choose between 1-4!")
    if choice == "4":
        print("4")
    else:
        print("No valid choice")