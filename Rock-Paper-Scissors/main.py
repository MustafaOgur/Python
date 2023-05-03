import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_of_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

game_list = ["Rock","Paper","Scissors"]

choice_of_computer = game_list[random.randint(0,2)]

if choice_of_user == 0:
  print("\nYour chose:")
  print(rock)
  print("\nComputer chose:")
  if choice_of_computer == "Rock":
    print(rock)
    print("\nIt's a draw!")
  elif choice_of_computer == "Paper":
    print(paper)
    print("\nYou lose!")
  else:
    print(scissors)
    print("\nYou win!")

elif choice_of_user == 1:
  print("\nYour chose:")
  print(paper)
  print("\nComputer chose:")
  if choice_of_computer == "Rock":
    print(rock)
    print("\nYou win!")
  elif choice_of_computer == "Paper":
    print(paper)
    print("\nIt's a draw!")
  else:
    print(scissors)
    print("\nYou lose!")

elif choice_of_user == 2:
  print("\nYour chose:")
  print(scissors)
  print("\nComputer chose:")
  if choice_of_computer == "Rock":
    print(rock)
    print("\nYou lose!")
  elif choice_of_computer == "Paper":
    print(paper)
    print("\nYou win!")
  else:
    print(scissors)
    print("\nIt's a draw!")

else:
  print("\nPlease write one of the numbers 0 , 1 or 2 !!!")
    

