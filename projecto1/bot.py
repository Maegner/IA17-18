from search import *
import copy
import time
import resource

#TAI color
#sem cor = 0
#com cor > 0
def set_no_color():
	return 0

def no_color (c):
	return c==0 

def has_color(c):
	return c>0

#TAI pos
#tuplo (l,c)
def pos_line(pos):
	return pos[0]

def pos_column(pos):
	return pos[1]

def get_upper(pos):
	return (pos_line(pos)-1,pos_column(pos))

def get_bottom(pos):
	return (pos_line(pos)+1,pos_column(pos))

def get_left(pos):
	return (pos_line(pos),pos_column(pos)-1)

def get_right(pos):
	return (pos_line(pos),pos_column(pos)+1)

#TAI group
#matriz[[linha],[linha]]

def getColorInPosition(matrix,pos):
	return matrix[pos_line(pos)][pos_column(pos)]

def setColorInPosition(matrix,pos,color):
	matrix[pos_line(pos)][pos_column(pos)] = color


        
        

def printGame(matrix):
	
	for line in matrix:
		
		lineVisual = "| "
		
		for element in line:
			lineVisual+= str(element)
			lineVisual+=" |"
		
		print(lineVisual)

def copyMatrix(matrix, matrixDest):
    for line in range(len(matrix)):
        lineVector = []
        for column in range(len(matrix[0])):
            lineVector.append(matrix[line][column])
        matrixDest.append(lineVector)


def switchPos(matrix, pos1, pos2):
    color1= getColorInPosition(matrix, pos1)
    color2 = getColorInPosition(matrix, pos2)
    setColorInPosition(matrix, pos1, color2)
    setColorInPosition(matrix, pos2, color1)



def propagateFall(matrix):
    numeroColunas = len(matrix[0])
    numerLinhas = len(matrix)
    zerosPositions = []
    zeroIndex = []
    for column in range(numeroColunas):
        zerosPositions.append([])
        zeroIndex.append(0)
    for column in range(numeroColunas):
        for line in range(numerLinhas-1, -1,-1):
            position = (line, column)
            if getColorInPosition(matrix, position) == 0:
                zerosPositions[column].append(position) 
            elif len(zerosPositions[column]) > 0 and zeroIndex[column] < len(zerosPositions[column]):
                switchPos(matrix, zerosPositions[column][zeroIndex[column]], position)
                zerosPositions[column].append(position)
                zeroIndex[column] +=1
    return matrix


def deslocaTudoEsquerda(matrix, column):
	if(column == 0):
		return
	for i in range(len(matrix)):
		pos = (i, column)
		newPos = (i, column-1)
		color = getColorInPosition(matrix, pos) 
		setColorInPosition(matrix,pos,set_no_color())
		setColorInPosition(matrix, newPos, color)
	return matrix


def isTheEnd(state):
    
    groups = state.groups
    if len(groups) == 0:
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
    matrixCopy = []
    copyMatrix(matrix, matrixCopy)
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

def findIsolatedBalls(groups):

    isolatedBallNumber = 0

    for group in groups:
        if len(group) == 1:
            isolatedBallNumber+=1
    
    return isolatedBallNumber


def board_remove_group(matrix, group):
    matrixCopy = []
    copyMatrix(matrix, matrixCopy)
    colunasVazias = []
    linesNumber = len(matrixCopy) 
    columnNumber = len(matrixCopy[0])

    for pos in group:
        setColorInPosition(matrixCopy,pos,set_no_color())
    propagateFall(matrixCopy)
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

def findColorNumber(matrix):
    colors = []
    for line in matrix:
        for element in line:
            if (not element in colors) and element != 0:
                colors.append(element)
    return len(colors)
    
                

class sg_state():

    def __init__(self, board):
        
        self.colorNumber = findColorNumber(board)
        self.groups = board_find_groups(board)
        self.isolatedBallNumber = findIsolatedBalls(self.groups)
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
        try:
            return self.numberBalls
        except:
            balls = 0
            for line in self.board:
                for element in line:
                    if element != 0:
                        balls +=1
            self.numberBalls = balls
            return self.numberBalls

    def isEmpty(self):
        for line in self.board:
            for element in line:

                if(has_color(element)):
                    return False
        return True

class same_game(Problem):
    def __init__(self, board):
        self.initial = sg_state(board)
        self.initial.initBalls(len(self.initial.board)*len(self.initial.board[0]))

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
        return isTheEnd(state)

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def h(self,node):
        
        heuristic = 0

        if node.action is None:
            return node.state.numberBalls
        
        heuristic+=node.state.colorNumber

        heuristic+=node.state.isolatedBallNumber

        #heuristic+=node.state.numberBalls


        return heuristic 