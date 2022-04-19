#To get a random number and  in the variable randrange
from random import randrange
 #greetings and point/round system
name = input("Insert your name: ")
print("Hello " + name + " help to guess the number that i'm  guessing. ")
points = 0
totalRounds = 1
#ask to re-play 
play_again = "Y"
# a while loop with the game and the re-play for the game
while play_again == "Y":
    number = randrange(0, 1001)
    for guesses in range(1, 11):
        print("rounds ", totalRounds, " out of ", 20 )
        print("attempt ", guesses, " out of ", 10 )
        NumberGues = int(input())
        if int(NumberGues) < int(number):
            print("You guessed to low")
        elif int(NumberGues) > int(number):
            print("You guessed to high")
        elif int(NumberGues) and int(number) < 50:
            print("You are warm")
        elif int(NumberGues) and int(number) < 20:
            print("You are really warm")
        if int(NumberGues) == int(number):
            break    
    if int(NumberGues) == int(number):
        points = points + 1
        guesses = str(guesses)
        print("cool " + name + ", you guessed the number in " + guesses + " rounds. ")
        play_again = input("Do you want to play again? [Y/N] ")
        if play_again == "Y":
            totalRounds = totalRounds + 1
            if totalRounds == 20:
                break
        elif play_again == "N":
            print("Thanks for playing!! ")           
    elif int(NumberGues) != int(number):
        number = str(number)
        print("Bad luck " + name + ", the number i was thinking of was " + number + ".")
        play_again = input("Do you want to play again? [Y/N] ")
        if play_again == "Y":
            totalRounds = totalRounds + 1
            if totalRounds == 21:
                print("That was all the rounds !!")
                break
        elif play_again == "N":
            print("Thanks for playing!! ")
    if totalRounds <= 20:
        print(name + " your score is: " + str(points))


