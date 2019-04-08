import copy

class Game(object):
    """
    Game basic elements: 
    generating board, 
    recordig checker movements and successors, 
    deciding winner, 
    generating features and history as raw data.

    """
    def __init__(self):
        self.board = self.generateBoard()
        self.history = [copy.deepcopy(self.board)]
    
    def setBoard(self,board):
        if board == 0:
            print("zero board")
        self.board = board
        self.history.append(copy.deepcopy(self.board))

    def generateBoard(self):
        board = [[0,0,0],
                 [0,0,0],
                 [0,0,0]]
        return board

    def getEntries(self, board = 0): # winning states: 3 rows + 3 columns + 2 diagonals
        if board == 0:
            board = self.board
        entries = [
                [board[0][0], board[0][1], board[0][2]],
                [board[1][0], board[1][1], board[1][2]],
                [board[2][0], board[2][1], board[2][2]],
                [board[0][0], board[1][0], board[2][0]],
                [board[0][1], board[1][1], board[2][1]],
                [board[0][2], board[1][2], board[2][2]],
                [board[0][0], board[1][1], board[2][2]],
                [board[2][0], board[1][1], board[0][2]]]
        return entries
        
    def getWinner(self, board = 0):
        if board == 0:
            board = self.board

        if [1, 1, 1] in self.getEntries(board): 
            return 1 # 1 represents an X, program 
        elif [-1, -1, -1] in self.getEntries(board):
            return -1 # -1 represents an O, opponent
        else:
            return 0

    def gameOver(self, board = 0):
        if board == 0:
            board = self.board
        if self.getWinner(board):
            return True
        for y in range(0,3):
            for x in range(0,3):
                if board[y][x] == 0:
                    return False
        return True

    def getFeatures(self, board = 0):
        if board == 0:
            board = self.board
        x1 = 0 # numbers of 2 consecutive x's in a line with an open cell. e.g. _ X X
        x2 = 0 # numbers of 2 consecutive o's in a line with an open cell. e.g. _ O O
        x3 = 0 # numbers of 2 x's in a line with an open cell in middle. e.g. X _ X
        x4 = 0 # numbers of 2 o's in a line with an open cell in middle. e.g. O _ O
        x5 = 0 # numbers of 1 x in the middle of an open line. e.g. _ X _
        x6 = 0 # numbers of 1 o in the middle of an open line. e.g. _ O _
        x7 = 0 # number of 1 x in the edge of an open line. e.g. X _ _
        x8 = 0 # number of 1 o in the edge of an open line. e.g. O _ _
        x9 = 0
        x10 = 0

        for entry in self.getEntries(board):
            if (entry == [1, 1, 0]) or (entry == [0, 1, 1]):
                x1 += 1
            elif (entry == [-1, -1, 0]) or (entry == [0, -1, -1]):
                x2 += 1
            elif entry == [1, 0, 1]:
                x3 += 1
            elif entry == [-1, 0, -1]:
                x4 += 1
            elif entry == [0, 1, 0]:
                x5 += 1
            elif entry == [0, -1, 0]:
                x6 += 1
            elif (entry == [1, 0, 0]) or (entry == [0, 0, 1]):
                x7 += 1
            elif (entry == [-1, 0, 0]) or (entry == [0, 0, -1]):
                x8 += 1
            elif (entry == [1, 1, 1]):
                x9 += 1
            elif (entry == [-1, -1, -1]):
                x10 += 1

        return x1,x2,x3,x4,x5,x6,x7,x8,x9,x10

    def getSuccessorsX(self):
        successors = []
        for y in range(0, 3):
            for x in range(0, 3):
                if self.board[y][x] == 0:
                    successor = copy.deepcopy(self.board)
                    successor[y][x] = 1
                    successors.append(successor)
        return successors
    
    def getSuccessorsO(self):
        successors = []
        for y in range(0, 3):
            for x in range(0, 3):
                if self.board[y][x] == 0:
                    successor = copy.deepcopy(self.board)
                    successor[y][x] = -1
                    successors.append(successor)
        return successors

    def getHistory(self):
        return self.history

    def setX(self, x, y):
        if self.board[y][x] == 0:
            self.board[y][x] = 1
            self.history.append(copy.deepcopy(self.board))
          

    def setO(self, x, y):
        if self.board[y][x] == 0:
            self.board[y][x] = -1

    def printBoard(self, board = 0):
        if board == 0:
            board = self.board 
        for row in board:
            print("\n---------------")
            for cell in row:
                if cell == 1:
                    print("| X |", end='')
                elif cell == -1:
                    print("| O |", end='')
                else:
                    print("|   |", end='')
        print("\n---------------")
                   
