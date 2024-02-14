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

#Write your code below this line 👇
while 1>0:
    print("what do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.")
    x=int(input())
    y=random.randint(0,2)
    if x==0:
        print(rock)
    elif x==1:
        print(paper)
    else:
        print(scissors)

    print("Computer chose:")
    if y==0:
        print(rock)
    elif y==1:
        print(paper)
    else:
        print(scissors)

    if x==y:
        print("Draw !")


    if x==0 and y==2:
        print("You won!")
    elif x==2 and y==0:
        print("You lose!")

    if x==2 and y==1:
        print("You won!")
    elif x==1 and y==2:
        print("You lose!")

    if x==1 and y==0:
        print("You won!")
    elif x==0 and y==1:
        print("You lose!")









