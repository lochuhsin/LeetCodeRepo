# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0
        self.hashtable = {0:None}
        self.recover(root)
        self.tree = root
        
        
    def recover(self,node):
        if node.right == None and node.left == None:
            return None
        
        
        if node.left != None:
            node.left.val = node.val*2 + 1
            self.hashtable[node.left.val] = None
                
            self.recover(node.left)
        
        if node.right != None:
            node.right.val = node.val*2 + 2
            self.hashtable[node.right.val] = None
        
            self.recover(node.right)
        
        
        
    def find(self, target: int) -> bool:
        return target in self.hashtable.keys()
        
    

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)