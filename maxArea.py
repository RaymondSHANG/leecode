from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_current = 0 
        
        while l<r:
            if height[l]<height[r]:
                current_min=height[l]
                l=l+1
            else:
                current_min = height[r]
                r=r-1
            area = (r-l+1)*current_min
            if area > max_current:n
                max_current=area
        return max_current
height = [1,8,6,2,5,4,8,3,7]
s = Solution()
print(s.maxArea(height))