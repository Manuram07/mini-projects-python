import random
ans=random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
diff=input("Choose a difficulty. Type 'easy' or 'hard': ")
lives=0
if diff == "easy":
    lives=10
elif diff=="hard":
    lives=5
else:
    print("Wrong option \ntry again later")
    exit()
while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    if guess==ans:
        print(f"You got it! The answer was {ans}")
        exit()
    elif guess > ans:
        print("Too high.")
        lives -=1
    else:
        print("Too low.")
        lives -=1
    print("Guess again.")
print("You've run out of guesses, you lose.")
print(ans)