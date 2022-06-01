import random
Name=input("enter your name : ")
user_score=0
pc_score=0
nuls=0
Listchoice=["Paper","Rock","Scissors"]

while True :
    print(Name,":",user_score)
    print("PC Score : ",pc_score)
    print("match nuls :",nuls)
    User_coup=input("enter your  coup :(P)aper,(R)ock,(S)cissors,(Q)uit")
    if User_coup =='Q':
        break
    if User_coup !="P" and User_coup != "R"and User_coup != "S" and User_coup != "Q":
        continue
    if User_coup =="P":
        print("Paper vs ......",random.choice(Listchoice))
    elif User_coup == "R":
        print("Rock vs ......", end=" ")
    else :
        print("Scissors vs ......", end=" ")

    Pc=random.choice(Listchoice)
    if Pc =="P":
        coupPC= "P"
        print("Paper")
    elif Pc == "R":
        coupPC= "R"
        print("Rock")
    else :
        coupPC= "S"
        print("Scissors")

    if User_coup == coupPC :
        print("match nul")
        nuls=nuls+1
    elif User_coup =="R" and coupPC =="S":
        print("you win")
        user_score=user_score +1
    elif User_coup =="R" and coupPC =="P":
        print("PC win")
        pc_score=pc_score +1
    elif User_coup =="P" and coupPC =="S":
        print("PC win")
        pc_score=pc_score +1
    elif User_coup =="P" and coupPC =="R":
        print("you win")
        user_score=user_score +1
    elif User_coup =="S" and coupPC =="R":
        print("PC win")
        pc_score=pc_score +1
    elif User_coup =="S" and coupPC =="P":
        print("you win")
        user_score=user_score +1


