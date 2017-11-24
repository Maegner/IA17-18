from bot import *
from search import *
from personalUtils import *

class sg_state(): 

    def __init__(self, board,ballNumber,isolatedBallColor,isolatedBallNumber):
        
        self.isolatedBallColor = isolatedBallColor
        self.isolatedBallNumber = isolatedBallNumber
        self.board = board
        self.numberBalls = len(board)*len(board[0]) 
    
    def __lt__(self, state):
        return self.numberBalls < state.numberBalls 

def isTheEnd(matrix):
    
    groups = board_find_groups(matrix)

    if len(group) == 0:
        return true

    for group in groups:
        if len(group) != 0:
            return false    
    return true

class same_game(Problem):
    
    def __init__(self,board):
        self.initial = board

    def actions(self, state):
        return state.groups
    
    def result(self, state, action):
        
        printGame(state.board)
        state = sg_state(board_remove_group(state.board, action))
        state.removeBalls(len(action))
        return state
    
    def goal_test(self,state):
        return isTheEnd(state.board)

    def path_cost(self, c, state1, action, state2):
        return c + 1
    
    def h(self,node):
        
        heuristic = 0

        if getColorInPosition(node.action[0]) in node.state.isolatedBallColors:
            heuristic += 1000000000000
        
        heuristic += (node.state.numberBalls - len(action))

        heuristic += node.state.isolatedBallNumber
        
        return heuristic