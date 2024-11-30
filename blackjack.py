import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
c_chance=[True,False]
con=True
def s(l):
    return sum(l)
def check(p,c,n):
    if s(p) == 21:
        return win(player, computer, "Win with a Blackjack 😎")
    elif s(c)==21:
        return win(player, computer, "lose with a Blackjack 😭")
    elif s(p)>21:
        return win(player, computer, "You went over. You lose 😭")
    elif s(c)>21:
        return win(player, computer, "Opponent went over. You win 😁")
    elif s(p)==s(c) and n==1:
        return win(player, computer, "Draw 🙃")
    elif s(p)>s(c) and n==1:
        return win(player, computer, "You win 😃")
    elif s(p)<s(c) and n==1:
        return win(player, computer, "You lose 😤")
    else:
        return "y"
def win(player,computer,winner):
    print(f"Your final hand: {player}, final score: {s(player)}")
    print(f"Computer's final hand: {computer}, final score: {s(computer)}")
    print(winner)
    return "n"
print(art.bjlogo)
while(con==True):
    game=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    # print("\n"*30)
    if game=="y":
        player=[]
        computer=[]
        for i in range(2):
            player.append((random.choice(cards)))
        computer.append((random.choice(cards)))
        print(f"Your cards: {player}, current score: {s(player)}")
        print(f"Computer's first card: {computer[0]}")
        chance=check(player,computer,0)
        while (chance == "y"):
            chance = input("Type 'y' to get another card, type 'n' to pass:")
            if chance == "y":
                player.append(random.choice(cards))
                if 11 in player and s(player)>21:
                    player.remove(11)
                    player.append(1)
                print(f"Your cards: {player}, current score: {s(player)}")
                print(f"Computer's first card: {computer[0]}")
                chance=check(player,computer,0)
            else:
                computer.append((random.choice(cards)))
                if s(player)<=s(computer):
                    c_c=False
                    check(player, computer, 1)
                else:
                    c_c=True
                while c_c==True:
                    c_c=random.choice(c_chance)
                    if c_c==True:
                        computer.append((random.choice(cards)))
                        b=check(player, computer, 0)
                        if b != "y":
                            c_c=False
                        else:
                            if s(player) >= s(computer):
                                c_c = True
                            else:
                                c_c = False
                                check(player,computer,1)
                    else:
                        c_c=False
                        check(player, computer, 1)
                chance = "n"    
    elif game=="n":
        con=False
        print("Thank You for playing")
    else:
        print("""   Your final hand: [], final score: undefined
   Computer's final hand: [], final score: undefined
Draw 🙃""")
        con=False
print("Good Bye")