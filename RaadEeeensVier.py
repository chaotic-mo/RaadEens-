import random
TotalRounds =  0
#This is the welcome message
print("Welkom to the guessing game! " )
print("You need to guess the number between 1 and 1000. ")

name = input("please type your name: ")
number = random.randint(0,1001)
print("Hello " + name + ", I'm thinking of a number between 1 and 1000. ")

while TotalRounds <= 20:
    print("Try to guess")
    print('attempt', TotalRounds, 'of', 20)
    Trials = int(input())
    TotalRounds = TotalRounds + 1
    if Trials < number:
        print("You guessed to low. ")
    elif Trials and number < 50:
        print("You are reall hot!! ")
    elif Trials and number < 20:
        print("You are really really hot!! ")
    elif Trials > number:
        print("You guessed to High. ")
    elif Trials == number:
        break

if Trials == number:
    TotalRounds = str(TotalRounds)
    print("Cool " + name +", You guessed the number in " + TotalRounds + " rounds. ")
elif Trials != number:
    number = str(number)
    print("Bad luck" + name + ", the number i was thinking of was " 
    + number + ".")

