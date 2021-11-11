'''
This solution is my first thought
however too many sorted functions
'''

from collections import defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        level_nodes = defaultdict(list)
        
        def dfs(node, coord, level):
            if not node:
                return

            nonlocal level_nodes
            val = node.val
            level_nodes[coord].append((val, level))
            dfs(node.left, coord-1, level+1)
            dfs(node.right, coord+1, level+1)
        
        dfs(root, 0, 0)
        level_list = sorted(list(level_nodes.keys()))

        output = []
        for i in level_list:
            nodes = sorted(level_nodes[i], key=lambda x: x[1])
            output.append([i[0] for i in nodes])
            
        return output

'''
Optimize the above of sorted, by using a very clever tune.
Record the minimum left side range and maximum right side range,
Then we generate the sequence by range(min left, max right).
No need to sort the column index now. LOL
'''
import queue
from collections import defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        dic = defaultdict(list)
        
        q = queue.Queue()
        q.put((root, 0))
        
        min_column = max_column = 0
        
        while not q.empty():
            node, coord = q.get()
            dic[coord].append(node.val)
            
            min_column = min(min_column, coord)
            max_column = max(max_column, coord)
            
            if node.left:
                q.put((node.left, coord-1))
                
            if node.right:
                q.put((node.right, coord+1))
                
        

        return [dic[i] for i in range(min_column, max_column + 1)]
