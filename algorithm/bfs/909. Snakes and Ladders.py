'''
This is simply a dry run bfs. But .... the tricky part
is to calculate the correct label and position

Detailed explantion
https://leetcode.com/problems/snakes-and-ladders/discuss/794701/C%2B%2B%3A-bfs-oror-detailed-explanation-oror-faster-than-99.31
'''


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def label_to_position(label):
            r, c = divmod(label-1, n)
            if r % 2 == 0:
                return n-1-r, c
            else:
                return n-1-r, n-1-c
            
        seen = set()
        queue = collections.deque()
        queue.append((1, 0))
        while queue:
            label, step = queue.popleft()
            r, c = label_to_position(label)
            if board[r][c] != -1:
                label = board[r][c]
            if label == n*n:
                return step
            for x in range(1, 7):
                new_label = label + x
                if new_label <= n*n and new_label not in seen:
                    seen.add(new_label)
                    queue.append((new_label, step+1))
        return -1

'''
Very clean but a little bit difficult to comprehense
'''
class Solution:
    def snakesAndLadders(self, board):
        n = len(board)
        need = {1: 0}
        bfs = [1]
        for x in bfs:
            for i in range(x + 1, x + 7):
                a, b = (i - 1) / n, (i - 1) % n
                nxt = board[~a][b if a % 2 == 0 else ~b]
                if nxt > 0: i = nxt
                if i == n * n: return need[x] + 1
                if i not in need:
                    need[i] = need[x] + 1
                    bfs.append(i)
        return -1


'''
Optimize with more detail
'''
class Solution:
    def snakesAndLadders(self, board):
        n = len(board)
        need = {1: 0}
        bfs = [1]
        for x in bfs:
            refuse_steps = False
            for i in range(min(n**2, x + 6), x, -1):
                a, b = (i - 1) // n, (i - 1) % n
                nxt = board[~a][b if a % 2 == 0 else ~b]
                if nxt > 0: i = nxt
                if i == n * n: return need[x] + 1
                if nxt == -1 and refuse_steps: continue  # here
                if nxt == -1: refuse_steps = True  # and here
                if i not in need:
                    need[i] = need[x] + 1
                    bfs.append(i)
        return -1