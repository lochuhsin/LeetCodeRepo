import collections
"""
using hashmap to store every domain, ex: google.com and com with visited values
If encounter same domain, add up values.
return everything in hash map
"""


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        ans = collections.Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)

            ## This part is clever
            frags = domain.split('.')
            for i in range(len(frags)):
                ans[".".join(frags[i:])] += count

        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]
