import random

def drawBoard(spots):
    board = (f"| {spots[1]} {spots[2]} {spots[3]} |\n"
             f"| {spots[4]} {spots[5]} {spots[6]} |\n"
             f"| {spots[7]} {spots[8]} {spots[9]} |")
    print(board)
def checkSpace(position, spots):
    return spots[position] not in {'X', 'O'}
def checkTurn(turn):
    if turn % 2 == 0: return 'X'
    else: return 'O'
def aiMove(spots):
    for position in range(1, 10):
        if checkSpace(position, spots):
            spots[position] = 'O'
            if checkForWin(spots):
                spots[position] = str(position)
                return position
            spots[position] = str(position)
    
    for position in range(1, 10):
        if checkSpace(position, spots):
            spots[position] = 'X'
            if checkForWin(spots):
                spots[position] = str(position)
                return position
            spots[position] = str(position)
    
    emptySpots = [position for position in range(1, 10) if checkSpace(position, spots)]
    return random.choice(emptySpots)

def checkForWin(spots):
    if (spots[1] == spots[2] == spots[3]) \
        or (spots[4] == spots[5] == spots[6]) \
            or (spots[7] == spots[8] == spots[9]):
                return True
    elif (spots[1] == spots[4] == spots[7]) \
        or (spots[2] == spots[5] == spots[8]) \
            or (spots[3] == spots[6] == spots[9]):
                return True
    elif (spots[1] == spots[5] == spots[9]) \
        or (spots[3] == spots[5] == spots[7]):
                return True
    else: return False
