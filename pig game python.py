#setup
import random

num = 0
player = True
point1 = []
point2 = []
temp_point = []
player1_history = []
player2_history = []

def roll():#roll the dice random number 1-6
    num = random.randrange(1,6)
    print (num)
    return num

def roll_bad():#rolled a 1 swich player lose temp points
    print ("you fail")
    if player == True:
        temp_point = []
        swap()
    if player == False:
        temp_point = []
        swap()
        
def roll_good(num):#rolld more then one add to temp points
        temp_point.append(num)


def hold():#cash out add temp points to points change turn
    if player == True:
        point1.append(temp_point)
        print(point1)
    elif player == False:
        point2.append(temp_point)
        print(point2)


def win():# check if a player wins
    if sum(point1) > 100:
        print ("player 1 wins")
    if sum(point2) > 100:
        print ("player 2 wins")

def trc(): #trac history
    print (point1 + "\n" + point2)

def swap():
    global player
    
    if player == True:
        player = False
        print ("player 2 turn")
    elif player == False:
        player = True
        print ("player 1 turn")

while True:
    win()
    pick = input ("roll or hold\n")

    if pick == "roll":
        got = roll()
        if got != 1:
            roll_good(got)

        else:
            roll_bad()
            
    elif pick == "hold":
        hold()

    else:
        print("input error")

  

    
       

















    
