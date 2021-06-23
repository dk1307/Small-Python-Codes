from random import randint
import sys
 
choice = ["rock","paper","scissors"]
def rps():
    player = input("\nEnter Your Choice: ").lower()
    computer = choice[randint(0,2)]
    print("\nHere Computer Chose: " + computer)
 
    if player == computer:
        print("\nHeyy It's Draw!! Better luck next time.")
    elif player == "rock" and computer == "paper":
        print("\nHeyy Computer Wins!! Better luck next time.")
    elif player == "rock" and computer == "scissors":
        print("\nHeyy You Win!!")
    elif player == "paper" and computer == "rock":
        print("\nHeyy You Wins!!")
    elif player == "paper" and computer == "scissors":
        print("\nHeyy Computer Wins!! Better luck next time.")
    elif player == "scissors" and computer  == "rock":
        print("\nHeyy Computer Wins!! Better luck next time.")
    elif player == "scissors" and computer == "paper":
        print("\nHeyy You Wins!!")
    elif player == "end":
        sys.exit("Heyy Thank you for playing my game!!") 

    rps()

def main():
    print("\nWelcome to my custom the Rock, Paper, Scissors Game.")
    print("Enter 'end' to exit for this game.")
    rps()
    
main()