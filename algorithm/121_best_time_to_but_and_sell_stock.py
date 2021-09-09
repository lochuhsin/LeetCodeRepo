# Thought process
'''
The first attemp and most intuitive one is approaching by using
O(n^2) time complexity, iterate over all outcome of value, and check
whether the value is maximum. If the maximum value is less then zero,
return 0 instead.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maximum = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                v = prices[j] - prices[i]
                if v > maximum:
                    maximum = v
        if maximum < 0:
            return 0
        return maximum


# Thought process
'''
The second solution of time complexity is O(n), the core thought is
using local low variable to contain the lowest value.

Then using the current price - current lowest value to get the difference,
compare to the local result.

The key point is, when looping over the for loop. Record the compare the price[i]
with the lowest price to get the current low price. After that if the current price is the lowest,
the difference will be zero. as result = max(result, prices[i] - low) shows.

To remind that lowest price might not be the global lowest price.
Consider [5, 4, 3, 2, 1]. Obviously there are no profit in this array. Although
5 is the maximum and 1 is the minimum.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if prices is None or len(prices)<=1:
            return 0

        result = 0
        low = prices[0]
        for i in range(len(prices)):
            low = min(low, prices[i])
            result = max(result, prices[i] - low)
        return result

