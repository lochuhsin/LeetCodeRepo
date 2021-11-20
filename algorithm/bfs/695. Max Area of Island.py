'''
just run bfs or dfs, sum the area
'''
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def bfs(start, grid):
            seen, area, q = {start: None}, 0, deque([start])
            while q:
                r, c = q.popleft()
                area += 1

                for ir, ic in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_r, new_c = r+ir, c+ic
                    if (0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and
                                grid[new_r][new_c] == 1 and (new_r, new_c) not in seen):

                        q.append((new_r, new_c))
                        grid[r][c] = "xxx"
                        seen[(new_r, new_c)] = None
            return area

        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs((r, c), grid))
        return max_area
