def create_screen(rows, columns):
    '''
    Creates a screen of rows x columns pixels
    '''
    grid = []
    for row in range(rows):
        grid.append([0] * columns)
    return grid

def print_screen(screen):
    ''' Prints the screen to the console.
        When a pixel == 0, then a '*' is displayed
        When a pixel == 1, then a ' ' is displayed
    '''
    for row in range(len(screen)):
        for col in range(len(screen[0])):
            if screen[row][col] == 0:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    return

def doSomething(screen,x):

    for i in range(len(screen)):
        screen[i][x]=1

    return screen

def somethingElse(screen,x):
    for i in range(len(screen[0])):
        screen[x][i]=1


def drawThing(screen,ulrow,ulcol,lrrow,lrcol):

    for col in range(ulcol,lrcol+1):
        screen[ulrow][col]=1

    middleCol = (ulcol + lrcol)//2

    for row in range(ulrow,lrrow+1):
        screen[row][middleCol]=1

    return screen
        
def drawOtherThing(screen,ulrow,ulcol,lrrow,lrcol):

    for r in range(ulrow,lrrow+1):
        screen[r][ulcol]=1
    for r in range(ulrow,lrrow+1):
        screen[r][lrcol]=1
    for c in range(ulcol,lrcol+1):
        screen[ulrow][c]=1

    return screen

def drawReverseThing(screen,ulrow,ulcol,lrrow,lrcol):

    for r in range(ulrow,lrrow+1):
        screen[r][ulcol]=1
    for r in range(ulrow,lrrow+1):
        screen[r][lrcol]=1
    for c in range(ulcol,lrcol+1):
        screen[lrrow][c]=1

    return screen


def foo():
    s = create_screen(8,9)
    print_screen(doSomething(s,4))

def bar():
    s = create_screen(8,9)
    print_screen(somethingElse(s,4))

def baz():
    s = create_screen(8,9)
    somethingElse(s,4)
    print_screen(s)             
    
def gaucho():
    s = create_screen(8,9)
    print_screen(drawThing(s,1,2,6,5))
    
def isla():
    s = create_screen(8,9)
    print_screen(drawOtherThing(s,2,3,5,7))

def vista():
    s = create_screen(8,9)
    print_screen(drawReverseThing(s,2,3,5,7))

    
s1 = [ [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
	   [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],       
           [0,0,0,0,0,0,0,0] ]

        
s2     = [ [0,0,0,0,0,0,0,0],
           [0,1,1,1,1,0,0,0],
	   [0,1,0,0,1,0,0,0],
	   [0,1,0,0,1,0,0,0],           
           [0,1,1,1,1,0,0,0],
           [0,0,0,0,0,0,0,0] ]
        

def draw_line(row1,col1,row2,col2,screen):
    if row1 != row2 and col1 != col2:
        slope = (col2-col1)/(row2-row1)
        for x in range(min(row1,row2),max(row1,row2)+1):
            y = round(slope*(x-row1)+col1)
            screen[x][y] = 1
        for y in range(min(col1,col2),max(col1,col2)+1):
            x = round(((y-col1)/slope)+row1)
            screen[x][y] = 1
    elif row1 == row2 and col1 == col2:
        screen[row1][row2] = 1
    elif row1 == row2 and col1 != col2:
        for y in range(col1,col2+1):
            screen[row1][y] = 1
    elif row1 != row2 and col1 == col2:
        for x in range(row1,row2+1):
            screen[x][col1] = 1
    return screen

def distractor():
    s = create_screen(8,9)
    print_screen(draw_line(2,3,5,7,s))
