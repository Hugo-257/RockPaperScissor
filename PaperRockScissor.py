from math import isfinite
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

game=(rock,paper,scissors)
cp=random.randint(0,2)
player=int(input("What do you choose? Type 0 for rock, 1 for Paper and 2 for Scissors.\n"))
if player==0:
    print(game[0])
    print("Computer choose")
    print(game[cp])
    if cp==1:
        print("You loose")
    elif cp==2:
        print("You win")
    else: 
        print("Equality...")
elif player==1:
    print(game[1])
    print("Computer choose")
    print(game[cp])
    if cp==1:
        print("Equality...")
    elif cp==2:
        print("You lose")
    else: 
        print("you win")

elif player==2 :
    print(game[2])
    print("Computer choose")
    print(game[cp])
    if cp==1:
        print("You win...")
    elif cp==2:
        print("Equality...")
    else: 
        print("You lose")
else:
    print("Invalid choice")


