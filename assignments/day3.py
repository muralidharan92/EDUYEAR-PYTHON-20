# Age Calculator

from datetime import date
userYear = int(input("Please enter your born year in YYYY format: "))
currentDate = date.today()
currentAge = currentDate.year - userYear
print(currentAge)

# Simple Calculator

input1 = int(input("Please enter 1st number: "))
input2 = int(input("Please endre 2nd number: "))
print("{} + {} = {}".format(input1, input2, input1+input2))
print("{} - {} = {}".format(input1, input2, input1-input2))
print("{} / {} = {}".format(input1, input2, input1/input2))
print("{} // {} = {}".format(input1, input2, input1//input2))
print("{} * {} = {}".format(input1, input2, input1*input2))
print("{} % {} = {}".format(input1, input2, input1%input2))
print("{} ** {} = {}".format(input1, input2, input1**input2))

# Count occurence of character in String

s = "This year we will learn python"
print(s.count("y"))

# Print even Index Character from string

s = "0123456789"
# s = "abcdefghijklmnopqrstuvwxyz"
print(s[::2])