import random

random = random.randint(1,10)
tries = 3

print("This is a game, called 'Guess the number from 1 to 10'")
print("Number is selected. Try to guess")

for i in range(1, tries+1):
    try:
        guess = int(input("Enter your guess: "))
        if guess == random:
            print("Good job!")
        if guess > random:
            print("Try a less one")
        if guess < random:
            print("Try a bigger one")
    except ValueError:
        print("No, we need whole number")
else:
    print(f"Ha ha, loser. The number I remembered is {random}")