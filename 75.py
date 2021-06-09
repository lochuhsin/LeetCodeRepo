class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)):
            for j in range(i,-1,-1):
                if j == 0:
                    pass
                elif nums[j] < nums[j-1]:
                    nums[j],nums[j-1] = nums[j-1],nums[j]