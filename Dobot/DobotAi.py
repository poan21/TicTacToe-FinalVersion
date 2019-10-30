import random
import time
from DobotMovement import DobotMovement

""" Module with DobotAi class """

class DobotAi():
    """ DobotAi decisions """

    def __init__(self, game, dm=None, difficulty="easy"):
        self.diff = difficulty
        self.currGame = game
        self.dm = dm

    def decideMove(self):
        """ Calculating where to place his piece """

        print("Deciding move...")
        if self.diff == "easy":
            return self.easyMove()
        elif self.diff == "hard":
            num = self.hardMove()
            self.dm.placePos(num)
            time.sleep(3)
            return num

    def easyMove(self):
        """ Making a randomly generated move """

        while True:
            rngPlace = random.randint(0, 8)
            if self.currGame.board[int(rngPlace)] == "_":
                time.sleep(3)
                self.dm.placePos(rngPlace)
                return rngPlace

    def hardMove(self):
        """ Making move that follows a certain condition, otherwise random. """
        if len(set(self.currGame.board)) == 1:
            return 8

        dPiece = self.currGame.dobot
        pPiece = self.currGame.player
        winningPatterns=[
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
        ]

        for pat in winningPatterns:
            if self.currGame.board[pat[0]] == dPiece:
                if self.currGame.board[pat[1]] == dPiece:
                    if self.currGame.board[pat[2]] == "_":
                        return pat[2]
                elif self.currGame.board[pat[2]] == dPiece:
                    if self.currGame.board[pat[1]] == "_":
                        return pat[1]
            elif self.currGame.board[pat[1]] == dPiece:
                if self.currGame.board[pat[2]] == dPiece:
                    if self.currGame.board[pat[0]] == "_":
                        return pat[0]

        for pat in winningPatterns:
            if self.currGame.board[pat[0]] == pPiece:
                if self.currGame.board[pat[1]] == pPiece:
                    if self.currGame.board[pat[2]] == "_":
                        return pat[2]
                elif self.currGame.board[pat[2]] == pPiece:
                    if self.currGame.board[pat[1]] == "_":
                        return pat[1]
            elif self.currGame.board[pat[1]] == pPiece:
                if self.currGame.board[pat[2]] == pPiece:
                    if self.currGame.board[pat[0]] == "_":
                        return pat[0]

        if self.currGame.board.count("_") == 7:
            if self.currGame.board[4] == pPiece:
                return 0
            else:
                if self.currGame.board[2] == "_" and self.currGame.board[5] == "_":
                    return 2
                else:
                    return 6

        if self.currGame.board.count("_") == 5:
            if self.currGame.board[2] == dPiece and self.currGame.board[1] == "_" and self.currGame.board[0] == "_":
                return 0
            elif self.currGame.board[2] == dPiece and self.currGame.board[6] == "_" and self.currGame.board[7] == "_":
                return 6

            if self.currGame.board[6] == dPiece and self.currGame.board[0] == "_":
                return 0
            elif self.currGame.board[6] == dPiece and self.currGame.board[2] == "_":
                return 2


        if self.currGame.board.count("_") == 8:
            if self.currGame.board[4] == "_":
                return 4
            else:
                return 8

        if self.currGame.board.count("_") == 6 and self.currGame.board[4] == dPiece:
            if self.currGame.board[1] == "_":
                return 1
            elif self.currGame.board[3] == "_":
                return 3
            elif self.currGame.board[5] == "_":
                return 5
            else:
                return 7

        if self.currGame.board.count("_") == 6 and self.currGame.board[4] == pPiece and self.currGame.board[4] == pPiece:
            return 2

        return self.easyMove()
