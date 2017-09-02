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