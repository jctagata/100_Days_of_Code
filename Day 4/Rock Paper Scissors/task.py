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

move_list = [rock, paper, scissors]

computer_move = random.randint(0,2)

human_move = int(input("1 - Rock\n"
                     "2 - Paper\n"
                     "3 - Scissors?\n"
                     "Play your move!: ")) - 1

print(f"You picked:\n"
      f"{move_list[human_move]}")

print(f"Computer picked:\n"
      f"{move_list[computer_move]}")

if human_move == computer_move:
    print("It's a draw...")
elif human_move == 0:
    if computer_move == 1:
        print("You lose...")
    else:
        print("You win!")
elif human_move == 1:
    if computer_move == 2:
        print("You lose...")
    else:
        print("You win!")

elif human_move == 2:
    if computer_move == 0:
        print("You lose...")
    else:
        print("You win!")