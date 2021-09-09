# Thought process
'''
Suppose we let target - elements in list as v,
then we check the element v is in the list or not.
If true then check the index or the value of itself
is equal to itself( or identical index). If not return
the current element index and the element v index.

To optimize the check v is in the given list, using hash table
or dictionary will be the better solution. 
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {v: i for i, v in enumerate(nums)}
        
        for i, v in enumerate(nums):
            if target - v in dic and i != dic[target-v]:
                return [i, dic[target-v]]



# Thought process

'''
There are one more optimization on space complexity then the above one
we initialize the dic (hashmap) with empty value. After every check
if the value is not in hashmap, throw the value and corresponding index
into the dictionary. 

This way it saves the space for hashmapping all the
elements to dictionary.

Also it reduces the check statement of if, because there is no longer needed
to check the value is duplicate or not.(The value will appears only ones including
the value itself.)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        for i, v in enumerate(nums):
            if target - v in dic:
                return [i, dic[target-v]]
            dic[v] = i
            

