#Take 2 lists and return a list that contains only the element 
#that are common between the lists 
#User Input for range determination. Try to use two different ranges for the list
import random

num = raw_input('Please Enter a Number for the First list: ')
num1 = raw_input('Please Enter another Number for the Second list: ')
num = int(num)
num1 = int(num1)

x = range(1, num+1)
y = range (1, num1+1)

a= []

for elem in x:
	for element in y:
		if elem == element:
			a.append(element)

print (a)