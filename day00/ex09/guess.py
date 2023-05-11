from random import randint

def guessIt():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")

    randomN = randint(1, 99)
    trials = 1

    while 1:
        print("What's your guess between 1 and 99?")
        choice = input(">> ")

        if choice.isnumeric():
            choice = int(choice)
            # feedback guess
            if choice < randomN:
                print("Too low!")
            elif choice > randomN:
                print("Too high!")
            else:
                if randomN == 42:
                    print("The answer to the ultimate question of life, the universe and everything is 42.")

                if trials == 1:
                    print("Congratulations! You got it on your first try!")
                else:
                    print("Congratulations, you've got it!")
                    print("You won in {:d} attempts!".format(trials))
                return

        elif choice.lower() == "exit":
            print("Have a nice day!")
            return

        else:
            print("That's not a number.")
        trials += 1


if __name__ == "__main__":
    guessIt()