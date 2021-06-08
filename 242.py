class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = {}
        for i in s:
            if i not in table.keys():
                table[i] = 1
            else:
                table[i] += 1
        for j in t:
            if j not in table.keys():
                return False
            else:
                table[j] -= 1
                
        for i in table.keys():
            if table[i] != 0:
                return False
        return True