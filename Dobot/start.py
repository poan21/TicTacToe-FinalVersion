import DobotDllType as ddType
from DobotMovement import DobotMovement
from Game import Game
from DobotAi import DobotAi
from cv2_hough import getAllCircles, grabPos, checkPlaced
import os
""" File that starts the game """

def start():
    """ Function which starts the game """
    os.system("cls")
    print("Ready to play Tic-Tac-Toe with DoBot?")

    """ Select which shape player wants to be """
    x = 0
    while x == 0:
        pShape = input("""
Who would you like to play as, X or O?
--> """)
        if pShape.lower() == "x":
            game = Game("X", "O")
            x = 1
        elif pShape.lower() == "o":
            game = Game("O", "X")
            x = 1
        else:
            input("Incorrect input, please check your spelling...")

    """ Select difficulty """
    x = 0
    while x == 0:
        diffInp = input ("""
Which difficulty would you like to play against?
> Easy
> Hard
--> """)
        if diffInp.lower() == "easy":
            diff = "easy"
            x = 1
        elif diffInp.lower() == "hard":
            diff = "hard"
            x = 1
        else:
            input("Incorrect input, please check your spelling...")

    """ Select who goes first """
    x = 0
    while x == 0:
        fTurn = input("""
Who should go first?
> Player
> DoBot
--> """)
        if fTurn.lower() == "player":
            game.setFirstTurn("1")
            x = 1
        elif fTurn.lower() == "dobot":
            game.setFirstTurn("2")
            x = 1
        else:
            input("Incorrect input, please check your spelling...")

    ai = DobotAi(game, DobotMovement(), diff)

    print("Good luck and have fun!")
    input("\nPress enter to continue...")
    os.system("cls")
    print("Board status")
    game.boardStatus()

    """ While loop that runs until game.announceWinner() finds winner """
    while True:
        if game.player == game.turn:
            """ Player turn """
            print("It's your turn!")
            input("Press enter when you have done your move...")
            placed = checkPlaced(game)
            validPlace = game.place(placed)
            os.system("cls")
        else:
            """ DoBot Turn """
            print("DoBots turn\n")
            move = ai.decideMove()
            validPlace = game.place(move)
        if validPlace:
            """ If valid placement, show board, check if they won or proceed to next turn """
            print("Board status")
            game.boardStatus()
            game.checkWinner()
            game.nextTurn()
        else:
            """ If not valid placement, show board and message """
            game.boardStatus()
            print("Invalid placement, try again.\n")


if __name__ == "__main__":
    start()
