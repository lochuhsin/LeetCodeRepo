class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        container = [None]*len(nums)
        
        for i in range(len(nums)):
            value = nums[i]
            count = 0
            for j in range(len(nums)):
                if value > nums[j]:
                    count += 1
            container[i] = count
        
        return container