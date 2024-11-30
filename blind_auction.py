import art
print(art.auclogo)
def dic_bits(n,p):
    bit[n]=p
def cal_auc_result(bit):
    max=0
    win="noone"
    for i in bit:
        if bit[i] > max:
            max=bit[i]
            win=i
    print(f"The winner is {win} with a bid of ${max}")
auc=True
bit={}
while(auc==True):
    name=input("What is your name?:")
    price=int(input("What is your bid?: $"))
    dic_bits(n=name,p=price)
    con=input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if con=="no":
        auc=False
    print("\n"*20)
cal_auc_result(bit)