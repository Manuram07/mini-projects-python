def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

cal={"+":add,
     "-":sub,
     "*":mul,
     "/":div }
import art
print(art.callogo)
rep=True
while 1==1:
    if rep==True:
        n1=float(input("What's the first number?: "))
    else:
        n1=r
    for i in cal:
        print(i)
    opp=input("Pick an operation: ")
    n2=float(input("What's the next number?: "))
    r=cal[opp](n1,n2)
    print(f"{n1} {opp} {n2} = {r}")
    con=input(f"Type 'y' to continue calculating with {r}, or type 'n' to start a new calculation: ")
    if con=="y":
        rep=False
    elif con =="n":
        print("\n"*30)
        rep=True