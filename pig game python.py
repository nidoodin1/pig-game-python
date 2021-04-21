import random # For dice rolls

num = 0
player = True # True = Player 1, False = Player 2
point1 = [] # Points for Player 1
point2 = [] # Points for Player 2
temp_point = [] # Points that can be lost
to_win = 30 # Points required to win

def roll():
    """ Rolls 6 sided dice """
    global num
    num = random.randrange(1, 6)
    return num

def roll_bad():
    """ Event for bad roll """
    global temp_point
    print ("You rolled a 1, next player's turn")
    temp_point.clear()
    swap()

def roll_good(num):
    """ Event for good roll """
    global temp_point   
    temp_point.append(num)
    
def hold():
    """ Cash out points into table """
    if player == True:
        point1.extend(temp_point)
        temp_point.clear()
        print(point1)
    elif player == False:
        point2.extend(temp_point)
        temp_point.clear()
        print(point2)

def win():
    """ Checks for win by either player """
    if sum(point1) > to_win:
        print("Player 1 wins")
        return True
    if sum(point2) > to_win:
        print("Player 2 wins")
        return True

def swap():
    """ Swap player turn """
    global player  
    if player == True:
        player = False
        temp_point.clear()
        print ("Player 2's turn")
    else: #player == False:
        player = True
        temp_point.clear()
        print ("Player 1's turn")

def see():
    """ Display number of points for both players """
    print("Player 1 points:", point1)
    print("Player 2 points:", point2)

def helpme():
    """ Display help """
    print("Type 'roll' to roll dice\nType 'hold' to cash out\nType 'see' to see the points")


print("Type 'help' for help")
print("Player 1's turn")

# Main loop
while True:
    # Get player input
    pick = input("> ")

    # Roll picked
    if pick == "roll":
        result = roll()
        print("You rolled:", result)
        if result != 1:
            roll_good(result)
        else:
            roll_bad()
            
    # Hold picked
    elif pick == "hold":
        hold()
        if win() == True:
            break
        swap()

    # See picked
    elif pick == "see":
        see()

    # Help picked
    elif pick == "help":
        helpme()

    # Incorrect input
    else:
        print("Wrong input, type 'help' for commands")

see()
print("\n-----end of program-----\n") 

  

    
       

















    
