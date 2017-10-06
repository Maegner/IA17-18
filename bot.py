
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

s = board_find_groups([[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]])

print(s)