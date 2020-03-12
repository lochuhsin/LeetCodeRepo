class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        count = 0
        for i in range(len(nums)):
            string = str(nums[i])
            
            if len(string) % 2 == 0:
                count += 1
                
        return count
            
