from personalUtils import *
from search import *
import copy


def isTheEnd(matrix):
    
    groups = board_find_groups(matrix)
    if len(groups) == 0:
        print("finished")
        return True 
    return False

def isImpossible(matrix):
    
    groups = board_find_groups(matrix)
    
    if len(groups) == 0:
        return False

    for group in groups:
        if len(group) != 1:
            return False
    return True

def get_neighbours(pos,matrix,element,result):

    # verfies if the element to the top of the refered position is equal to the element
    if pos[0]-1 >= 0 :
        if element == matrix[pos[0]-1][pos[1]]:
        
            nextPos = (pos[0]-1,pos[1])
            matrix[pos[0]-1][pos[1]] = -1
            result.append((pos[0]-1,pos[1]))
            get_neighbours(nextPos,matrix,element,result)

    # verfies if the element to the bottom of the refered position is equal to the element
    if len(matrix) > pos[0]+1:
        if element == matrix[pos[0]+1][pos[1]]:
        
            nextPos = (pos[0]+1,pos[1])
            matrix[pos[0]+1][pos[1]] = -1
            result.append((pos[0]+1,pos[1]))
            get_neighbours(nextPos,matrix,element,result)
     
    # verfies if the element to the right of the refered position is equal to the element
    if len(matrix[pos[0]]) > pos[1]+1:
        if element == matrix[pos[0]][pos[1]+1]:
        
            nextPos = (pos[0],pos[1]+1)
            matrix[pos[0]][pos[1]+1] = -1
            result.append((pos[0],pos[1]+1))
            get_neighbours(nextPos,matrix,element,result)

    
    # verfies if the element to the left of the refered position is equal to the element
    if  pos[1]-1 >= 0:
        if element == matrix[pos[0]][pos[1]-1]:
            nextPos = (pos[0],pos[1]-1)
            matrix[pos[0]][pos[1]-1] = -1
            result.append((pos[0],pos[1]-1))
            get_neighbours(nextPos,matrix,element,result)
    return result

def board_find_groups(matrix):
    matrixCopy = copy.deepcopy(matrix)
    result = []
    l = 0
    col = 0
    for linha in matrixCopy:
        for element in linha:
            if element == -1 or element == 0:
                col+=1
                continue
            matrixCopy[l][col] = -1
            neighbours = get_neighbours((l,col),matrixCopy,element,[(l,col)])
            if(len(neighbours) >= 1):
                result.append(neighbours)
            col+=1
        l+=1
        col = 0
    return result

def findIsolatedBalls(groups,matrix):

    isolatedBallNumber = 0
    isolatedBallColors = []

    for group in groups:
        if len(group) == 1:
            isolatedBallNumber+=1
            isolatedBallColors.append(getColorInPosition(matrix,group[0]))
    
    return isolatedBallNumber,isolatedBallColors

def board_remove_group(matrix, group):

    matrixCopy = copy.deepcopy(matrix)
    colunasVazias = []
    linesNumber = len(matrixCopy) 
    columnNumber = len(matrixCopy[0])

    for pos in group:
        posLine =  pos_line(pos)
        posColumn = pos_column(pos)
        color = getColorInPosition(matrixCopy, pos)
        posAbove = get_upper(pos)
        if (posLine > 0 ):
            propagateFall(matrixCopy, pos)

        else:
            setColorInPosition(matrixCopy,pos,set_no_color())
    for column in range(columnNumber):
        if(matrixCopy[linesNumber-1][column] == 0):
            colunasVazias.append(column)
    for column in colunasVazias[::-1]:
        somatorio = column +1
        while(1):
            if(somatorio > columnNumber-1):
                break
            deslocaTudoEsquerda(matrixCopy,somatorio)
            somatorio +=1
    return matrixCopy

class sg_state():

    def __init__(self, board):
        
        self.groups = board_find_groups(board)
        self.isolatedBallNumber,self.isolatedBallColors = findIsolatedBalls(self.groups,board)
        self.board = board

    def initBalls(self, numberBalls):
        self.numberBalls = numberBalls
    def getIsolatedBallColors(self):
        return self.isolatedBallColors

    def getIsolatedBallNumber(self):
        return self.isolatedBallNumber
    
    def __lt__(self, state):
        return self.numberBalls < state.numberBalls 
    def removeBalls(self, n):
        self.numberBalls -= n
    def getBalls(self):
        return self.numberBalls

    def isEmpty(self):
        for line in self.board:
            for element in line:

                if(has_color(element)):
                    return False
        return True

class same_game(Problem):
    def __init__(self, board):
        self.initial = board
        self.initial.initBalls(len(board.board)*len(board.board[0]))

    def actions(self, state):
        
        action = []

        for group in state.groups:
            if len(group) > 1:
                action.append(group)

        return action
    
    def result(self, state, action):
        newState = sg_state(board_remove_group(state.board, action))
        newState.initBalls(state.getBalls())
        newState.removeBalls(len(action))
        return newState


    def goal_test(self,state):
        return isTheEnd(state.board)

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def h(self,node):
        
        heuristic = 0

        if node.action is None:
            return node.state.numberBalls
        
        
        heuristic = heuristic + node.state.numberBalls

        return heuristic 

a = [[1,1,5,3],[5,3,5,3],[1,2,5,4],[5,2,1,4],[5,3,5,1],[5,3,4,4],[5,5,2,5],[1,1,3,1],[1,2,1,3],[3,3,5,5]]
initialBoard = sg_state(a)
prob = same_game(initialBoard)
#printGame(a)
astar_search(prob)
#print("\n")
#print(depth_first_tree_search(prob).solution())
