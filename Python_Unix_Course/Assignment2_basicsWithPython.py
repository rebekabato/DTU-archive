#!/usr/bin/env python3
import numpy as np
import math

# 1. Write 'Hello World' on the screen
print("Hello World")
print("----end of the 1. task----")


# 2.Write 'Hello World' 10 times using a loop. One Hello per line.
for i in np.arange(1,11):
	print("Hello World")
print("----end of the 2. task----")


# 3.Write numbers 1 to 10 to the screen one number per line. Use a loop.
for i in np.arange(1,11):
	print (i)
print("----end of the 3. task----")


# 4.Make a program ask for a name, and then write a greeting using that name. However, if it is your name you give as input the greeting should be extra nice.
name = input("Type your name, please: ")
if name.upper() == "REBEKA": # it seems this evaluation is not that anonymous that we would think :O :P
	print ("Warm welcome ",name)
else:
	print("Hi ",name)
print("----end of the 4. task----")
 

# 5.Make a program that ask for two numbers (one at a time) and then prints them and their sum.
print("This program calculates the sum of two numbers ")
numberOne = input("Type a number, please: ")
numberTwo = input("Type one more number, please: ")
while (not numberOne.isdigit()) or (not numberTwo.isdigit()):
	if (numberOne.isdigit() != True):
		numberOne = input("The first entry is not a number, please type a number: ")		
	
	if (numberTwo.isdigit() != True):
		numberTwo = input("The second entry is not a number, please type a number: ")

print (numberOne, '+', numberTwo, "equals to ",float(numberOne) + float(numberTwo))
print("----end of the 5. task----")

# Since, I was told that not to handle the different kinds of inputs - because we assume that the user is a well-behaved
# and sensible person enough to follows what the program says - so from this point, I stop improving my code in this aspect
# and I will concentrate only on what the task asks me to solve.
 
# 6.Ask for two numbers and ask what operation to perform on them (+, - , *, /) and display the numbers and the result.
print("This program performs basic calculations")
numberOne = float(input("Type a number, please: "))
numberTwo = float(input("Type one more number, please: "))
operation = str(input("Please select an operation that you want to perform (+, - , *, /): "))
if operation == '+':
	print (numberOne, operation, numberTwo, "equals to ",float(numberOne) + float(numberTwo))
elif operation == '-':
	print (numberOne, operation, numberTwo, "equals to ",float(numberOne) - float(numberTwo))
elif operation == '*':
	print (numberOne, operation, numberTwo, "equals to ",float(numberOne) * float(numberTwo))
elif operation == '/':
	print (numberOne, operation, numberTwo, "equals to ",float(numberOne) / float(numberTwo))
else:
	print("Your input is invalid")
print("----end of the 6. task----")

# 7.Ask for two integers and print them and all integers between them. It is not necessary to perform input control - just assume that the user is well-behaved and inputs integers.
start = int(input("Type a number, please: "))
stop = int(input("Type one more number, please: "))
for i in np.arange(start+1, stop-1):
	print (i)
print("----end of the 7. task----")

# 8.Now make the same program work even if you switch the input numbers, so it does not matter if you input the smallest number first or last.
numberOne = int(input("Type a number, please: "))
numberTwo = int(input("Type one more number, please: "))
start = None
stop = None
if numberOne <= numberTwo:
	start = numberOne
	stop = numberTwo
if numberTwo <= numberOne:
	start = numberTwo
	stop = numberOne

for i in np.arange(start+1, stop-1):
	print (i)
print("----end of the 8. task----")

#9.This needs to be read carefully: Make a program that asks for number, 
# and then continues asking for numbers as long as you input numbers that are 
# greater or equal to all previous numbers (not the sum of previous numbers).
store = None
while True:
	askNumber = float(input("Type a number, please: "))
	if store == None:
		store = askNumber
	elif (store != None) and (askNumber >= store):
		store = askNumber
	elif (store != None) and (askNumber < store):
		break
print("----end of the 9. task----")

# 10. Ask for a positive integer and calculate the factorial (n!) of that number. 
# Display the result. If input is negative, display an error message.
print("This program calculates the factorial of a number.")
positiveInt = int(input("Type a positive whole number, please: "))
if positiveInt < 0:
	print("Error: Your input does not meet the following requirement: 'positive whole number'.")
elif positiveInt == 0:
	print("The factorial of zero is one.")
elif positiveInt > 0:
	factorial = np.prod(np.arange(1, positiveInt+1))
	print("The factorial of ", positiveInt, "is ", factorial)
print("----end of the 10. task----")

# 11. If you solved the previous one then this should be relatively easy.
# Ask for an integer and calculate the sum from 0 up/down to the integer.
# An example: If you input 5 then calculate 5 + 4 + 3 + 2 + 1 (+ 0) = 15.
# If input is -4 then calculate -4 + -3 + -2 + -1 (+ 0) = -10.

number = int(input("Type a whole number(either + or -), please: "))
if number >= 0:
	result = np.sum(np.arange(0, number+1))
	print("Result: ", result)
elif number <= 0:
	result = np.sum(np.arange(0, abs(number)+1))
	print("Result: -", result)

