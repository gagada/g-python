#Print out Elements of a list that are less than 10

a = [1,1,2,3,5,8,13,21,34,55,89,100,150,14,65,7,67,18,200]
x = []

for element in a:
	if element < 10:
		x.append(element)

print (x)		

