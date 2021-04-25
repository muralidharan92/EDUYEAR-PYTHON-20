# Find even & odd number conunt from list
list = [1,2,3,4,5,6,7,8,9]
evenNum = 0
oddNum = 0
for num in list:
    if num % 2 == 0:
        evenNum += 1
    else:
        oddNum += 1
print("Number Of Even number in list {}".format(evenNum))
print("Number Of Odd number in list {}".format(oddNum))

# Find Min & Max number from list

list = [145, 5487, 454, 7826, 6654, 4897, 425, 8632]
for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[j] < list[i]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
print("Min value from the list is {}".format(list[0]))
print("Max value from the list is {}".format(list[-1]))

# check the list is palindrom or not

list = [1,2,2]
temp = list.copy()
print("Is list is Palindrom? - {}".format(temp[::-1] == list))

# Check teh numbers in list is palindrom

list = [121, 122, 141, 144, 401, 404]

for num in list:
    temp = num
    rev = 0
    while num > 0:
        dig = num%10
        rev = rev * 10 + dig
        num = num//10
    if temp == rev:
        print("{} is palindrom".format(temp))
    else:
        print("{} is not palindrom".format(temp))
