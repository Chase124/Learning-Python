numberList = ['12','15','18','14','21','45','12']

convertedNumbers = []

maxNumber = 0

# Use a loop to convert the list from a string to a number with int and then append to a new list
for number in numberList:
    convertedNumbers = int(number)
    #print convertedNumbers
# Now you will have a list of the string and one of the numbers

# Find the biggest number in the numbers list
maxNumber = max(numberList)

# Print
print maxNumber


