import random
from tkinter.font import names

import art
def check(a,b):
    if a["follower_count"]>b["follower_count"]:
        return "a"
    else:
        return "b"
score=0
game=True
print(art.hllogo)
a=random.choice(art.hldata)
while game:
    b=random.choice(art.hldata)
    same=True
    while same:
        if a['name']==b['name']:
            b = random.choice(art.hldata)
        else:
            same=False
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(art.hlvs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
    guess=input("Who has more followers? Type 'A' or 'B': ").lower()
    # print("\n"*30)
    # print(art.hllogo)
    ans=check(a,b)
    if guess==ans:
        score+=1
        print(f"You're right! Current score {score}")
        if guess=="b":
            a=b
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game=False