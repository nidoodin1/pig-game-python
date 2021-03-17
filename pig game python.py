#setup
import random#for dice

num = 0 #empty number for math
player = True #True = player 1 False = player 2
point1 = [] #player 1 points
point2 = [] #player 2 points
temp_point = [] #ponints that can be lost
to_win = 30 #how menny you need to win

def roll():#roll the dice random number 1-6
    global num
    num = random.randrange(1,6)
    print (num)
    return num

def roll_bad():#if you rolled a 1 swich player lose temp points
    global temp_point
    print ("you fail")
    temp_point.clear()
    swap()

def roll_good(num):#add roll to temp points and have anuther roll
    global temp_point   
    temp_point.append(num)
    
def hold():#cash out and add temp points to true points temp points now empty
    if player == True:
        point1.extend(temp_point)
        temp_point.clear()
        print(point1)
    elif player == False:
        point2.extend(temp_point)
        temp_point.clear()
        print(point2)

def win():# check if a player wins #end program hear
    if sum(point1) > to_win:
        print ("player 1 wins")
        return True
    if sum(point2) > to_win:
        print ("player 2 wins")
        return True

def swap():#chang turn
    global player  
    if player == True:
        player = False
        temp_point.clear()
        print ("player 2 turn")
    else: #player == False:
        player = True
        temp_point.clear()
        print ("player 1 turn")

def see():#see how menny points
    print("player 1" , point1)
    print("player 2" , point2)

def helpme():#get help
    print("roll to roll dice\nhold to cash out\nsee to see the points")

print("type help for help")
print("player 1 turn")
while True:#main loop
    pick = input ("")#input

    if pick == "roll":#pick roll
        got = roll()
        if got != 1:
            roll_good(got)

        else:
            roll_bad()
            
    elif pick == "hold":#pick hold
        hold()
        if win() == True:
            break
        swap()

    elif pick == "see":#pick see
        see()

    elif pick == "help":#pick help
        helpme()

    else:#pick error try again
        print("input error")

see()
print("\n-----end of program-----\n") 

  

    
       

















    
