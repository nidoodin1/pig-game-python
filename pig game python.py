
import random  # For dice rolls
import colored
from colored import fg, attr, stylize

color = colored.fg("blue")
num = 0
player = True  # True = Player 1, False = Player 2
point1 = []  # Points for Player 1
point2 = []  # Points for Player 2
temp_point = []  # Points that can be lost
to_win = 15  # Points required to win
pink = colored.fg("hot_pink_3a")


def roll():
    """ Rolls 6 sided dice """
    global num
    num = random.randrange(1, 6)
    return num


def roll_bad():
    """ Event for bad roll """
    global temp_point
    print(stylize("You rolled a 1, next player's turn", color))
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
        print(color + "", point1)
    elif player == False:
        point2.extend(temp_point)
        temp_point.clear()
        print(color + "", point2)


def win():
    """ Checks for win by either player """
    if sum(point1) > to_win:
        print(stylize("Player 1 wins", color))
        return True
    if sum(point2) > to_win:
        print(stylize("Player 2 wins", color))
        return True


def swap():
    """ Swap player turn """
    global player
    global color
    if player == True:
        player = False
        temp_point.clear()
        color = colored.fg("red")
        print(stylize("Player 2's turn", color))
    else:  # player == False:
        player = True
        temp_point.clear()
        color = colored.fg("blue")
        print(stylize("Player 1's turn", color))


def see():
    """ Display number of points for both players """
    print(color + "Player 1 points:", point1)
    print(color + "Player 2 points:", point2)


def helpme():
    """ Display help """
    print("Type 'roll' to roll dice\nType 'hold' to cash out\nType 'see' to see the points")


print("Type 'help' for help")
print(stylize("Player 1's turn", color))

# Main loop
while True:
    # Get player input
    pick = input("> ")

    # Roll picked
    if pick == "roll":
        result = roll()
        print(color + "You rolled:", result)
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
print(stylize("\n-----end of program-----\n", pink))














