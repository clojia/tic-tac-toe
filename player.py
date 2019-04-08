import random
from game import Game

class Player(object):
    """
    LMS weight update, deciding moves

    """

    def __init__(self, board, hypothesis, mode = 1, learningRate=.1):
        self.board = board
        self.hypothesis = hypothesis
        self.history = []
        self.learningRate = learningRate
        self.mode = mode
        self.stableWeights = 0
        self.notConverge = True 

    def evaluateBoard(self, board):
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = self.board.getFeatures(board)
        w0, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10 = self.hypothesis
        return w0 + w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5 + w6*x6 + w7*x7 + w8*x8 + w9*x9 + w10*x10

    def setBoard(self, board):
        self.board = board

    def getBoard(self):
        return self.board

    def setHypothesis(self, hypothesis):
        self.hypothesis = hypothesis

    def getHypothesis(self):
        return self.hypothesis

    def randomMove(self):
        if self.mode == 1:
            successors = self.board.getSuccessorsX()
        else:
            successors = self.board.getSuccessorsO()
 
        randomBoard = successors[random.randint(0, len(successors)-1)]
    
        self.board.setBoard(randomBoard)

    def chooseMove(self):
        if self.mode == 1:
            successors = self.board.getSuccessorsX()
        else:
            successors = self.board.getSuccessorsO()
   
        bestSuccessor = successors[0] 
        bestValue = self.evaluateBoard(bestSuccessor)
        for successor in successors:
            value = self.evaluateBoard(successor)
            if value > bestValue:
                bestValue = value
                bestSuccessor = successor

        self.board.setBoard(bestSuccessor)

    def updateWeights(self, history, trainingExamples):
        for i in range(0, len(history)):
            w0, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10 = self.hypothesis 
            vEst = self.evaluateBoard(history[i])
            x1,x2,x3,x4,x5,x6,x7,x8,x9,x10 = trainingExamples[i][0]
            vTrain = trainingExamples[i][1]            

            w0 = w0 + self.learningRate*(vTrain - vEst)
            w1 = w1 + self.learningRate*(vTrain - vEst)*x1
            w2 = w2 + self.learningRate*(vTrain - vEst)*x2
            w3 = w3 + self.learningRate*(vTrain - vEst)*x3
            w4 = w4 + self.learningRate*(vTrain - vEst)*x4
            w5 = w5 + self.learningRate*(vTrain - vEst)*x5
            w6 = w6 + self.learningRate*(vTrain - vEst)*x6
            w7 = w7 + self.learningRate*(vTrain - vEst)*x7
            w8 = w8 + self.learningRate*(vTrain - vEst)*x8
            w9 = w9 + self.learningRate*(vTrain - vEst)*x9
            w10 = w10 + self.learningRate*(vTrain - vEst)*x10
            if 0 < abs(vTrain - vEst) < 0.01: 
                self.stableWeights += 1
            if self.stableWeights >= 100:
                self.notConverge = False
            self.hypothesis = w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10
