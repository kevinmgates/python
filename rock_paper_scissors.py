# computer_choice = "scissors"
import random

computer_choice = random.choice(["scissors", "paper", "rock"])
user_choice = input("rock, paper or scissors?! ")

if computer_choice == user_choice:
    print("tie! the computer chose: " + computer_choice)
elif user_choice == "rock" and computer_choice == "scissors":
    print("you win! the computer chose: " + computer_choice)
elif user_choice == "paper" and computer_choice == "rock":
    print("you win! the computer chose: " + computer_choice)
elif user_choice == "scissors" and computer_choice == "paper":
    print("you win! the computer chose: " + computer_choice)
else:
    print("you lose! the computer chose: " + computer_choice)