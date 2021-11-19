'''
Using bidirectional bfs, introduce by solution, but coded on my own.
Simple bfs is still valid though
'''
from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        offsets = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        
        q = deque([(0, 0, 0)])
        seen = {(0, 0): 0}
        
        q_target = deque([(x, y, 0)])
        seen_target = {(x, y): 0}
        
        while True:
            
            r, c, count = q.popleft()
            r_tar, c_tar, count_tar = q_target.popleft()
            
            if (r, c) in seen_target:
                return count + seen_target[(r, c)]
            
            for ir, ic in offsets:
                if (r+ir, c+ic) not in seen:
                    seen[(r+ir, c+ic)] = count+1
                    q.append((r+ir, c+ic, count+1))
                    
                if (r_tar+ir, c_tar+ic) not in seen_target:
                    seen_target[(r_tar+ir, c_tar+ic)] = count_tar+1
                    q_target.append((r_tar+ir, c_tar+ic, count_tar+1))
            
