import random

number=random.randrange(1,100)
print("\nWelcome My custom random guess number game")
guess=int(input("\nGuess a number between 1 to 100:"))

while guess!=number:
    if guess < number:
        print("Heyy you need to guess higher number. try again!")
        guess=int(input("\nGuess a number between 1 to 100:"))
    else:
        print("Heyy you need to guess lower number. try again!")
        guess=int(input("\nGuess a number between 1 to 100:"))

print("Heyy You guessed the number correctley thank you for chossing me!!!")