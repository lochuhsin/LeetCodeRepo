"""
Brute force solution
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        glob_len = 0
        for i in range(len(s)):
            loc_len = 0
            dic = {}
            for j in range(i, len(s)):
                if s[j] not in dic:
                    dic[s[j]] = None
                else:
                    if (leng := len(dic)) > loc_len:
                        loc_len = leng
                    dic = {s[j]: None}
            if len(dic) > loc_len:
                loc_len = len(dic)

            if loc_len > glob_len:
                glob_len = loc_len

        return glob_len

"""
window sliding solution

The concept is almost the same as my first thought,
create a dictionary that stores distinct char while looping
over the arr(strings). However i made a mistake that i exclude
all the dictionary value when encouter duplicate values. This
causes exceptions.
For example : abcdea
In my first solution is simple, dic = {a, b, c, d, e}, max_length=5
encounter a => dic = {a} -> length = 1, return max_length = 5

But !! heres the problem

string = a b c d e c f g h i j
so everthing is fine before second c,

dic = {a, b, c, d, e}
but when encounter c~

dic becomes => {c}
therefore the final dictionary becomes
dic = {c, f, g, h, i, j} , len = 6

But the True max sub string is:
dic = {d, e, c, f, g, h, i, j}, len = 8

So the major change is if encounter duplicates,
Instead of dropping every elements in the current dictionary,
drop the elements before the duplicate elements, including duplicate
itself.

In the above example, the dictionary becomes:
before dic = {a, b, c, d, e}
encounter dic = {d, e, c}
then move on~
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res


"""
window sliding optimization
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans


"""
leetcode clean answer
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        usedChar = {}

        for i, v in enumerate(s):
            if v in usedChar and start <= usedChar[v]:
                start = usedChar[v] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[v] = i

        return maxLength



