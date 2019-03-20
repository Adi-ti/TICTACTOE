from __future__ import print_function
import sys
ways = []

for x in range (0, 9) :
    ways.append(str(x + 1))

playerOneTurn = True
winner = False

def printBoard() :
    print( '\n -----')
    print("This Game is developed by Aditi")
    print("Board looks like-----------------")
    print( '|' + ways[0] + '|' + ways[1] + '|' + ways[2] + '|')
    print( ' -----')
    print( '|' + ways[3] + '|' + ways[4] + '|' + ways[5] + '|')
    print( ' -----')
    print( '|' + ways[6] + '|' + ways[7] + '|' + ways[8] + '|')
    print( ' -----\n')
a=0
while not winner :

    printBoard()
    
    if(a>=9):
        print("Draw!Better luck next time")
        sys.exit()
    if playerOneTurn :
        print( "Player 1:")
    else :
        print( "Player 2:")

    try:
        way = int(input(">> "))
    except:
        print("What are you doing?")
        continue
    if(way>9):
        sys.exit()
    if ways[way - 1] == 'X' or ways [way-1] == 'O':
        print("Invalid number chosen by you")
        continue

    if playerOneTurn :
        a+=1
        ways[way - 1] = 'X'
    else :
        a+=1
        ways[way - 1] = 'O'

    playerOneTurn = not playerOneTurn

    for x in range (0, 3) :
        y = x * 3
        if (ways[y] == ways[(y + 1)] and ways[y] == ways[(y + 2)]) :
            winner = True
            printBoard()
        if (ways[x] == ways[(x + 3)] and ways[x] == ways[(x + 6)]) :
            winner = True
            printBoard()

    if((ways[0] == ways[4] and ways[0] == ways[8]) or 
       (ways[2] == ways[4] and ways[4] == ways[6])) :
        winner = True
        printBoard()

print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")
