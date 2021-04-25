# From range n to m, print all the numbers divisible by 5 & 7

for i in range(1, 100):
    if i % 5 == 0 and i % 7 == 0:
        print(i)

# Find sum of the series 2+22+222+2222+22222 using n term

numberOfTerm = 5
sum = 0
value = "2"
for i in range(1, numberOfTerm+1):
    temp = value*i
    sum += int(temp)
print(sum)

# While loop Take int val from user and primt sum of value and quit once press q

num = 0
while True:
    userInput = input("Please enter a number to sum or press q to quit: ")
    if userInput.lower() == 'q':
        break
    else:
        num = num + int(userInput)
        print(num)

# Factorial number

num = int(input("Please Enter number to find Factorial: "))
result = num

if num == 0 or num == 1:
    result = 1
else:
    while num > 1:
        num = num-1
        result *= num
print(result)

