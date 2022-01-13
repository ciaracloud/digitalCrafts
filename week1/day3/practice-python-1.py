# import random
# print("You flipped a coin!")
# print("It is", random.randrange(1,3))

# import random
# print("You flipped a coin!")
# coin = ["heads!", "tails!"]
# print("It is", random.choice(coin))

# import random
# beadColors = ["pink", "blue", "green"]
# print("Hello! A random color will be generated! I will add that color bead to the necklace first!")
# print("The first bead color is", random.choice(beadColors))

# import random
# listToShuffle = ["one","two","three"]
# random.shuffle(listToShuffle)
# print(listToShuffle)

# count = 0
# number = int(input("Enter a number: "))
# while count < number:
#     is_even = number % 2 == 0
#     if is_even:
#         print("The number, ", number, ", is even!")
#     else:
#         print("The number, ", number, ", is odd!")
#     break


# number = int(input("Enter a number: "))
# if number % 2 == 0:
#         print("The number, ", number, ", is even!")
# else:
#         print("The number, ", number, ", is odd!")

import random
print("Let's roll a dice!")
numberOfSides = int(input("How many sides should it have? (2-20): "))
print("It's rolling...")
while numberOfSides < 2 or numberOfSides > 20:
    print(int(input("How many sides should it have? (2-20): ")))
print("It's a", random.randrange(1,numberOfSides), "!")

