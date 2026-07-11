class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # onion-peeling Approach
        # Movement [0][0] to [0][N]
        # Movement [0][N] to [N][N]
        # Movement [N][N] to [0][N]
        # Movement [N-1][0] to [1][0]
        m = len(matrix)
        n = len(matrix[0])
        res = []
        srow , scol , erow , ecol = 0 ,0 , m-1 , n-1
        while srow <= erow and scol <= ecol:
             # 1. Traverse Right (Top Row)
            for i in range(scol, ecol + 1):
                res.append(matrix[srow][i])
            srow += 1  

            # 2. Traverse Down (Right Column)
            for i in range(srow, erow + 1):
                res.append(matrix[i][ecol])
            ecol -= 1 

            # 3. Traverse Left (Bottom Row)
    
            if srow <= erow:
                for i in range(ecol, scol - 1, -1):
                    res.append(matrix[erow][i])
                erow -= 1  
            # 4. Traverse Up (Left Column)
            # Check if there is still a column to traverse
            if scol <= ecol:
                for i in range(erow, srow - 1, -1):
                    res.append(matrix[i][scol])
                scol += 1  # Move left boundary right

        return res

