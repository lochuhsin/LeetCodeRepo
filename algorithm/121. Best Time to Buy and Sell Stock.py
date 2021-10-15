'''
Straight foward is brute force of O(n^2)
However if think closely
The maximize profit comes with the smallest value in array.
Becarefull the time only goes foward.
Therefore we create a buy_value that stores the stock that
buy's in.

After start looping, There are two situations:

1. If the stock is lower than the buy_value
we which the buy_value to current one.
(The lower of buy value, the more possible that the profit comes)

2. If the stock is larger than the buy_value,
we get the sell difference(profit), however we must compare the
profit to the overall glob profit(max_profit).
If the profit is larger, than switch the max_profit to the current one.

To be noticed that, it is easy to fall in to a trap that search max(prices)
and min(prices), then calculate the difference. This is a wrong approach,
It can not ensure the min(prices) is always ahead max(prices)
ex: [9, 8, 7, 6, 5]

'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        max_profit = -1
        buy_value = float('inf')

        for i in prices:
            if i < buy_value:
                buy_value = i
            elif (profit := i - buy_value) > max_profit:
                max_profit = profit

        return max_profit if max_profit > 0 else 0