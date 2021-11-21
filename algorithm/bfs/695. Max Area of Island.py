'''
just run bfs or dfs, sum the area
however. mine solution reaches TLE
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

'''
This solution uses seen dic, can't figure out why is faster. (I change value)
'''

from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid):
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans



