from player import Player
from learner import Learner
from game import Game

class Experience(object):
    """
    Experience mode: teacher or self-learning.
    Default 30 games for training

    """
    def __init__(self,  
            playerX, 
            playerO, 
            learnerX, 
            learnerO,
            epoch = 100,
            sampleFile = "./samples.txt"):
 
        self.playerX = playerX
        self.playerO = playerO 
        self.learnerX = learnerX
        self.learnerO = learnerO
        self.sampleFile = sampleFile
        self.epoch = epoch
        self.xwins = 0
        self.owins = 0
        self.draws = 0


    def selfMode(self):
        while self.playerX.notConverge:
            board = Game()
            self.playerX.setBoard(board)
            self.playerO.setBoard(board)

            while(not board.gameOver()):
                self.playerX.chooseMove()
                if board.gameOver():
                    break     
                self.playerO.randomMove() 
              #  self.playerO.chooseMove()

            self.learnerX.setHypothesis(self.playerX.getHypothesis()) 
            self.playerX.updateWeights(board.getHistory(),self.learnerX.getTrainingExamples(board.getHistory()))          
            self.learnerO.setHypothesis(self.playerO.getHypothesis()) 
            self.playerO.updateWeights(board.getHistory(),self.learnerO.getTrainingExamples(board.getHistory()))          

            winner = board.getWinner()
                
            if(winner == 1):
                print("X wins")
                self.xwins += 1
            elif(winner == -1):
                print("O wins")
                self.owins += 1
            elif(winner == 0):
                print("game is a draw")
                self.draws += 1

        print("xwins: "+ str(self.xwins))
        print("Owins: "+ str(self.owins))
        print("draws: "+ str(self.draws))
        print("learned weights: " + str(self.playerX.getHypothesis())) 

    def teacherMode(self):
        for i in range(0, self.epoch):
            with open(self.sampleFile) as f: 
                for line in f:
                  board = Game()
                  states = []
                  history = line.strip().split(';')
  
                  for samples in history:
                      sample = samples.split(',')
                      states.append([[int(sample[i]), int(sample[i+1]), int(sample[i+2])] for i in range(0, len(sample), 3)])
                  
                  self.learnerX.setHypothesis(self.playerX.getHypothesis())
                  self.playerX.updateWeights(states, self.learnerX.getTrainingExamples(states))  
                  self.learnerO.setHypothesis(self.playerO.getHypothesis()) 
                  self.playerO.updateWeights(states,self.learnerO.getTrainingExamples(states))          

                  
                  winner = board.getWinner(states[-1])
       
                  if(winner == 1):
                      print("X wins")
                      self.xwins += 1
                  elif(winner == -1):
                      print("O wins")
                      self.owins += 1
                  elif(winner == 0):
                      print("game is a draw")
                      self.draws += 1
        
        print("X won " + str(self.xwins) + " games.")
        print("O won " + str(self.owins) + " games.")
        print("There were " + str(self.draws) + " draws.") 
        print("learned weights: " + str(self.playerX.getHypothesis())) 

