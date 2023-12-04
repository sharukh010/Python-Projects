# Number guessing game
## Algorithm:
* User inputs the lower bound and upper bound of the range.
* The compiler generates a random integer between the range and store it in a variable for future references.
* For repetitive guessing, a while loop will be initialized.
* If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You guessed too high“
* Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You guessed too small”
* And if the user guessed in a minimum number of guesses, the user gets a “Congratulations! ” Output.
* Else if the user didn’t guess the integer in the minimum number of guesses, he/she will get “Better Luck Next Time!” output.
## random.randint()
It takes range of numbers from which the random number need to be selected the ending element is also included

## math.log()
It is used to calculate the number of minimum attempts requried to guess the number
math.log(a,b)
where,
a = number on which logrithm need to be applied
b = base
>>log() function return decimal values like(4.33342) we need to round it to nearest integer to calculate number of attempts

## How to declare a variable without assigning any value to it?
Just Assign it None
ex:variable = None

# How to print formated string in python?
1. using print(f"number = {variable_name}")
2. using print("number1 = %d number2 = %d" % (variable_name1,variable_name2))
3. using print("number = {}".format(variable_name))