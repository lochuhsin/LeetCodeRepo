'''
Although i have figured it out by myself. There are several twists
that should mention.

The key idea is simple, run bfs.

Okay if one runs dfs, it is indeed a solution but
needs to create a result list inorder to contains several
different approach to the target value (amout).

For example [1, 2, 3]-> 5, there are steps = [5, 3, 2], three kinds
of solutions. Return the least one. as return min(steps)

So it is natural to run bfs, since the algorithm tends to find the
shortest path to the target.

Another point to mention is that, remember to creating a seen dictionary,
as i forgot to do so. It turns out running into TLE. The reason is i thought
the graph contains no cycles so there is no need to create seen dict. However
this is wrong~~~.

The final point is the stop condition, the original idea is using a flag
to check if the value is over the target when summing up. But, i came up a
better solution is using (keep going if non negetive).
'''


from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        seen_target = {}
        q = deque()
        for i in coins:
            q.append((i, amount, 1))

        while q:
            coin, target, count = q.popleft()
            if target - coin == 0:
                return count

            elif (new_target := target - coin) > 0 and new_target not in seen_target:
                for i in coins:
                    seen_target[new_target] = None
                    q.append((i, new_target , count+1))

        return -1
