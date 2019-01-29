number_list = ['15','84','200','20000', '50','9','800000','150','4000','12','15','18','14']
numberLengthList = []
maxNumberSize = 0

# first use a loop to count how many characters in each number

for number in number_list:
    #print ("{0} is the number in the list".format(number))
    numberLengthList.append(len(number))
    #print("The biggest number length in the number list is {0}".format(max(numberLengthList)))

maxNumberSize = max(numberLengthList)

for number in number_list:
    if len(number) == maxNumberSize:
        print(number)
