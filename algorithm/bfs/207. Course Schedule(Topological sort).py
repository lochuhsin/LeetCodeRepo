'''
using kahn's algorithm. implemented by myself
few detail's aren't quite sure yet.

This is what i know by far:

First we construct a graph, or whatever it is simple to represent.

The first key concept is, if the there is an order in graph,
the first node don't have any ancestors. That is indegree is zero.

Therefore we need to create a node indegree tracking list. I uses
list as container. index to be the node, value be the indegree.
Just like dictionary however the key is index, val is list element.

Second inorder to determind the order of the nodes, we use remove edges
technique. if the indegree of the node is zero than store it into list.
this is the key of topological sort.

forexample:

1 -> 2
1 -> 3
2 -> 4
3 -> 5
4 -> 4

now since the indegree of 1 is 0. 1 becomes the first order.
after reaches 1 we remove one and goes to 2 and 3 (bfs or dfs whatever)

since the edge 1 -> 2, 1 -> 3 have been walked, we remove the edges.
(In this perticular problem, we don't actually remove the edges, we minus
the indegree by 1.) now since the indegree of 2 and 3 is now zero. we add them
into order, so on and so forth. ( current order -> [1, 2, 3] or [1, 3, 2])

'''
from collections import defaultdict, deque


class Solution(object):
    def canFinish(self, n, prerequisites):
        # if curious of course order;
        # course_list = []

        graph_dic = defaultdict(list)
        indegree = [0 for i in range(n)]

        total_depth = 0
        for course, precourse in prerequisites:
            indegree[course] += 1
            graph_dic[precourse].append(course)
            total_depth += 1

        q = deque([i for i in range(n) if indegree[i] == 0])

        removededges = 0
        while q:
            node = q.popleft()
            # course_list.append(node)

            for next_node in graph_dic[node]:
                indegree[next_node] -= 1
                removededges += 1

                if indegree[next_node] == 0:
                    q.append(next_node)

        return removededges == total_depth
