def sum (a, b):
    res = a + b
    return res

def sub (a, b):
    res = a - b
    return res

def div (a, b):
    res = float(a) / float(b)
    return res

def mul (a, b):
    res = a * b
    return res

goagain = 'y'

while ( 'y' == goagain  ):


    n1 = input("Type the first number: \n")
    caracter = raw_input("Type in the caracter: \n")
    n2 = input("Type the second number: \n")

    if ('+' == caracter ):
        print('The answer of {0} + {1} is {2}'.format (n1, n2, sum(n1, n2)))

    if ('-' == caracter):
        print( 'The answer of {0} - {1} is {2}'.format(n1, n2, sub( n1,n2)))

    if ('/' == caracter):
        print('The answer of {0} / {1} is {2}'.format (n1, n2, div( n1,n2)))

    if ('*' == caracter):
        print('The answer of {0} * {1} is {2}'.format (n1, n2, mul( n1,n2)))

    goagain = raw_input('Would you like to use the calculater again (y/n) \n')


print(' Thank you for using the calculater' )