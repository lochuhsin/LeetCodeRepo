'''
Using Bfs technique
Consider every bus stop as a state, 
for every state have their reachable stop
 => dic[state: 1] = [reachable states: 1, 2, 3, 4, 5..... etc]
Remember the reachable states contains ifself.
'''


'''
My algorithm .... reach time exceed ......
'''
import queue

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        dic = {}
        
        for i in routes:
            for stop in i:
                if stop not in dic:
                    dic[stop] = list(i)
                else:
                    dic[stop] += [r for r in i if r != stop]

        q = queue.Queue()
        q.put(source)
        
        dic_traveled = {}
        
        level = 0
        while not q.empty():
            
            next_queue = queue.Queue()
            while not q.empty():
                node = q.get()
                
                if node == target: return level

                dic_traveled[node] = level
                for i in dic[node]:
                    if i not in dic_traveled:
                        next_queue.put(i)
            level += 1
            q = next_queue

        return -1