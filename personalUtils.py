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
		print("deleted from top line")
		return matrix
	
	else:

		for lineNumber in range(deletedPosLine-1,-1,-1):
			position = (lineNumber,deletedPosColumn)
			newPosition = (lineNumber+1,deletedPosColumn)
			color = getColorInPosition(matrix,position)

			setColorInPosition(matrix,newPosition,color) #drop it down
			setColorInPosition(matrix,position,0)  #empty previous position


	#printGame(matrix)
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