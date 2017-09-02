#Ask for a number from the user
#Depending on even or odd, print an appropriate message

num = raw_input('Please Enter a Number: ')
num = int(num)

#Checks if this is a Multiple of 4 
if num % 2 == 0 and num % 4 == 0:
	print('This is a multiple of 4')
elif num % 2 == 0:
	print('Your Number is Even')
else:
	print('Your Number is Odd')

#Ask the user for 2 numbers
#One number to check, one number to divide
#Check if the numbers divide evenly or not.

num1 = raw_input('Please Enter a check Number: ')
num1 = int(num1)

divide = raw_input('Please Enter a number to divide: ')
divide = int(divide)

if num1 % divide == 0:
	print ('Divides evenly')
else:
	print ('Does not divide evenly')