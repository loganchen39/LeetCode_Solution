# Algo. 1
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        : Do not return anything, modify board in-place instead.
        
        : type board: List[List[int]]
        : rtype: None
        
        : TC: 64.47%, O(m*n), need to check each element of the matrix individually, right?
        : SC: 10%, O((m+2)*(n+2)), allocated an new matrix bd, with extra 2 new rows and columns to surround the boundary. 
        :\Algo. 1 BF from Ligang, similar as Solu 1, use an auiliary matrix bd[m+2][n+2], with 2 extra rows and columns surrounding 
        : boundaries with value of 0, so when checking each element especially the boundary elements, the calculation 
        : becomes uniform, no need to differentiate boundary elements, which could be very redundant. 
        :\Another important lesson learned is about python list/array assignment programming tricks, especially for 2D or 
        : above! See comments and code below. 
        """
        if not board or not board[0]: return
        
        m, n = len(board), len(board[0])
        
        bd = [[0]*(n+2) for _ in range(m+2)]
        #bd = [[0 for _ in range(n+2)] for _ in range(m+2)]
        #print(board)
        # WRONG!! You can NOT assign 2D (or above) list like this. The reason might be in <<Fluent Python>> p. 38.
        # The built-in sequence types in Python are one-dimentional, so they support only one index or slice, and 
        # not a tuple of them.?
        #bd[1:m+1][1:n+1] = board[0:m][0:n]  
        #for i in range(m):
        #    for j in range(n):
        #        bd[i+1][j+1] = board[i][j]
        
        for i in range(m):
            # 1D assignment ok, but NOT like bd[1:m+1][j+1] = board[:][j]!!
            bd[i+1][1:n+1] = board[i][:]  
                
        print(bd)
        
        #bd[0][:]   = [0]*(n+2)  # should work;
        #bd[m+1][:] = [0]*(n+2)
        #bd[:][0]   = [0]*(m+2)  # should NOT work;
        #bd[:][n+1] = [0]*(m+2)
        
        for i in range(m):
            for j in range(n):
                # NOT work! same as x = bd[i:i+3], contains whole line, no limit as [j:j+3]!
                #x = bd[i:i+3][j:j+3]
                #x = []
                #print("i = " + str(i) + ", j = " + str(j) + ", x = ")
                #print(x)
                #break
                
                x = []
                for k in range(i, i+3):
                    y = bd[k][j:j+3]  # 1D assignment like this seems ok!
                    x.append(y)  # make sure every element of x is an independent element. 
                    
                #print("i = " + str(i) + ", j = " + str(j) + ", x = ")
                #print(x)
                
                
                n_live = sum([sum(y) for y in x]) - bd[i+1][j+1]
                #if bd[i+1][j]   == 1: n_live += 1
                #if bd[i+1][j+2] == 1: n_live += 1
                #if bd[i][j+1]   == 1: n_live += 1
                #if bd[i+2][j+1] == 1: n_live += 1
                #if bd[i][j]     == 1: n_live += 1
                #if bd[i][j+2]   == 1: n_live += 1
                #if bd[i+2][j]   == 1: n_live += 1
                #if bd[i+2][j+2] == 1: n_live += 1
                
                print("i = " + str(i) + ", j = " + str(j) + ", n_live = " + str(n_live))
                
                if board[i][j] == 0 and n_live == 3: board[i][j] = 1
                if board[i][j] == 1:
                    if n_live <= 1 or n_live >= 4: 
                        board[i][j] = 0
        
        return




# Algo. 2
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        : Do not return anything, modify board in-place instead.
        
        : type board: List[List[int]]
        : rtype: None
        
        : TC: 64.47%, O(m*n), need to check each element of the matrix individually
        : SC: 10%, O(m*n), allocated an new matrix bd, with extra 2 new rows and columns to surround the boundary. 
        :\Algo. 2 Solu 1 similar to Algo. 1, use an auiliary matrix copy_board initialized as board,  
        """
        if not board or not board[0]: return
        rows, cols = len(board), len(board[0])
        
        # Neighbors array to find 8 neighboring cells for a given cell
        #neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]  # more understandable
        
        # Create a copy of the original board
        # if you use: copy_board = board, or copy_board = board[:][:], or even copy_board = board.copy()??, 
        # then copy_board is just a ref point to board, it would be WRONG! For 2D (or above) array
        # below is an actual copy, the only way to do this? 
        # However for 1D list, you can use copy_board = board[:] or board.copy() to create a real copy! 
        # but not copy_board = board, it would still be a ref to board!
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        # Iterate through board cell by cell.
        for row in range(rows):
            for col in range(cols):
                # For each cell count the number of live neighbors.
                live_neighbors = 0
                for neighbor in neighbors:
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])
                    # Check the validity of the neighboring cell and if it was originally a live cell.
                    # The evaluation is done against the copy, since that is never updated.
                    # Here no need for an extra 2 rows and columns of 0 value elements, use "neighbors"
                    # and "if" conditions to automatically check the valid elements!
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (copy_board[r][c] == 1):
                        live_neighbors += 1

                # Rule 1 or Rule 3        
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                # Rule 4
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1


