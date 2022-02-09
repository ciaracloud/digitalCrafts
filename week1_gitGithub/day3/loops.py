print("Intro to looping")

counter = 0

while counter < 5:
    print("counter is less than 5")
    counter += 1

while True:
    print("This is true")
    break

choice = input("Would you like to continue y/n ?")
while choice == "y":
    print("yay!")

