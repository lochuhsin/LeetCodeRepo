'''
Simple, run bfs with an external flag to control
whether the order should reverse.

One optimizational point is that instead of reversing
the list after appending the val, reverse the appending
order will be better.

ps: the data structure can be changed using deque~~
to perform appendleft and normal append
'''


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return None
            
        
        level_val = []
        flag = 0
        
        def bfs(child_list):
            
            if len(child_list) < 1:
                return None
            
            nonlocal level_val
            nonlocal flag
            
            val = []
            new_child_list = []
            
            for node in child_list:
                val.append(node.val)
                
                if node.left:
                    new_child_list.append(node.left)
                    
                if node.right:
                    new_child_list.append(node.right)
            
            if flag == 0:
                level_val.append(val)
                flag = 1
                
            else:
                level_val.append(val[::-1])
                flag = 0
                
            bfs(new_child_list)

        start = [root]    
        bfs(start)
        
        return level_val


'''
Optimization by using deque
'''

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return None
           
        
        level_val = []
        flag = 0
        
        def bfs(child_list):
            
            if len(child_list) < 1:
                return None
            
            nonlocal level_val
            nonlocal flag
            
            val = deque()
            new_child_list = []
            
            for node in child_list:
                if flag == 0:
                    val.append(node.val)
                else:
                    val.appendleft(node.val)
                
                if node.left:
                    new_child_list.append(node.left)
                    
                if node.right:
                    new_child_list.append(node.right)
            
            level_val.append(val)
            flag = 1 if flag == 0 else 0
            bfs(new_child_list)
            

        start = [root]    
        bfs(start)
        
        return level_val