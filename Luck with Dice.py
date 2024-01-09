import random
#Function for die roll
def roll():
    min=1
    max=6
    roll=random.randint(min,max)
    return roll
#main
#Rules
print("!!Rules!!\n1.Try to get any Number Other than 1, to add that number total score but if you get 1\n Score get reset to 0\n")
#Taking Winning Score as Input
while True:
    Winning_Score=input("Enter Winning Score (50 to 100)\n")
    if(Winning_Score.isdigit()):
            Winning_Score=int(Winning_Score)
            if(100>=Winning_Score>=50):
                print(f"Winning Score Set to {Winning_Score}")
                break
            elif(Winning_Score>100):
                print("Any Score Kept higher than 100, will cause game to extend for a long period to make it boring\nPlease Enter Winning Score within 50 to 100")
            else:
                print("Invalid Input\nPlease Keep Winning Score between 50 to 100")
    else:
        print("Invalid Input")
#Taking Number of Player as input
while True:
    players=input("Enter Number of Player (2-4) :  ")
    if(players.isdigit()):
        players=int(players)
        if(4>=players>=2):
            break
        else:
            print("Invalid Input\nPlease Enter Number of Players Between 2-4")
    else:
        print("Invlaid Input")

Indi_Score=[0 for i in range(players)] #List for All Score
i=0 #variable for travserling All Score
#Actucall Game Working
while True:
    if(max(Indi_Score)<Winning_Score): # Always Checking if anybody won
        print("Would you like to roll Player ",(i+1),"\n1.Yes\t2.No")
        opt=input()
        if(opt.isdigit()):
            opt=int(opt) #kardiya bas
            if(opt==1):
                value=roll();
                if(value!=1):
                    print("You got",value)
                    Indi_Score[i]+=value
                    print(f"Your Current Score is {Indi_Score[i]}")
                else:
                    print(f"Luck, Not on Your Side\n{Indi_Score[i]} to Zero")
                    Indi_Score[i]=0
                    if(i==(players-1)):
                        i=0
                    else:
                        i+=1
            else:
                if (i==(players-1)):
                    i=0
                else:
                    i+=1
        else:
            print("Invalid Option")
    else:
        break
print("Player",(i+1),"Congrats,Luck was on your side, Unlike her...")


















































