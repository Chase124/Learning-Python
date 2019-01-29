#The class is the skeliton of all the objects that you can call into the code
class Calculator:

    #These are the variables wich inside the class is called properties
    a=0
    b=0
    res = 0
    op = ' '


    #The fuctions are called methods inside the class
    def printCalculator(self):
        print(self.op + str(self.res))

    def sum(self):
        self.res = self.a + self.b
        self.op = 'Sum: '
        self.printCalculator()

    def sub(self):
        self.res = self.a - self.b
        self.op = 'Sub: '
        self.printCalculator()

    def div(self):
        self.res = float(self.a) / float(self.b)
        self.op = 'Div: '
        self.printCalculator()

    def mul(self):
        self.res = self.a * self.b
        self.op = 'Mul: '
        self.printCalculator()

# These are the objets that have been called (instantiated)
# An Instance is the proper way of saying objects when they are created in memory
myCalculator1 = Calculator() #instance 1

myCalculator1.a=10
myCalculator1.b=20
myCalculator1.mul()


myCalculator2 = Calculator()#instance 2

myCalculator2.a=50
myCalculator2.b=25
myCalculator2.div()



myCalculator3 = Calculator()#instance 3

myCalculator3.a = 5
myCalculator3.b = 24
myCalculator3.sum()


myCalculator4 = Calculator()#instance 4

myCalculator4.a = 25
myCalculator4.b = 4
myCalculator4.sub()

