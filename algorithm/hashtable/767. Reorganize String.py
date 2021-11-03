from collections import Counter

# Still haven't figure out how to do yet

'''
The idea is to build a max heap with freq. count
a) At each step, we choose the element with highest freq (a, b) where b is the element, to append to result.
b) Now that b is chosen. We cant choose b for the next loop. So we dont add b with decremented value count immediately into the heap. Rather we store it in prev_a, prev_b variables.
c) Before we update our prev_a, prev_b variables as mentioned in step 2, we know that whatever prev_a, prev_b contains, has become eligible for next loop selection. so we add that back in the heap.

In essence,

at each step, we make the currently added one ineligible for next step, by not adding it to the heap
at each step, we make the previously added one eligible for next step, by adding it back to the heap
'''


class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        c = Counter(s)
        pq = [(-value,key) for key,value in c.items()]
        heapq.heapify(pq)
        p_a, p_b = 0, ''
        while pq:
            a, b = heapq.heappop(pq)
            res += [b]
            if p_a < 0:
                heapq.heappush(pq, (p_a, p_b))
            a += 1
            p_a, p_b = a, b
        res = ''.join(res)
        if len(res) != len(s): return ""
        return res