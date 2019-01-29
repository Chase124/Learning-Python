
def this_is_a_nomal_function():
    print('This is a nomal function')


class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    def move(self):
        print("Moving now!")


class Animals(Animate):
    def eat_food(self):
        print("Eating now!")

class Mammals(Animals):
    pass


class DancingMammal(Animals):
    def dance(self):
        self.left_Foot_Forward()
        self.left_Foot_Back()
        self.right_Foot_Back()
        self.right_Foot_Forward()

    def left_Foot_Forward(self):
        print ('left foot forward')

    def left_Foot_Back(self):
        print ('left foot back')

    def right_Foot_Forward(self):
        print ('right foot forward')

    def right_Foot_Back(self):
        print ('right foot back')

class Giraffes(DancingMammal):
    def __init__(self, n, h, c):
        self.name = n
        self.height = h
        self.color = c
        #self.spriteFile = "giraffe.jpg"

    def find_food(self):
        self.move()
        print ("I have found food!")
        self.eat_food()

    def give_birth(self):
        self.give_birth
        print ("")

    def myGiraffeInfo(self):
        print ('This is a Giraffe its name is {0} she is {1} cm tall and she is predominantly {2}'.format(self.name,self.height,self.color) )

    def this_is_a_method(self):
        print('This is a method')

    def this_is_also_a_method(self):
        print('Class functions are called methods')


class Sidewalks(Inanimate):
        pass

gerald = Giraffes("Gerald", 300, "Yellow" )
john = Giraffes("John",  500, "Red" )
jenny = Giraffes("Jemmy", 200, "Orange")


gerald.this_is_also_a_method()
gerald.myGiraffeInfo()
john.myGiraffeInfo()
john.eat_food()
gerald.move()

gerald.find_food()

jenny.dance()
