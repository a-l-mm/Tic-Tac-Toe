from setup import drawBoard, checkTurn, checkForWin, checkSpace, aiMove
import os
import time
spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9', }

playing = True
complete = False
turn = 0
prevTurn = -1

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    drawBoard(spots)
    if prevTurn == turn:
        print('Invalid spot, try again.')
    prevTurn = turn
    if checkTurn(turn) == 'X': 
        print('Your turn')
        choice = input()
        if choice == 'q':
             playing = False
             break
        if choice.isdigit():
            choice = int(choice)
            if choice in spots and checkSpace(choice, spots):
                spots[choice] = 'X'
                turn += 1
            else:
                print('Inavlid or taken spot, try again.')
    else: 
        print('Choosing...')
        time.sleep(5)
        choiceAI = aiMove(spots)
        if choiceAI in spots and checkSpace(choiceAI, spots):
            spots[choiceAI] = 'O'
            turn += 1
   
    if checkForWin(spots): playing, complete = False, True
    if turn > 8: playing = False
    os.system('cls' if os.name == 'nt' else 'clear')
    drawBoard(spots)
    if complete:
        if checkTurn(turn) == 'O': print('You win!')
        elif checkTurn(turn) == 'X': print('You lose..')
    else: print('No winner no chicken dinner..')
