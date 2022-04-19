import random 
number = random.randint(0, 1001)

name = input("Insert your name: ")
print("Hello" + name + "help to guess the number that i'm  guessing. ")

totalRounds = 0
guesses = 10

def game():
    while totalRounds == guesses:
        print(name + "Try to gues the number that i'm thinking of. ")
        print("attempt", guesses, "of", 10 )
        NumberGues = int(input())
        totalRounds = totalRounds + 1
        if NumberGues < number:
            print("You guessed to low")
        elif NumberGues > number:
            print("You guessed to high")
        elif NumberGues and number < 50:
            print("You are warm")
        elif NumberGues and number < 20:
            print("You are really warm")
        elif NumberGues == number:
            break

    if NumberGues == number:
            totalRounds = str(totalRounds)
            print("cool " + name + ", you guessed the number in " + totalRounds + "rounds. " )
    elif NumberGues != number:
        number = str(number)
        print("Bad luck" + name + ", the number i was thinking of was " + number + ".")

answer = input("Do you want to play again?  [Y/N]")
if answer == "N":
    print("You stopt the game")
elif answer == "Y":
    print("staring the game again.")
    totalRounds = totalRounds + 1
    game()







