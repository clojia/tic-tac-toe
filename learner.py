from game import Game 

class Learner(object):
    """
    
    Preprocessing: getting training examples from game history

    """
    def __init__(self, hypothesis, mode = 1):
        self.hypothesis = hypothesis
        self.checker = Game()
        self.mode = mode

    def evaluateBoard(self,board):
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = self.checker.getFeatures(board)
        w0, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10 = self.hypothesis
        return w0 + w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5 + w6*x6 + w7*x7 + w8*x8 + w9*x9 + w10*x10

    def setHypothesis(self, hypothesis):
        self.hypothesis = hypothesis

    def getTrainingExamples(self,history):
        trainingExamples = []

        for i in range(0,len(history)):
           if(self.checker.gameOver(history[i])):
               if(self.checker.getWinner(history[i]) == 1):
                   trainingExamples.append([self.checker.getFeatures(history[i]), 100])
               elif(self.checker.getWinner(history[i]) == 0):
                   trainingExamples.append([self.checker.getFeatures(history[i]), 0])
               else:
                   trainingExamples.append([self.checker.getFeatures(history[i]), -100])
           else:
               if i+2 >= len(history):
                   if(self.checker.getWinner(history[len(history)-1]) == 1):
                       trainingExamples.append([self.checker.getFeatures(history[i]), 100])
                   elif(self.checker.getWinner(history[len(history)-1]) == 0): 
                       trainingExamples.append([self.checker.getFeatures(history[i]), 0])
                   else:
                       trainingExamples.append([self.checker.getFeatures(history[i]), -100])
             
               else:   
                   trainingExamples.append([self.checker.getFeatures(history[i]), self.evaluateBoard(history[i+2])])
        return trainingExamples
