#Print out Elements of a list that are less than 20

a = [1,1,2,3,5,8,13,21,34,55,89,100,150,14,65,7,67,18,200]
x = []

#Ask the user for a number and return a list that contains only elements
#from the original list and that are smaller than that number given by 
#the user
userInput = raw_input('Please Enter a Number: ')
userInput =int(userInput)

for element in a:
	if element < userInput:
		x.append(element)

print (x)		

