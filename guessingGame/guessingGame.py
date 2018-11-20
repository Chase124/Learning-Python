import random

num = random.randint(1, 100)


print ("Guess a number between 1 and 100")

while True:

    guess = input()

    i = int(guess)

    if i == num:
        print("You guessed right")
    elif i < num:
        print('Try higher')
    elif i > num:
        print('Try lower')

