class Square:

   

    def __init__(self, isDirty,isOccupied,X,Y):

        

        self.isDirty = isDirty

        self.isOccupied = isOccupied

        self.X = X

        self.Y = Y

        self.hasCleaned = False


    def CleanUp(self):

        self.isDirty = False    
        self.hasCleaned = True



    def MoveIn(self):

        self.isOccupied = True


    def MoveOut(self):

        self.isOccupied = False

        