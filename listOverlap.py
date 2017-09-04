#Take 2 lists and return a list that contains only the element 
#that are common between the lists 

a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,89]

x = []

for elem in a:
	for element in b:
		if elem == element:
			x.append(element)

print (x)
