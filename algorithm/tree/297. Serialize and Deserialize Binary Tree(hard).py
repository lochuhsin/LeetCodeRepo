'''
using dfs to serialize and deserialize 
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        
        q = deque([root])
        vals = []
        while q:
            node = q.popleft()
            if node is None:
                vals.append("x")
                continue
                
            vals.append(str(node.val))
            q.append(node.left)
            q.append(node.right)

        return ",".join(vals)        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data:
            return None
        
        vals = data.split(",")
        nodes = iter((None if v == 'x' else TreeNode(int(v))) for v in vals)
        root = next(nodes)
        q = deque([root])
        
        while q:
            node = q.popleft()

            left = next(nodes)
            if left:
                node.left = left
                q.append(left)
            
            right = next(nodes)
            if right:
                node.right = right
                q.append(right)
            
        return root
        