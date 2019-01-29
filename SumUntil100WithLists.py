# input
#if statment to cheak max is 100
# sum up the numbers
myList = []
acum = 0

while (acum < 100 ):
    numbers = input("Type in another number")
    myList.append(numbers)
    acum = sum(myList)
    print (myList)


if( acum >= 100 ):
    print ("You have reached {}".format(acum))