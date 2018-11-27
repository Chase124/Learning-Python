import random

num = random.randint(1, 100)

#DEBUG
#print num

print ("Guess a number between 1 and 100")

guess = input()
i = int(guess)

while i != num:

    if i < num:
        print('Try higher')
    elif i > num:
        print('Try lower')

    guess = input()
    i = int(guess)

print('You have guessed the correct number congratulations')