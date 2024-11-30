MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0
}


def making(menu):
    result=check(menu)
    if result=="y":
        for i in menu["ingredients"]:
            resources[i] -= menu["ingredients"][i]
        return menu["cost"]
    else:
        return None
def check(menu):
    ok=0
    for i in menu["ingredients"]:
        if menu["ingredients"][i] > resources[i]:
            print(f"{i} is not sufficient")
            ok += 1
    if ok == 0:
        return "y"
    else:
        print("Sorry ,please try again later \nYour money is refunded")
        return "n"
        

def reception(b):
    print("Insert Coins")
    q =int(input("quarters :"))
    d = int(input("dimes :"))
    n = int(input("nickles :"))
    p = int(input("pennies :"))
    t=(q*0.25)+(d*0.10)+(n*0.05)+(p*0.01)
    print(f"You have paid ${t}")
    change=t-b
    if change >= 0:
        print(f"Your {user_input} is ready ")
        print(f"your bill is ${b} and you will ${change} back")
        resources["Money"] += b
    else:
        print("insufficient money \nYour money is refunded")

def working(user):
    if user=="report":
        for i in resources:
            print(f"{i}:{resources[i]}")
    elif user=="off":
        print("Thank you")
        exit()
    else:
        bill=making(MENU[user])
        if bill is not None:
            reception(bill)
        
        
        
while 1==1:
    user_input=input("What would you like? (espresso/latte/cappuccino):").lower()
    working(user_input)
