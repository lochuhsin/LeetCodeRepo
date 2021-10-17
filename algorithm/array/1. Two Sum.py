'''
Thought process:
If a list that contains two numbers that sums up to target,
Create a dictionary that stores the value of the opposite value(target - v) and position
when it reaches the next number(target - v) found out that the value is already exist in 
the container returns the current value position and the container stored position.

'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, v in enumerate(nums):
            if target - v in dic:
                return [i, dic[target - v]]
            else:
                dic[v] = i