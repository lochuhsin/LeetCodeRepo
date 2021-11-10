'''
Run bfs , invert from right side insert
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return None
        
        node_list = [root]
        val_list = []
        while len(node_list) > 0:
            
            new_node_list = []
            val_list.append(node_list[0].val)  # add rightest node val
            
            for node in node_list:
                if node.right:
                    new_node_list.append(node.right)
                if node.left:
                    new_node_list.append(node.left)
                    
            node_list = new_node_list
        return val_list
                    