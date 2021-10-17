'''
Thought process:
create new container, fill up all elements from nums1 and nums2
find median.

Time complexity O(m+n)

'''


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        combine_list = []
        i1 = 0
        i2 = 0

        while i1 < len(nums1) and i2 < len(nums2):
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
        elif len(combine_list) % 2 == 0:
            return (combine_list[int((len(combine_list)-1)/2)] + combine_list[int(len(combine_list)/2)])/2
        else:
            return combine_list[int((len(combine_list)-1)/2)]

'''
Another solution O(min(nums1, nums2))
Still needs to figure out
'''


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        l1, l2 = len(nums1), len(nums2)

        if l1 > l2:
            nums1, nums2, l1, l2 = nums2, nums1, l2, l1
        if l2 == 0:
            raise ValueError

        imin, imax, half_len = 0, l1, (l1+l2+1) / 2
        while imin <= imax:
            i = int((imin + imax) / 2)
            j = int(half_len - i)

            if i < l1 and nums2[j-1] > nums1[i]:
                imin = i + 1

            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1

            else:
                if i == 0: max_left = nums2[j-1]
                elif j == 0: max_left = nums1[i-1]
                else: max_left = max(nums1[i-1], nums2[j-1])

                if (l1 + l2) % 2 == 1:
                    return max_left

                if i == l1: min_right = nums2[j]
                elif j == l2: min_right = nums1[i]
                else: min_right = min(nums1[i], nums2[j])

                return (max_left+min_right) / 2












