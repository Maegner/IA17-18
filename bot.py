from personalUtils import *
from search import *
import copy
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
            if(element == -1 or element == 0):
                col+=1
                continue

            matrixCopy[l][col] = -1
            neighbours = get_neighbours((l,col),matrixCopy,element,[(l,col)])
            if(len(neighbours) > 1):
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
            append(isolatedBallColors,getColorInPosition(matrix,group[0]))
    
    return isolatedBallNumber,isolatedBallColors



def board_remove_group(recievingMatrix, group):

    matrix = copy.deepcopy(recievingMatrix)

<<<<<<< HEAD
def board_remove_group(matrix, group):
    matrixCopy = copy.deepcopy(matrix)
=======
>>>>>>> dd3f284b160b7f2519e67cd63ecc127e3c486b3b
    colunasVazias = []
    linesNumber = len(matrixCopy) 
    columnNumber = len(matrixCopy[0])
    for pos in group:
        posLine =  pos_line(pos)
        posColumn = pos_column(pos)
        color = getColorInPosition(matrixCopy, pos)
        posAbove = get_upper(pos)
        if (posLine > 0 and getColorInPosition(matrixCopy, posAbove) != color):
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

    def __init__(self, board,ballNumber,isolatedBallColor,isolatedBallNumber):
        
        self.isolatedBallColor = isolatedBallColor
        self.isolatedBallNumber = isolatedBallNumber
        self.board = board
        self.numberBalls = len(board)*len(board[0]) 
    
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
    def actions(self, state):
        return board_find_groups(state.board)
    
    def result(self, state, action):
        return sg_state(board_remove_group(state.board, action))


    def goal_test(self, state):
        return state.isEmpty()

    def path_cost(self, c, state1, action, state2):
        return 1 #Duvidas aqui

    #def h(self, node):
       # return 

class same_game(Problem):

    def __init__(self,board):
        self.board = board

a = [[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]] 
initialBoard = sg_state(a)
prob = same_game(initialBoard)
printGame(a)
print("\n")
print(depth_first_tree_search(prob).solution())

