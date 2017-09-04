#Program asks the user for a number and the prints out a list 
#of all the divisors of that number.

num = raw_input('Please Enter a number: ')
num = int(num)

x = range(1, num+1)
divList = []

for element in x:
	if num % element == 0:
		divList.append(element)


print (divList)


	


