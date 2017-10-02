
def get_neighbours(pos,matrix,element,result):
     
    # verfies if the element to the right of the refered position is equal to the element
    if len(matrix[pos[0]]) > pos[1]+1:

        print(pos[0])
        
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

s = get_neighbours((0,0),[[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]],2,[(0,1)])
print(s)      