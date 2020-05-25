from random import randint

tofind = randint(1, 99)


def menu(attempt):
    print("\n")
    guess = input("What is your guess between 1 an 99?\n")
    if guess == "exit":
        print("Cya, the secret number was " + str(tofind))
        quit()
    try:
        guess = int(guess)
        attempt += 1
        if guess > tofind:
            print("Too High !")
            menu(attempt)
        elif guess < tofind:
            print("Too Low !")
            menu(attempt)
        elif guess == tofind:
            if tofind == 42:
                print("The answer to the ultimate question of life,", end='')
                print("the universe and everything is 42.")
            print("Congratulations, you've got it !")
            print("You won in {} attempt(s)".format(attempt))
            if attempt == 1:
                print("You should go to the Casino !")
            quit()
    except ValueError:
        print("That's not a number")
        menu(attempt)


print("This is a guessing game!")
print("Try to find the secret number between 1 and 99")
print("Type 'exit' to close the game.")

menu(0)
