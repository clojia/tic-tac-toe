########## FILES ##########
- tic_tac_toe.py 
main function: set initial weights, run testing and output winning rate

- experience.py:
Experience class: select experience mode (teacher/self)

- learner.py:
Learner class: generate training examples from game history

- player.py:
Player class: update weights, decide moves, append states to game history

- game.py:
Game class: allow moves, output win/lose/tie, generate features, decide winner, draw board

- samples.txt:
training data for teacher mode (win:lose:tie = 1:1:1). Data looks like:
"""
0,0,0,0,0,0,0,0,0;0,0,0,0,1,0,0,0,0;0,0,0,-1,1,0,0,0,0;0,0,0,-1,1,1,0,0,0;0,-1,0,-1,1,1,0,0,0;0,-1,0,-1,1,1,0,1,0;0,-1,0,-1,1,1,-1,1,0;1,-1,0,-1,1,1,-1,1,0;1,-1,0,-1,1,1,-1,1,-1;1,-1,1,-1,1,1,-1,1,-1
"""
one row representing one game history, every six digits represent one state. 1 represent an X, -1 represent  an O, 0 represent an unfilled square


########### USAGE ##########
python3 tic_tac_toe.py -m <mode> *please note python3 instead of python
e.g.
"""
python3 tic_tac_toe.py [-m self]
"""
(self mode: train from 30 games generated by the program)
"""
python3 tic_tac_toe.py -m teacher 
"""
(teacher mode: train from 30 games in samples.txt)


