#Number guessing game

import random
import math

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

number = random.randint(lower,upper)#generates random integer from lower to upper(included)
limit = round(math.log(upper-lower+1,2))
count = 0

print(f"You have to guess the number in {limit} attempts")
guess = None

while (count < limit):
    try:
        guess = int(input("Enter your guess : "))
        flag = 1
        if(guess < number):
            print("Your guess is too small!")

        elif(guess > number):
            print("Your guess is too high!")
        else:
            print(f"Your guess is correct the number is {guess}")
            break

    except ValueError:
        print("Invalid number")

    
    count = count+1

if count >= limit:
    print("The number is %d" % number )
    print("Better Luck next Time!")


