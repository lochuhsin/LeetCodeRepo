'''
Still haven't figure out why yet.....'
'''


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Base case.
        if 1 not in nums:
            return 1
        
        # Replace negative numbers, zeros,
        # and numbers larger than n by 1s.
        # After this convertion nums will contain 
        # only positive numbers.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        # Use index as a hash key and number sign as a presence detector.
        # For example, if nums[1] is negative that means that number `1`
        # is present in the array. 
        # If nums[2] is positive - number 2 is missing.
        for i in range(n): 
            a = abs(nums[i])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])
            
        # Now the index of the first positive number 
        # is equal to first missing positive.
        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return n
            
        return n + 1
    
    
'''
This is an one pass solution
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
  
        i = 0
        end = len(nums)

        while i != end:
            val = nums[i]
            
            if val == i+1:
                i += 1
            elif val > end or val <= 0 or nums[val -1] == val:
                end = end - 1
                nums[i], nums[end] = nums[end], nums[i]
            
            else:
                nums[i], nums[val - 1] = nums[val - 1], nums[i]
                
        return i + 1
    

'''one pass original version'''
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        
        
        // We will partition the array into two sides, with one copy of each number
        // on the left, in order, as far as possible.
        // [1, 2, 3, 4, 5, ..., n][...(everything else, but not n+1)...].
        
        
        int i = 0, end = nums.size();
        
        
        // Call LeftPartition the interval [1, ..., i - 1]
        // Call RightPartition the interval [nums[end], nums[nums.size() - 1]].
        // Initially, both are empty.
        // At the end, when "i" and "end" meet, call the results FinalLeftPartition and FinalRightPartition.
        // Then the answer to the problem is 1 + size(FinalLeftPartition).
        //
        // We build those intervals in-place, by swapping elements when necessary, and updating i and end.
        
        
        
        while (i != end) {
            int val = nums[i];
            if (val == 1 + i)             // Number is in the right place. We may consider it part of LeftPartition, and advance i.
                ++i;
                
                
            else if (
                val > end                    // If this should go in FinalLeftPartition, then that would overlap with FinalRightPartition.
                || val <= 0                   // The number is negative, it cannot possibly belong in FinalLeftPartition.
                || nums[val - 1] == val                // This is a duplicate. It doesn't belong in FinalLeftPartition.
                
                
                
                    // How can we get away with checking just this one spot for a duplicate?
                    // See the next "else" branch -- we always put values into this exact spot.
            ) {
                
                
                // If any of the above statements is true, this value doesn't need to be in FinalLeftPartition.
                // So we may put it in the right partition,
                // and advance "end".
                
                
                swap(nums[i], nums[--end]);
                
                
                // Now nums[i] has some new value that we haven't considered before, so
                // leave "i" as is and go back to the top of the loop.
                
                
            } else {
                
                
                // We don't yet know whether val should be in
                // FinalLeftPartition or FinalRightPartition, so put it in neither.
                // In order to consider another value, place val so that it matches its own index;
                // that is, place it where it will be if indeed it ends up in FinalLeftPartition,
                // and next consider the element there.
                
                
                swap(nums[i], nums[val - 1]);
                
                
                // We learned nothing new about what elements will be in FinalLeftPartition or FinalRightPartition,
                // and nums[i] has the previous value of nums[val - i], which we haven't dealt with yet,
                // so continue the loop without advancing either pointer.
                // But we did make useful progress in this branch: now in the future, if we see the same "val"
                // again, we will know it's a duplicate, because of the "nums[val - 1] == val" check above!
            }
        }
        return i + 1;
    }
};
