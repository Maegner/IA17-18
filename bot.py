from search import *
import copy

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

def propagateFall(matrixPrem,deletedPos):

	matrix = matrixPrem
	numeroColunas = len(matrix[0])

	deletedPosLine = pos_line(deletedPos)
	deletedPosColumn = pos_column(deletedPos)

	setColorInPosition(matrix,deletedPos,0)


	if(deletedPosLine == 0):
		return matrix
	
	else:

		for lineNumber in range(deletedPosLine-1,-1,-1):
			position = (lineNumber,deletedPosColumn)
			newPosition = (lineNumber+1,deletedPosColumn)
			color = getColorInPosition(matrix,position)

			setColorInPosition(matrix,newPosition,color) #drop it down
			setColorInPosition(matrix,position,0)  #empty previous position

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


def isTheEnd(matrix):
    
    groups = board_find_groups(matrix)
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
        if (posLine > 0 and getColorInPosition(matrix, posAbove) != color ):
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
        return isTheEnd(state.board)

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def h(self,node):
        
        heuristic = 0

        if node.action is None:
            return node.state.numberBalls
        
        heuristic+=node.state.isolatedBallNumber

        heuristic+= node.state.numberBalls

        return heuristic 

print(depth_first_tree_search(same_game([[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]])).state.board)
#printGame(a)
#print("\n")
#print(depth_first_tree_search(prob).solution())
