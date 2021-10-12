'''
Two pointer solution

Consider two person, p1 & p2. Standing left of the valley and right of the valley
p1 only remembers the maximum height of his own path.
p2 only remembers the maximum height of his own path.

Now start running the loop.
1. If p1 current height is smaller than the p2 max_height, p1 move first.

Btw: why is max_height not p2 current height ?

The reason is: p1, p2 only stops at the height that is larger than other. Which means
the height must increases until larger than other, therefore the maximum height must be
the stopping point. ~ Vice versa

2. After p1 move one step, p1 recall the current height and the largest height that
stored in p1's memory. If the current height is smaller, add the difference between
p1_max_height and current height.

3. The loop goes, p1 height still smaller than p2_max_height(of course ~) this time
after p1 move one step, the height is higher than p1's memory. Therefore no need to add
volumn. p1 updates it's max_height memory.

4. The loop goes on and on untill (if exist) p1's max_height is larger than p2.
Now Turns to p2. 

'''


class Solution:
    def trap(self, height: List[int]) -> int:
        p1 , p2 = 0 ,len(height) -1
        max_p1_height, max_p2_height = height[p1], height[p2]
        
        volumn = 0
        
        while p1 != p2:
            
            if height[p1] < max_p2_height:
                p1 += 1
                if (p1_height := height[p1]) < max_p1_height:
                    volumn += max_p1_height - p1_height
                else:
                    max_p1_height = p1_height
                    
            else:
                p2 -= 1
                if(p2_height := height[p2]) < max_p2_height:
                    volumn += max_p2_height - p2_height
                else:
                    max_p2_height = p2_height
                    
        return volumn
        