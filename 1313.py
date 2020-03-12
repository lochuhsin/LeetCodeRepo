class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        container = []
        for i in range(len(nums)):
            if i%2 == 0:
                count = nums[i]
            else:
                container += [nums[i]]*count
        return container

