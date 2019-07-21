# Algo. 1.
from collections import deque
class Solution:
    def numIslands(self, grid):
        """
        : type grid: List[List[str]]
        : rtype: int   
        
        : TC: faster than 6.07%
        : SC: less than 20.19%
        :\1. BF algo., 2-while-loop + BFS + Deque as queue + visited mark: 2-while-loop (or for-loop) to loop 
        : each element [i, j] of '1', use BFS to search and MARK all the adjacent grid of '1' to form an island. 
        : The TC (6.07%) is O(m*n), and SC (20.19%) is O(m*n), not good;
        :\Checked the LC Approach #2, Space complexity : O(min(M, N)) because in worst case where the grid is 
        : filled with lands, the size of queue can grow up to min(M,N). ?? 
        : Also in stead of allocating O(mxn) visited array, you can set the grid[i][j] from '1' to '0' as mark.
        """

        m= len(grid)
        if m == 0: return 0
        # Can not assign like this: m, n = len(grid), len(grid[0]), ERROR for grid=[]
        n = len(grid[0])   
        if n == 0: return 0
        
        n_res = 0
        visited = [[False]*n for i in range(m)]  # mxn matrix
        # visited = [[False]*n for i in range(m)], wrong, it becomes visited = [0, 0, 0, 0], as False*5=0;
        # It would be not efficient to use List as a queue, particularly for list.pop(0) operation with large dataset.
        queue = deque()  
        
        # i, j = 0, 0; wrong! the 'j = 0' should be inside of 'while i < m', better to use 2 for-loops; 
        i = 0
        while i < m:
            j = 0
            while j < n:
                if grid[i][j] == '1':
                    if visited[i][j]:
                        pass
                    else:
                        visited[i][j] = True
                        queue.append([i, j])
                        
                        while queue:
                            k, l = queue.popleft()
                            
                            if l+1 <= n-1 and grid[k][l+1] == '1' and not visited[k][l+1]:
                                visited[k][l+1] = True
                                queue.append([k, l+1])
                            if l-1 >= 0 and grid[k][l-1] == '1' and not visited[k][l-1]:
                                visited[k][l-1] = True
                                queue.append([k, l-1])
                            if k+1 <= m-1 and grid[k+1][l] == '1' and not visited[k+1][l]:
                                visited[k+1][l] = True
                                queue.append([k+1, l])
                            if k-1 >= 0 and grid[k-1][l] == '1' and not visited[k-1][l]:
                                visited[k-1][l] = True
                                queue.append([k-1, l])
                        else:  # queue empty;
                            n_res += 1
                j += 1  # In whatever case, i, j do NOT change in the above code, and will loop ove each element.
            i = i + 1
        
        return n_res




# Algo. 2
class Solution:
    def numIslands(self, grid):
        """
        : type grid: List[List[str]]
        : rtype: int   
        
        : TC: 5.21%
        : SC: 19.53%
        : \1. BF algo., 2-for-loop + DFS to set visited mark which is the key: 2-for-loop to loop 
        : each element [i, j] of '1', use DFS to search and MARK all the adjacent grid of '1' to form an island. 
        : The TC is O(m*n)? and SC is O(m*n), not good;
        : \1. The 2D array grid is a 'structured' graph, the adjacent elements can be found and constructed by indexing, 
        : so you don't actually need an adjacency list/Matrices to represent the 'graph'.
        :\Checked the LC Approach #1, in stead of allocating O(mxn) visited array, you can set the grid[i][j] from '1' to '0'
        : as mark. Then the DFS SC worst case is O(mxn) when the grid map is fill with lands where DFS goes by mxn deep.
        """

        m= len(grid)
        if m == 0: return 0
        n = len(grid[0])   
        if n == 0: return 0
        
        n_res = 0
        visited = [[False]*n for i in range(m)] 
        
        def dfs_search(grid, idx, visited):
            # if grid[idx[0]][idx[1]] == '0' or visited[idx[0]][idx[1]]: return  # better not to have this statement
            # Let's be firmly identical and consistent, the visited[idx[0]][idx[1]] is always False;
            # and you set it as True here inside the dfs_search function!
            visited[idx[0]][idx[1]] = True
            
            adj_idx = []
            if idx[1]-1 >= 0   and grid[idx[0]][idx[1]-1] == '1' and not visited[idx[0]][idx[1]-1]: adj_idx.append([idx[0], idx[1]-1])
            if idx[1]+1 <= n-1 and grid[idx[0]][idx[1]+1] == '1' and not visited[idx[0]][idx[1]+1]: adj_idx.append([idx[0], idx[1]+1])
            if idx[0]-1 >= 0   and grid[idx[0]-1][idx[1]] == '1' and not visited[idx[0]-1][idx[1]]: adj_idx.append([idx[0]-1, idx[1]])
            if idx[0]+1 <= m-1 and grid[idx[0]+1][idx[1]] == '1' and not visited[idx[0]+1][idx[1]]: adj_idx.append([idx[0]+1, idx[1]])
            
            for i in range(len(adj_idx)):
                # visited[adj_idx[i][0]][adj_idx[i][1]] = True, do NOT set it True here!
                dfs_search(grid, adj_idx[i], visited)
                
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs_search(grid, [i, j], visited)
                    n_res += 1
        
        return n_res




# Algo. 3, Union Find; 
class UnionFind():
    def __init__(self, grid):
        # A lot can be learned about python programming from this code!
        nr, nc = len(grid), len(grid[0])
        self.parent = [i  for i in range(nr*nc)]
        self.rank   = [0]*(nr*nc)
        self.count  = sum(grid[i][j] == '1' for i in range(nr)  for j in range(nc))
                
    def find(self, idx):
        # The following code segment of iteration also works;
        # But it does NOT set "self.parent[idx] = self.find(self.parent[idx])" like the recursive algo. does  
        # which is actually the pass-compression algo. to improve the TC. 
        #while self.parent[idx] != idx:
        #    idx = self.parent[idx]
        #return self.parent[idx]
        
        if self.parent[idx] != idx: 
            # The following code line does NOT work, have to use self.find, or ERROR of "'find' not defined"!
            # self.parent[idx] = find(self, self.parent[idx])
            
            # have to use self.parent[idx], not just parent!
            # pass-compression algo. to improve the TC, Ref. p508 <<Intro. To Algo.>>.
            self.parent[idx] = self.find(self.parent[idx])  
        return self.parent[idx]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        # Union by rank
        # With this union by rank algo., do all the final unions have maximum rank of 1? i.e. 
        # one root, with all leafs directly point to it? Then there's no need for pass-compression? 
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]: 
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx]  += 1
            
            self.count -= 1
    
    
class Solution:
    def numIslands(self, grid):
        """
        : type grid: List[List[str]]
        : rtype: int   
        
        : TC: 5.22%
        : SC: 15.50%
        :\1. Union find (i.e. Disjoint set) algo., a good ref. is <<Intro. To Algo.>>. 
        : It usually starts with individual element as initial set, and then union (combine) them according
        : adjacency relationships. You can use linked list or tree (forest) to implement the algo. But here 
        : can simply use self.parent[idx] to store (point to) the parent ID. Each element is index-based
        : within [0..nr*nc], and you also use self.rank[idx] to store the rank of each element. 
        :\Each set has a representative which is usually the root, each set has a tree structure, all the 
        : disjoint sets are the forest structure.
        :\The TC is O(nr*nc), Note that Union operation takes essentially constant time when UnionFind is 
        : implemented with both path compression and union by rank.
        """

        nr = len(grid)
        if nr == 0: return 0
        nc = len(grid[0])   
        if nc == 0: return 0
        
        n_res = 0
        uf = UnionFind(grid)
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    grid[r][c] == '0'
                    # Within the following 'if' statement, you can NOT set like grid[r-1][c]='0' yet, 
                    # or it will not extend to adjacent elements of '1's.
                    
                    # No need to check grid[r-1][c] anymore, which has already been processed before.
                    #if r-1 >= 0 and grid[r-1][c] == '1': uf.union(r*nc+c, (r-1)*nc+c)
                    if r+1 < nr and grid[r+1][c] == '1': uf.union(r*nc+c, (r+1)*nc+c)
                    #if c-1 >= 0 and grid[r][c-1] == '1': uf.union(r*nc+c, r*nc + c-1)
                    if c+1 < nc and grid[r][c+1] == '1': uf.union(r*nc+c, r*nc + c+1)
        
        return uf.count