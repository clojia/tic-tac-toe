### tic-tac-toe game
### 1 represent X
### -1 represent O
### 0 represent unfilled square

import argparse
import random

from player import Player
from learner import Learner
from game import Game
from experience import Experience

def main():
    parser = argparse.ArgumentParser(description='Tic-Tac-Toe Game.')
    parser.add_argument('-m','--mode', required=False, default='self',
                        choices=['teacher', 'self'], help='experience mode')
    
    args = parser.parse_args() 
 
    print("Experience Mode: " + args.mode)
    
    board = Game()
    hypothesisX = (.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1)
    hypothesisO = (.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1)
   
    playerX = Player(board,hypothesisX,1)
    playerO = Player(board,hypothesisO,-1)
    learnerX = Learner(hypothesisX,1)
    learnerO = Learner(hypothesisO,-1)
    
    sampleFile = "./samples.txt"   
    
    setExperience = Experience(playerX, playerO, learnerX, learnerO)
    if args.mode == "self":
        setExperience.selfMode()
    elif args.mode == "teacher":
        setExperience.teacherMode() 


    xwins = 0
    owins = 0
    draws = 0
    while True:
        board = Game()
        playerX.setBoard(board)
        playerO.setBoard(board)
        
        while(not board.gameOver()):
            playerX.chooseMove()
            board.printBoard()
           
            if board.gameOver():
               break

            xval = int(input("Enter xcoordinate: "))
            yval = int(input("Enter ycoordinate: "))
            
            while xval < 0 or xval > 2 or yval < 0 or yval > 2or board.board[yval][xval]:
                print("Invalid move, please re-try:")
                xval = int(input("Enter xcoordinate: "))
                yval = int(input("Enter ycoordinate: "))
           
            board.setO(xval,yval)
          #  board.printBoard()

        winner = board.getWinner()
            
        if(winner == 1):
            print("X wins")
            xwins += 1
        elif(winner == -1):
            print("O wins")
            owins += 1
        elif(winner == 0):
            print("game is a draw")
            draws += 1


        print("X won " + str(xwins) + " games.")
        print("O won " + str(owins) + " games.")
        print("There were " + str(draws) + " draws.") 
        print("Winning rate of X is  " + str(xwins/(draws+xwins+owins)) + ".")  
       
        learnerX.setHypothesis(playerX.getHypothesis())
        
        playerX.updateWeights(board.getHistory(), learnerX.getTrainingExamples(board.getHistory())) 
  
if __name__ == '__main__':
    main()
