'''
using kahn's algorithm. implemented by myself
few detail's aren't quite sure yet
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
