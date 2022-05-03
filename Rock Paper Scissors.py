import random

print("Hello and welcome to this rock, paper, and scissors game!!")
confirm = input("Type y to continue: ")

print("")

if confirm.lower() == "y":
  print("Let's Goo!!")
else:
  quit()

user_score = 0
computer_score = 0

Options = ["rock", "paper", "scissors"]

def compare():
  if user_score > computer_score:
    print("Nice job you win!!")
  elif computer_score > user_score:
    print("You lost!!")
  elif user_score == computer_score:
    print("It's a tie! No one won!")

while True:
  user_choice = input("Type in rock, paper, or scissors, and q to quit: ").lower()

  print("")

  if user_choice == "q":
    print("Thanks for Playing!")
    print("You scored", user_score)
    print("The computer scored", computer_score)
    compare()
    print("")
    quit()
  elif user_choice not in Options:
    continue
  
  random_number = random.randint(0, 2)
  computer_choice = Options[random_number]
  comp_msg = print("The computer chose", computer_choice + ".")

  if user_choice == "rock" and computer_choice == "scissors":
    print("You won!")
    user_score += 1
  elif user_choice == "paper" and computer_choice == "rock":
    print("You won!")
    user_score += 1
  elif user_choice == "scissors" and computer_choice == "paper":
    print("You won!")
    user_score += 1
  elif user_choice == computer_choice:
    print("No one Won")
  else:
    print("You lost")
    computer_score += 1
  
 


  
  
