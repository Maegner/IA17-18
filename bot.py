from personalUtils import *
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
    if len(matrix[pos[0]]) > pos[1]-1:
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
    if len(matrix) < pos[0]-1:
        if element == matrix[pos[0]-1][pos[1]]:
        
            nextPos = (pos[0]-1,pos[1])
            matrix[pos[0]-1][pos[1]] = -1
            result.append((pos[0]-1,pos[1]))
            get_neighbours(nextPos,matrix,element,result)
    else:
        return result

def board_find_groups(matrix):
    result = []
    l = 0
    col = 0
    for linha in matrix:
        for element in linha:
            if(element == -1):
                col+=1
                continue

            matrix[l][col] = -1

            result.append(get_neighbours((l,col),matrix,element,[(l,col)]))
            col+=1
        l+=1
        col = 0
    return result


def board_remove_group(matrix, group):
    colunasVazias = []
    linesNumber = len(matrix[0]) -1
    columnNumber = len(matrix)-1
    for pos in group:
        posLine =  pos_line(pos)
        posColumn = pos_column(pos)
        color = getColorInPosition(matrix, pos)
        posAbove = get_upper(pos)

        if (posLine == linesNumber and no_color(getColorInPosition(matrix, posAbove))):
            colunasVazias.append(posColumn)

        if (posLine > 0 and getColorInPosition(matrix, posAbove) != color):
            propagateFall(matrix, pos)

        else:
            setColorInPosition(matrix,pos,set_no_color())
    for column in colunasVazias:
        somatorio = column +1
        while(1):
            if(somatorio > columnNumber):
                break
            deslocaTudoEsquerda(matrix,somatorio)
            somatorio +=1
    return matrix

testMatrix = [[0,0,0,0],[0,2,3,3],[1,2,1,3],[2,2,2,2]]
matrix = copy.deepcopy(testMatrix)
printGame(testMatrix)
print("\n")
test = board_find_groups(matrix)
printGame(board_remove_group(testMatrix, test[1]))
