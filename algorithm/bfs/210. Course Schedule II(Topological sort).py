'''
Using dfs to solve topological sort.
Still haven figure out yet.

There are 2nd solution. using Indegree (kahn's algorithm)
'''


from collections import defaultdict


class Solution:
    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)

        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topological_sorted_order = []
        is_possible = True

        # By default all vertces are WHITE
        color = {k: Solution.WHITE for k in range(numCourses)}
        def dfs(node):
            nonlocal is_possible

            # Don't recurse further if we found a cycle already
            if not is_possible:
                return

            # Start the recursion
            color[node] = Solution.GRAY

            # Traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                         # An edge to a GRAY vertex represents a cycle
                        is_possible = False

            # Recursion ends. We mark it as black
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == Solution.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []


'''
For detail, see 207
'''
class Solution:
    def findOrder(self, numCourses, prerequisites):
        order = []

        graph_dic = defaultdict(list)
        indegree = [0 for i in range(numCourses)]

        edgs_count = 0  # edges count
        for course, precourse in prerequisites:
            graph_dic[precourse].append(course)
            indegree[course] += 1
            edgs_count += 1

        q = deque([i for i in range(len(indegree)) if indegree[i] == 0])

        while q:
            node = q.pop()
            order.append(node)
            for new_node in graph_dic[node]:
                indegree[new_node] -= 1
                edgs_count -= 1

                if indegree[new_node] == 0:
                    q.append(new_node)
        return order if edgs_count == 0 else []
