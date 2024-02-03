class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [['g' for i in range(n)] for i in range(m)]
        for i in guards:
            matrix[i[0]][i[1]] = 'G'
        for i in walls:
            matrix[i[0]][i[1]] = 'W' 
       
        count = 0
        for x,y in guards:
            if x > 0: # checks left of the current guard
                for j in range(x-1,-1,-1):
                    curr = matrix[j][y]
                    if curr == 'W' or curr == 'G':
                        break
                    else:
                        matrix[j][y]='r'

            if x < m-1: # checks right of the current guard
                for j in range(x+1,m):
                    curr = matrix[j][y]
                    if curr == 'W' or curr == 'G':
                        break
                    else:
                        matrix[j][y]='r'
            
            if y > 0: # checks above of the current guard
                for j in range(y-1,-1,-1):
                    curr = matrix[x][j]
                    if curr == 'W' or curr == 'G':
                        break
                    else:
                        matrix[x][j]='r'
            
            if y < n-1: # checks below of the current guard
                for j in range(y+1,n):
                    curr = matrix[x][j]
                    if curr == 'W' or curr == 'G':
                        break
                    else:
                        matrix[x][j]='r'
        
        for i in matrix: # goes through matrix counting green boxes
            for j in i:
                if j == 'g':
                    count += 1       
        return count