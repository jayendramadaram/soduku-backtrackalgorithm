import numpy as np



import numpy as np
given_puzzle = [[8, 1, 0, 0, 3, 0, 0, 2, 7], 
                [0, 6, 2, 0, 5, 0, 0, 9, 0], 
                [0, 7, 0, 0, 0, 0, 0, 0, 0], 
                [0, 9, 0, 6, 0, 0, 1, 0, 0], 
                [1, 0, 0, 0, 2, 0, 0, 0, 4], 
                [0, 0, 8, 0, 0, 5, 0, 7, 0], 
                [0, 0, 0, 0, 0, 0, 0, 8, 0], 
                [0, 2, 0, 0, 1, 0, 7, 5, 0], 
                [3, 8, 0, 0, 7, 0, 0, 4, 0]]

def check(row, col, num,given_puzzle):

    
    for i in range(9):
        if given_puzzle[row][i] == num:
            return False

        
    for i in range(9):
        if given_puzzle[i][col] == num:
            return False

        
    x = col // 3
    y = row // 3
    for i in range(3):
        for j in range(3):
            if given_puzzle[y*3+i][x*3+j] == num:
                return False

    return True
lis=[0,1,2,3,4,5,6,7,8,9]
def start_backtrack(given_puzzle):
    global lis
    for row in range(len(given_puzzle)):
        for col in range(len(given_puzzle[row])):
            if given_puzzle[row][col] == 0:
                for num in lis:
                    if check(row, col, num,given_puzzle):
                        print(np.array(given_puzzle))
                        given_puzzle[row][col] = num
                        start_backtrack(given_puzzle)
                        given_puzzle[row][col] = 0
                
                return False
        
    print(np.array(given_puzzle))         
    quit()
    

start_backtrack(given_puzzle)






























'''
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]

def possible(row, column, number):
    global grid
    #Is the number appearing in the given row?
    for i in range(0,9):
        if grid[row][i] == number:
            return False

    #Is the number appearing in the given column?
    for i in range(0,9):
        if grid[i][column] == number:
            return False
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False
    

    return True
lis=[]
def solve():
    global grid
    global lis
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0

                
      
    lis.append(np.matrix(grid))
    print(lis)

jay = solve()
print(jay)









'''





'''import numpy as np

grid = [[7,8,0,4,0,0,1,2,0],
         [6,0,0,0,7,5,0,0,9],
         [0,0,0,6,0,1,0,7,8],
         [0,0,7,0,4,0,2,6,0],
         [0,0,1,0,5,0,9,3,0],
         [9,0,4,0,6,0,0,0,5],
         [0,7,0,3,0,0,0,1,2],
         [1,2,0,0,0,7,4,0,0],
         [0,4,9,2,0,6,0,0,7]]
    
import numpy as np

def possible(row, column, number):
    global grid
    for i in range(0,9):
        if grid[row][i] == number:
            return False


    for i in range(0,9):
        if grid[i][column] == number:
            return False
    
    return True

def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0

                
      
    return grid

jay=solve()
print(np.array(jay))










'''




'''
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]
'''








'''


def solve(bo):
    find = find_empty(bo)
    print(find)
    if not find:
        print(True)
        return True
    
    
    else:
        row, col = find
    a=backtrack(bo,row,col)
    print(a)
    return a

    


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    

    return True





def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    #return None






def backtrack(bo,row,col):
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            print(bo[row][col])
            print(np.array(bo))

            if solve(bo):
                return True

            bo[row][col] = 0

    return False



solve(board)
jay=np.array(board)
print(jay)
'''


