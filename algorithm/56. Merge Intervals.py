'''
Thought process:

1. the range_list [1, 8] is always in increasing order, therefor it is obvious if 
to range list is overlap such as -> [0, 10], [10, 15] or [0, 5], [1, 3] or [4, 6], [1, 5]

2. The problem is the input intervals isn't sorted.  
If isn't sorted, then there are complex tasks that we need to figure out the conditions
that the range is overlap.

However if the input interval is sorted by the start element, the condition will be very simple,
check the end value and start value to see if it is overlap.
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key= lambda x: x[0])
        merge = []
        hold = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= hold[1]:
                hold = [hold[0], max(hold[1], intervals[i][1])]

            else:
                merge.append(list(hold))
                hold = intervals[i]
        merge.append(hold)
        return merge


'''
Same thought, but cleaner solution
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort_list = sorted(intervals, key=lambda x: x[0])
        container = []
        for rang in sort_list:
            if not container or container[-1][1] < rang[0]:
                container.append(rang)
            else:
                container[-1][1] = max(container[-1][1], rang[1])
            
        return container