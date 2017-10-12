from personalUtils import *
from search import *
import copy
def get_neighbours(pos,matrix,element,result):
     
    # verfies if the element to the right of the refered position is equal to the element
    if len(matrix[pos[0]]) > pos[1]+1:
        if element == matrix[pos[0]][pos[1]+1]:
        
            nextPos = (pos[0],pos[1]+1)
            matrix[pos[0]][pos[1]+1] = -1
            result.append((pos[0],pos[1]+1))
            get_neighbours(nextPos,matrix,element,result)

    
    # verfies if the element to the left of the refered position is equal to the element
    if pos[1]-1 >= 0:
        if element == matrix[pos[0]][pos[1]-1]:
            nextPos = (pos[0],pos[1]-1)
            matrix[pos[0]][pos[1]-1] = -1
            result.append((pos[0],pos[1]-1))
            get_neighbours(nextPos,matrix,element,result)

    # verfies if the element to the bottom of the refered position is equal to the element
    if len(matrix) > pos[0]+1:
        if element == matrix[pos[0]+1][pos[1]]:
        
            nextPos = (pos[0]+1,pos[1])
            matrix[pos[0]+1][pos[1]] = -1
            result.append((pos[0]+1,pos[1]))
            get_neighbours(nextPos,matrix,element,result)

    # verfies if the element to the top of the refered position is equal to the element
    if pos[0]-1 >= 0:
        if element == matrix[pos[0]-1][pos[1]]:
            nextPos = (pos[0]-1,pos[1])
            matrix[pos[0]-1][pos[1]] = -1
            result.append((pos[0]-1,pos[1]))
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


def board_remove_group(matrix, group):
    colunasVazias = []
    linesNumber = len(matrix) 
    columnNumber = len(matrix[0])
    for pos in group:
        posLine =  pos_line(pos)
        posColumn = pos_column(pos)
        color = getColorInPosition(matrix, pos)
        posAbove = get_upper(pos)
        if (posLine > 0 and getColorInPosition(matrix, posAbove) != color):
            propagateFall(matrix, pos)

        else:
            setColorInPosition(matrix,pos,set_no_color())
    for column in range(columnNumber):
        if(matrix[linesNumber-1][column] == 0):
            colunasVazias.append(column)
    for column in colunasVazias[::-1]:
        somatorio = column +1
        while(1):
            if(somatorio > columnNumber-1):
                break
            deslocaTudoEsquerda(matrix,somatorio)
            somatorio +=1
    return matrix

class sg_state():
    def __init__(self, board):
        self.board = board
        self.numberBalls = len(board)*len(board[0])
    def __lt__(self, state):
        return self.numberBalls < state.numberBalls 
    def removeBalls(self, n):
        self.numberBalls -= n
    def getBalls(self):
        return self.numberBalls

    def isEmpty(self):
        return self.numberBalls == 0

class same_game(Problem):
    def actions(self, state):
        return board_find_groups(state.board)
    
    def result(self, state, action):
        print("initialState\n")
        printGame(state.board)
        print("action\n")
        print(action)
        state = sg_state(board_remove_group(state.board, action))
        state.removeBalls(len(action))
        printGame(state.board)
        print("\n")
        return state

    def goal_test(self, state):
        return state.isEmpty()

    def path_cost(self, c, state1, action, state2):
        return 1 #Duvidas aqui

    #def h(self, node):
       # return 


a = [[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]] 
initialBoard = sg_state(a)
prob = same_game(initialBoard)
printGame(a)
print("\n")
print(depth_first_tree_search(prob))