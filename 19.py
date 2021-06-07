# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        container = []
        node = head
        while True:
            if node == None:
                break
            else:
                container.append(node)
                node = node.next
                
        if len(container) == 0 or len(container) == 1:
            return None
        if n == len(container):
            return container[1]
        
        else:
            preRemoveNode = container[-n-1]
            RemoveNode = container[-n]
            
            preRemoveNode.next = RemoveNode.next
        
        return head
        
            
            
                