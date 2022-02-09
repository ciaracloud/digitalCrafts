#my attempt at #1 (works!)
import math
number = int(input("what number would you like to use?"))
factorialOfNumber = math.factorial(number)
print(factorialOfNumber)

#my attempt at #2 (works!)
word = input("what would you like the word to be?")
if word[:] == word[::-1]:
    print("This word is a palindrome! :D")
else:
    print("This word is NOT a palindrome! :(")

#my attempt at #3 (doesn't work!)
number = int(input("what number would you like to use?"))
if number > 1:
    for i in range(2,number):
        if (number % i == 0):
            print ("Sorry! This is not a prime number! :/")
            break
        else:
            print("YAY! You found a prime number! :D")
            break
else:
    print("Try again and choose a number other than one!")

#group attempt at #3 (works!)
num = int(input("Let's see if your number is ready for PrimeTime "))
if num > 1:
    for i in range(2, num):
        if (num % i == 0):
            print('It is not a prime number')
            break
    else:
        print('It is a prime number')
else:
    print('Must provide a number larger than one')

