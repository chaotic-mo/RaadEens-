#This to load the function randrange in
from random import randrange
#This is the welcome message
print('Welkom to the guessing game! ')
print('You need to guess the number between 1 and 1000. ')
#This the varbiable to save the random range answer in
ToGuessNumber = randrange(0, 1001)
#This for-in statement is used for the amount of attempts to guess the number
for i in range(0, 21):
    print('attempt', i, 'of', 21)
#This Variable is made to save the number that the user has put in
    inPuttingTekst = input('> choose a number between 1 and 1000 and press [ENTER]: ')
#This for-in statement is used for giving more hints if the number is higher or lower than taht you guessed
    if int(inPuttingTekst) > ToGuessNumber:
        print('You need to guess lower! ')
    elif int(inPuttingTekst) < ToGuessNumber:
        print('Guess Higher!! ')
    elif i == 20:
        break
#This varbiale is used to make the tekst readble in numbers
    InsurdedNumber = int(inPuttingTekst)
#This if-else statement is used to determine if the guessed the number or not
    if int(inPuttingTekst) == ToGuessNumber:
        print('You have geussed the answer! ')
        break
    else:
        print('You did not guessed it try agin?. ', '\n')