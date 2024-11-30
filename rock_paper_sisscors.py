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
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
y=int(input())
if y==0:
    print(rock)
elif y==1:
    print(paper)
elif y==2:
    print(scissors)
else:
    print("You typed an invalid number, you lose!")
    exit()
print("computer's chose")
c=[rock,paper,scissors]
p=random.choice(c)
print(p)
if (y==0 and p==scissors)or(y==1 and p==rock)or(y==2 and p==paper):
    print("You won")
elif(y==0 and p==rock)or(y==1 and p==paper)or(y==2 and p== scissors):
    print("Its draw")
else:
    print("You lose")
