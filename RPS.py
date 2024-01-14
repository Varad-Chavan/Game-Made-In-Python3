import random
import time
def gen():
    min_value=1;
    max_value=3;
    roll=random.randint(min_value,max_value)
    return roll;

def display(opt):
    if(opt==1):
        print("Computer Did Rock")
    elif(opt==2):
        print("Computer Did Paper")
    elif(opt==3):
        print("Computer Did Scissors")

def check(human,comp):
    if(human==comp):
        return 2
    elif(human == 1 and comp == 3):
        return 1
    elif (human == 2 and comp == 1):
        return 1
    elif (human == 3 and comp == 2):
        return 1
    else:
        return 0

#
print("!!Rules!!\n1. Rock Kills Scissor\n2. Scissor Kills Paper\n3. Paper Kills Rock \n")

while True:
    number_of_round=input("Enter Number of Rounds in the multiple of 10s (1 to 5)\n")
    if(number_of_round.isdigit()):
        number_of_round=int(number_of_round)
        if(5>=number_of_round>=1):
            print("Done....\n")
            break
        else:
            print("!! Out of Range !!\nEnter Between 1 to 5\n")
    else:
        print("Invalid Input\n")
HwinCount=0
CwinCount=0
for x in range(1,number_of_round*10):
    print(f"Round {x}")
    while True:
        choice=input("Enter Your Choice\n1.Rock\n2.Paper\n3.Scissors\n")
        if(choice.isdigit()):
            choice=int(choice)
            if(choice==1):
                print("You Selected, Rock")
                time.sleep(2)
                break;
            elif(choice==2):
                print("You Selected, Paper")
                time.sleep(2)
                break;
            elif(choice==3):
                print("You Selected, Scissors")
                time.sleep(2)
                break;
            else:
                print("We Dont Appericate Anything Other Than Rock,Paper,Scissors\n")
        else:
            print("We Dont Appericate Anything Other Than Rock,Paper,Scissors\n")

    Choice=gen()
    result=check(choice,Choice)
    match result:
        case 0:
            print("Your Loose")
            CwinCount+=1
            display(Choice)
            print(f"ScoreCard\nYou - {HwinCount}\nComputer - {CwinCount}\n")
        case 1:
            print("You Won")
            HwinCount+=1
            display(Choice)
            print(f"ScoreCard\nYou - {HwinCount}\nComputer - {CwinCount}\n")
        case 2:
            print("It was a Draw\n")
            display(Choice)
            print(f"ScoreCard\nYou - {HwinCount}\nComputer - {CwinCount}\n")

if(CwinCount>HwinCount):
    print("Try Better Luck Next Time, Computer Won")
    print(f"Final ScoreCard\nYou - {HwinCount}\nComputer - {CwinCount}\n")
elif(CwinCount==HwinCount):
    print("It was a Draw")
    print(f"Final ScoreCard\nYou - {HwinCount}\nComputer - {CwinCount}\n")
else:
    print("Congrats Your Won\n")
    print(f"Final ScoreCard\nYou - {HwinCount}\nComputer - {CwinCount}\n")