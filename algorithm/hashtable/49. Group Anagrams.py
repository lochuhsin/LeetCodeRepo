# Not so obvious problem, and a little bit tricky

'''
The concept is, for given any string in strs, such as eat or ate or tea
For somehow convert them into (a, e, t) or given some unique way to define
these three characters.

Then stored them into a dic-> dic[(a, e, t)] = []
if after convert matches the key such as tea -> (a, e, t)
then the dictionary dic[(a, e, t)].append(tea). So on and so forth.

The solution below used an array of 26 space represents 26 characters.
using the first letter to be the base line of ascii value.
Ex: ord(a) = 97

if a char is 'a', then ord(a) - ord(a) = 0.
the position of character a is 0.
same as ord('b') - ord('a') = 1
the position for b is 1.
Then convert it to tuple -> to be the key of dictionary.


For another solution can be applied by gudols theory of prime numbers.
give : a = 2, b = 3, c=5 .........

Then the sum of ate, tea, eat will be the same and unique to other characters.
The downside is create a dictionary that connects the characters and prime numbers.
'''
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = collections.defaultdict(list)

        for s in strs:
            count = [0]*26
            for char in s:
                count[[ord(c) - ord('a')]] += 1
            ans[tuple(count)].append(s)

        return ans.values()


'''
using sorted str as mapped key.
Un-efficient in large strings. (nlogn)
Total complexity -> O(n * mlogm), m == len(string), n == len(strs)
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = collections.defaultdict(list)

        for string in strs:
            sort_s = sorted(string)
            ans[tuple(sort_s)].append(string)

        return ans.values()

