'''
Still figuring out why

Btw, there are 4 solutions, make sure understanding every answer.
'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sums = 0
        d = {0: 1}

        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k, 0)  # get key sums-k, return 0 if not exist
            d[sums] = d.get(sums, 0) + 1
            print(sums-k)

        return(count)
