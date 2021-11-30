'''
My first solution, one pass but O(N) space complexity.
I can comeup with 2-pass O(1) complexity, but not 1-pass O(1).

The second solution is 1-pass O(1). Very interesting.
'''


# Solution 1, 1-pass O(n)
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        node_list = []
        node = head
        while node:
            node_list.append(node)
            node = node.next
            
        node_list[k-1].val, node_list[-k].val  = node_list[-k].val, node_list[k-1].val
        return head


# 1-pass solution O(n) time complexity, O(1) space complexity

'''
The key concept is, after the current node reaches k
Not only set the front node pointer to current node.
Set the end node pointer to the head. Loop end node = end node.next
with the current node.

The reason is, when the current node reaches the end of linked list,
the distance between end node and current node is also k.
Therefore, when current node reaches the end. The end node points
to the exact place that is reverse position of k.
'''

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        front_node = None
        end_node = None
        node = head
        
        count = 0
        while node:
            count += 1
            
            if end_node: end_node = end_node.next
                
            if count == k:
                front_node = node
                end_node = head
                
            node = node.next
            
        front_node.val, end_node.val = end_node.val, front_node.val
        return head
