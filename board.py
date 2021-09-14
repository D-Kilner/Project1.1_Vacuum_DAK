#imports classes
import Square
import random
from vacuum import Vacuum
from pprint import pprint
import copy

class Board:

    def __init__ (self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.vacuum = Vacuum(0,0)
        self.arr = [[0 for i in range(columns)] for j in range(rows)]
        self.ResetBoard()
        self.Clean()

# resets the board
    def ResetBoard(self):
        rows = 0
        columns = 0
        while rows < self.rows:
            columns = 0
            while columns < self.columns:
                dirt = random.randrange(0,2)
                if dirt == 1:
                    self.arr[rows][columns] = Square.Square(True, False, rows, columns)
                else:
                    self.arr[rows][columns] = Square.Square(False, False, rows, columns)
                columns = columns + 1
            rows = rows + 1


        x = random.randrange(0, self.rows)
        y = random.randrange(0, self.columns)

        self.arr[x][y].isOccupied = True
        self.vacuum.X = x
        self.vacuum.Y = y
        self.PrintBoard()

# prints out each board state 
    def PrintBoard(self):
        for i in range(self.rows):
            rowString = ""
            for j in range(self.columns):
                if self.arr[i][j].isOccupied == True and self.arr[i][j].isDirty == True:
                   rowString = rowString + "DO "
            
                elif self.arr[i][j].isOccupied == False and self.arr[i][j].isDirty == True:
                    rowString = rowString + "DU "
                else:
                    rowString = rowString + "CU "

            print(rowString)
        print("\n")


    def canMoveUp(self, x, y):
        if (self.vacuum.X > 0):
            return True
        return False

    def canMoveDown(self, x, y):
        if (self.vacuum.X < self.rows - 1):
            return True
        return False

    def canMoveLeft(self, x, y):
        if (self.vacuum.Y > 0):
            return True
        return False

    def canMoveRight(self, x, y):
        if (self.vacuum.Y < self.columns - 1):
            return True
        return False

    def removeVacuum(self):
        self.arr[self.vacuum.X][self.vacuum.Y].CleanUp()
        self.arr[self.vacuum.X][self.vacuum.Y].MoveOut()

    def placeVacuum(self):
        self.arr[self.vacuum.X][self.vacuum.Y].CleanUp()
        self.arr[self.vacuum.X][self.vacuum.Y].MoveIn()

    def MoveUp(self):
        if self.canMoveUp(self.vacuum.X, self.vacuum.Y):
            self.removeVacuum()
            self.vacuum.X = self.vacuum.X - 1
            self.placeVacuum()
            self.PrintBoard()
            self.vacuum.MoveCount = self.vacuum.MoveCount + 1

    def MoveDown(self):
        if self.canMoveDown(self.vacuum.X, self.vacuum.Y):
            self.removeVacuum()
            self.vacuum.X = self.vacuum.X + 1
            self.placeVacuum()
            self.PrintBoard()
            self.vacuum.MoveCount = self.vacuum.MoveCount + 1

    def MoveLeft(self):
        if self.canMoveLeft(self.vacuum.X, self.vacuum.Y):
            self.removeVacuum()
            self.vacuum.Y = self.vacuum.Y - 1
            self.placeVacuum()
            self.PrintBoard()
            self.vacuum.MoveCount = self.vacuum.MoveCount + 1


    def MoveRight(self):
        if self.canMoveDown(self.vacuum.X, self.vacuum.Y):
            self.removeVacuum()
            self.vacuum.Y = self.vacuum.Y + 1
            self.placeVacuum()
            self.PrintBoard()
            self.vacuum.MoveCount = self.vacuum.MoveCount + 1

    def UpDirty(self):
        if self.canMoveUp(self.vacuum.X, self.vacuum.Y):
            if self.arr[self.vacuum.X-1][self.vacuum.Y].hasCleaned != True:
                return True
        return False

    def DownDirty(self):
        if self.canMoveDown(self.vacuum.X, self.vacuum.Y):
            if self.arr[self.vacuum.X+1][self.vacuum.Y].hasCleaned != True:
                return True
        return False



    def LeftDirty(self):
        if self.canMoveLeft(self.vacuum.X, self.vacuum.Y):
            if self.arr[self.vacuum.X][self.vacuum.Y-1].hasCleaned != True:
                return True
        return False

    def RightDirty(self):
        if self.canMoveDown(self.vacuum.X, self.vacuum.Y):
            if self.arr[self.vacuum.X][self.vacuum.Y+1].hasCleaned != True:
                return True
        return False

    def Clean(self):
        #snake pattern
        while self.canMoveUp(self.vacuum.X, self.vacuum.Y):
            self.MoveUp()

        while self.canMoveLeft(self.vacuum.X, self.vacuum.Y):

            self.MoveLeft()

        while self.canMoveRight(self.vacuum.X, self.vacuum.Y):

            while self.canMoveDown(self.vacuum.X, self.vacuum.Y):
                self.MoveDown()

            if self.canMoveRight(self.vacuum.X, self.vacuum.Y):
                self.MoveRight()

            while self.canMoveUp(self.vacuum.X, self.vacuum.Y):
                self.MoveUp()

            if self.canMoveRight(self.vacuum.X, self.vacuum.Y):
                self.MoveRight()
        print("All Clean")
        print("Moved " + str(self.vacuum.MoveCount) + " Spaces")