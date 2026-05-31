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

game_print = [rock, paper, scissors]
print("Welcome to Rock, Paper, Scissor Game")

user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choise >= 0 and user_choise <=2:
    print(game_print[user_choise])

computer_choice = random.randint(0,2)
print(" Computer choose:")
print(game_print[computer_choice])

if user_choise >= 3:
    print("Invalid")
elif user_choise == 0 and computer_choice == 2:
    print("You win")
elif user_choise == 0 and computer_choice == 1:
     print("You lose")
elif user_choise == 1 and computer_choice == 0:
     print("You win")
elif user_choise == 1 and computer_choice == 2:
    print("You lose")
elif user_choise == 2 and computer_choice == 0:
    print("You lose")
elif user_choise == 2 and computer_choice == 1:
    print("You win")
elif user_choise == computer_choice:
    print("It's Draw")
