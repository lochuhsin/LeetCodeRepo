'''
Explanation
t % 60 gets the remainder from 0 to 59.
We count the occurrence of each remainders in a array/hashmap c.

we want to know that, for each t,
how many x satisfy (t + x) % 60 = 0.

The straight forward idea is to take x % 60 = 60 - t % 60,
which is valid for the most cases.
But if t % 60 = 0, x % 60 = 0 instead of 60.

One solution is to use x % 60 = (60 - t % 60) % 60,
the other idea is to use x % 60 = (600 - t) % 60.
Not sure which one is more straight forward.
'''

'''
This is the extension of two sum
'''

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int)
        ret = 0
        for t in time:
            if t % 60 == 0: # check if a%60==0 && b%60==0
                ret += remainders[0]
            else: # check if a%60+b%60==60
                ret += remainders[60-t%60]
            remainders[t % 60] += 1 # remember to update the remainders
        return ret
