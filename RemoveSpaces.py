#print('Could you please type in you birthday date?')

#bday = input()
#print(bday.split())         #Putting the string into a list separating elements using spaces as a refrence
#print(bday.replace(" ", ""))#Replacing spaces with no space
#print(bday.rstrip())        # getting rid of all the spaces at the end of sentence


print('Could you please format the birthday dates to (ddmmyyyy), (dd/mm/yyyy) then (dd/mm/yy)?')
bdaylist = ["12   01 2009","23       04   1999","   23    03     2005","  16   00   2022","350 6 2009"]

for b in bdaylist:
    print(b.replace(" ", ""))
    breplaced = b.replace(" ", "")
    print (str(breplaced))
    bsplitted = str(breplaced)
    print ("{}/{}/{}".format(bsplitted[0:2],bsplitted[2:4],bsplitted[6:8]))
    print ("{}/{}/{}".format(bsplitted[0:2], bsplitted[2:4], bsplitted[4:8]))


# Check if day, month and year are valid
# If they are print them as usual
# else print a message saying which part of the date is incorrect