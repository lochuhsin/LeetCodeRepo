'''
Thought process:
create new container, fill up all elements from nums1 and nums2
find median.

Time complexity O(m+n)

'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combine_list = []
        i1 = 0
        i2 = 0
        
        while i1 < len(nums1) and i2 < len(nums2) :
            if nums1[i1] < nums2[i2]:
                combine_list.append(nums1[i1])
                i1 += 1
            else:
                combine_list.append(nums2[i2])
                i2 += 1
        
        combine_list += nums1[i1:len(nums1)]
        combine_list += nums2[i2:len(nums2)]

        if len(combine_list) < 1:
            return None
        elif len(combine_list)% 2 == 0:
            return (combine_list[int((len(combine_list)-1)/2)] + combine_list[int(len(combine_list)/2)])/2
        else:
            return  combine_list[int((len(combine_list)-1)/2)]