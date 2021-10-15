"""
loop over entire grid, if reaches zero, use bfs or dfs
however, my algorithm seems not pass the time limit test lul.
"""
import queue

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j) -> dict:
        node_list = queue.Queue()
        node_list.put((i, j))

        while not node_list.empty():
            i, j = node_list.get()
            grid[i][j] = 0

            if j+1 < len(grid[0]) and grid[i][j+1] == "1":
                node_list.put((i, j+1))

            if i+1 < len(grid) and grid[i+1][j] == "1":
                node_list.put((i+1, j))

            if j-1 >= 0 and grid[i][j-1] == "1":
                node_list.put((i, j-1))

            if i-1 >= 0 and grid[i-1][j] == "1":
                node_list.put((i-1, j))


'''
Leetcode solution (dfs , dfs) 
'''


class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

'''
Missing Union Find solution
'''

