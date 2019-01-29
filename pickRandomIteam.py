import random

desserts = ["ice_cream", "pancakes", "brownies", "cookies", "candy"]

correctAnswer = str(random.choice(desserts))
#print correctAnswer
print("Guess a dessert in the string {0}".format(desserts))
guess = raw_input()
word = str(guess)


while (word != correctAnswer): #fix this condition later

    guess = raw_input()

    word = str(guess)

    if word == correctAnswer:
        print("You have guessed the correct dessert")
    else:

        print ("Try again")

        #change the code to inform the user that he guessed the correct word even if he hit it at the first try
        #you are allowed to use only one print("You have guessed the correct dessert") in your code