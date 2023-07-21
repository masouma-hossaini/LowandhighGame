print("welcome to High Low game!")

import random
hardness = input("Choose a hardness level: Easy(1), Medium(2), Hard(3), Legendary(4): ")

if hardness == "1":
    highest_val = 10
    lowest_val = 1
    print("you have chosen the Easy level!")
elif hardness == "2":
    highest_val = 100
    lowest_val = 1
    print("you have chosen the Medium level!")
elif hardness == "3":
    highest_val = 500
    lowest_val = 1
    print("you have chosen the Hard level!")
else:
    highest_val = 1000
    lowest_val = 1
    print("you have chosen the Legendary level!")

answer = random.randint(lowest_val, highest_val)
guess = 0
print("please start guessing a number from {} to {}".format(lowest_val, highest_val))

while guess < 10:
    guesses = int(input())
    guess +=1
    print("it was your {} guess.".format(guess))
    if guesses == 0:
        break
    if guesses == answer:
        print("Good job! you guessed the number.")
        print("you can keep playing by choosing another level of the game.")
        break
    else:
        if guesses<answer:
            print("please guess higher, or type 0 to quit!")
        else:
            print("please guess lower, or type 0 to quit!")
if guesses != answer:
    print("Ops! you lost your chances. The number was {}".format(answer))