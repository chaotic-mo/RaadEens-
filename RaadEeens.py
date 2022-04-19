#This to load the function randrange in
from random import randrange
#This is the welcome message
print('Welkom to the guessing game! ')
print('You need to guess teh number between 1 and 10. ')
#This the varbiable to save the random range answer in
ToGuessNumber = randrange(1, 10)
#This for-in statement is used for the amount of attempts to guess the number
for i in range(1, 5):
    print('attempt', i, 'of', 5)
#This Variable is made to save the number that the user has put in
    inPuttingTekst = input('> choose a number between 1 and 10 and press [ENTER]: ')
#This for-in statement is used for giving more hints if the number is higher or lower than taht you guessed
    if int(inPuttingTekst) > ToGuessNumber:
        print('You need to guess lower! ')
    else:
        print('Guess Higher!! ')

#This if-else statement is used to determine if the guessed the number or not
    if int(inPuttingTekst) == ToGuessNumber:
        print('You have geussed the answer! ')
        break
    else:
        print('Try it again. ', '\n')

