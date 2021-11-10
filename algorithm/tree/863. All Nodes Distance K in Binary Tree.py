'''
First run bfs or dfs to insert every parent to node
(bfs and dfs are the same here, however dfs is more easy to code)
Then run bfs to locate the distance node. (remember to create seen dic)
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


import queue

class Solution:
    def distanceK(self, root, target, K):
        def dfs(node, par = None):  # pre-order traversal
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d+1))
        return []
            