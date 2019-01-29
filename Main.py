# Get an input
# Create a if statment to check if the max 100 was reached
# to sum up the numbers and make

acumulator = 0


while (acumulator < 100 ):
    numbers = input("Type in another number")
    acumulator = acumulator + numbers
    print(acumulator)


if (acumulator >= 100):
    print ("The limit was reached you got to {0}".format(acumulator))