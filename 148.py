# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:            
        def mergesort(arr):
            if len(arr) == 1:
                return arr
            mid = int(len(arr)/2) if len(arr) % 2 == 0 else int((len(arr)-1)/2)
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])
            
            l = 0
            r = 0
            newarr = []
            while True:
                if l == len(left) or r == len(right):
                    break
                if left[l].val < right[r].val:
                    newarr.append(left[l])
                    l += 1
                else:
                    newarr.append(right[r])
                    r += 1
            
            if l != len(left):
                for i in range(l,len(left)):
                    newarr.append(left[i])
            else:
                for i in range(r,len(right)):
                    newarr.append(right[i])
            return newarr
        
        if head == None:
            return head
        elif head.next == None:
            return head
        
        container = []
        node = head
        while True:
            if node == None:
                break
            else:
                container.append(node)
            node = node.next
        container = mergesort(container)
        for i in range(len(container)):
            if i+1 == len(container):
                pass
            if i == len(container)-1:
                container[i].next = None
            else:
                container[i].next = container[i+1]
            
        return container[0]
                
    
        
                    
            
            
            
            
            
            
            