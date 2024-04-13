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
