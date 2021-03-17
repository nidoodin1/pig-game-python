#setup
import random

num = 0
player = True
point1 = []
point2 = []
temp_point = []
player1_history = []
player2_history = []

def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1 

def roll():#roll the dice random number 1-6
    global num
    num = random.randrange(1,6)
    print (num)
    return num

def roll_bad():#rolled a 1 swich player lose temp points
    global temp_point
    print ("you fail")
    temp_point.clear()
    print(temp_point)
    swap()


def roll_good(num):#rolld more then one add to temp points
    global temp_point
    
    temp_point.append(num)
    


def hold():#cash out add temp points to points change turn
    if player == True:
        print ("player 1 turn")
        #print(temp_point)
        point1.extend(temp_point)
        temp_point.clear()
        print(point1)
    elif player == False:
        print ("player 2 turn")
        point2.extend(temp_point)
        temp_point.clear()
        print(point2)

    swap()


def win():# check if a player wins
    if sum(point1) > 10:
        print ("player 1 wins")
    if sum(point2) > 10:
        print ("player 2 wins")

def swap():
    global player
    
    if player == True:
        player = False
        temp_point.clear()
        print ("player 2 turn")
    else: #player == False:
        player = True
        temp_point.clear()
        print ("player 1 turn")

def see():
    print("player 1" , point1)
    print("player 2" , point2)

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

    elif pick == "see":
        see()

    else:
        print("input error")

    

  

    
       

















    
