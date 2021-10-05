import random
randNumber = random.randint(1, 5)
# print(randNumber)

userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("guesss a number/n"))
    guesses = guesses+1

    if(userGuess == randNumber):
        print(f"u guessed the right! and number is {randNumber}")
    else:
        if(userGuess > randNumber):
            print("please choose smaller num/n")
        else:
            print("please choose higher valued number!/n")

print(f"you guessed the number in {guesses} gueesses")

with open("hi.txt", "r") as f:
    hi = int(f.read())

if(guesses < hi):
    print(f"you have scored hiscore of {guesses}")
with open("hi.txt", "w") as f:
    f.write(str(guesses))
