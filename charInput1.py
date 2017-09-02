#This program asks the user to enter their name and their age.
#It then prints out a message notifying them when they will turn 100 years old. 

name = raw_input('Please Enter Your Name: ')
age = raw_input('Please Enter Your Age: ')
age = int(age)
year = (100 - age) + 2017
year = str(year)
print name + ' you will turn 100 years old in the year in: ' + year

#Ask the user for another number and prints out as 
#many copies of the previous message

copies = raw_input('Please Enter Another Number: ')
copies = int(copies)

print (copies * (name +' you will turn 100 years old in the year in: ' + year + '\n'))