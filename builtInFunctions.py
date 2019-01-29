class Test():
    def test_ABS(self, number):
        print (abs(number))


    def test_bool(self, input):
        print (bool(input))

    def testInputFromUser(self,year):
        if not bool(year):
            print("Invalid input")





my_test = Test()

my_test.test_ABS(-48)

my_test.test_bool(89)

my_test.test_bool('a')

my_test.test_bool(None)

my_test.test_bool(" ")

year = input("Type your year of birth:")
my_test.testInputFromUser(year)

your_Calculator = raw_input("Type in a math equation")

result = eval(your_Calculator)

print float(result)
print int(result)


your_Age = input("Type in your age")

if (your_Age > 13):
    print ("Access Granted")
else:
    print ("Access Denied")

len('this is a test string')

creature_list =['unicorn','cyclops','fairy','elf','dragon','troll']
i=0
while i < len(creature_list):
    print (len(creature_list[i]))
    print (creature_list[i])
    i += 1

for creature in creature_list:
    print(len(creature))

#pg118