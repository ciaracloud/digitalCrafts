#import random
#print(int(random.randint(2,20)))

import random
print("Let's roll a dice!")
numberOfSides = int(input("How many sides should it have? (2-20): "))
print("It's rolling!")
while numberOfSides < 2 or numberOfSides > 20:
    numberOfSides = int(input("How many sides should it have? (2-20): "))
print("It's a", random.randint(1,numberOfSides), "!")