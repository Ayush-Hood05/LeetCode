class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        flag_row = [False]*m
        flag_col = [False]*n
        # mark row and col
        for i in range (m):
            for j in range(n):
                if matrix[i][j] == 0:
                    flag_row[i] = True
                    flag_col[j] = True
        # for row update
        for i in range(m):
            if flag_row[i]:
                for j in range(n):
                    matrix[i][j] = 0
        # for col update
        for j in range(n):
            if flag_col[j]:
                for i in range(m):
                    matrix[i][j] = 0  
        
        