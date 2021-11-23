'''
The first one is a naive solution: (too sad i didn't even come up with this one.)
Run dfs in each cell with no matter what, the direction choose the monolic increase
then get the maximum length. One may wonder what if we start at the middle ?
Well there is no need to worry. Since we run dfs on every cell, we eventually will
meet the head of the longest path. 


Havn't understand faster approach.
'''


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def naive_dfs(matrix, s_r, s_c):
            nonlocal directions
            
            ans = 0
            for r, c in directions:
                r += s_r
                c += s_c
                if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] > matrix[s_r][s_c]:
                    ans = max(ans, naive_dfs(matrix, r, c))
            return ans + 1

        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if len(matrix) == 0: return 0
        
        rows = len(matrix)
        columns = len(matrix[0])
        
        length = 0
        
        ans = 0
        for r in range(rows):
            for c in range(columns):
                ans = max(ans, naive_dfs(matrix, r, c))
                
        return ans
                