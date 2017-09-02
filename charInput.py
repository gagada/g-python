#This program asks the user to enter their name and their age.
#It then prints out a message notifying them when they will turn 100 years old. 

name = raw_input('Please Enter Your Name: ')
age = raw_input('Please Enter Your Age: ')
age = int(age)
year = (100 - age) + 2017
year = str(year)
print 'You will turn 100 years old in the year in ' + year