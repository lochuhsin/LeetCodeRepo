class node(object):

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tree right rotation
def right_rotation(node: 'node') -> 'node':

    pointer = node.left
    node.left = pointer.right
    pointer.right = node 
    return pointer

# tree left rotation
def left_rotation(node: 'node') -> 'node':

    pointer = node.right
    node.right = pointer.left
    pointer.left = node
    return pointer
