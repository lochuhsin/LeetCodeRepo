'''
This is my first come up solution
convert wordsDict into a hashtable, which
stores duplicate value with lists.

Now the problem converted to -> find smallest distance
between two words. My solution is O(n^2) which is not good.
'''

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dic = defaultdict(list)
        
        for i, v in enumerate(wordsDict):
            self.dic[v].append(i)


    def shortest(self, word1: str, word2: str) -> int:
        w1_occur = self.dic[word1]
        w2_occur = self.dic[word2]
        
        min_distance = float('inf')
        for d1 in w1_occur:
            for d2 in w2_occur:
                if (diff := abs(d1 - d2)) < min_distance:
                    min_distance = diff
        return min_distance

'''
This is an optimization solution for shortest path function
Time complexity goes down to O(m+n), which is linear.
'''


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dic = defaultdict(list)
        self.l = len(wordsDict)
        for i, v in enumerate(wordsDict):
            self.dic[v].append(i)


    def shortest(self, word1: str, word2: str) -> int:
        
        l1, l2 = self.dic[word1], self.dic[word2]
        i = j = 0
        res = self.l
        # O(m+n) time complexity
        while i < len(l1) and j < len(l2):
            res = min(res, abs(l1[i]-l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return res