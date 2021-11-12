'''
Brilliant thought

consider p's ancestor to root. The path may be like
p -> p1 -> p2 -> p3 -> c1 -> c2 -> c3 -> root
as p1 .... p3 refers to p's ancestor, c1 ... c3 refers to common ancestor.

consider q's ancestor to root. if the path is:
q -> q1 -> q2 -> q3 -> c1 -> c2 -> c3 -> root

Then it is obvouisly that the algorithm stops at c1.
(While loop with fou loops)

However if the q path:
q -> q1 -> c1 -> c2 -> c3 -> root
the paths of two length is different.

we exchange two pointers q and p to the start point when both reach the root
therefore the pathes becomes:

p -> p1 -> p2 -> p3 -> c1 -> c2 -> c3 -> root -> q -> q1 -> [c1] -> c2 -> c3 -> root
q -> q1 -> c1 -> c2 -> c3 -> root -> p -> p1  -> p2 -> p3 -> [c1] -> c2 -> c3 -> root

since the path must be the same, the algorithm with while loop will 
"garentee" stops at c1  

ps: convert a tree problem to two pointer linked list problem.
'''


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
            
        return p1