from typing import List

#Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen=0
        for i in range(len(nums)):
            j=i
            k_left=k
            for j in range(i,len(nums)):
                if nums[j]==0:
                    k_left = k_left-1
                    if k_left == -1:
                        break
            if k_left==-1:
                max_temp=j-i
            else:
                #The lastone is 1, and early stop
                max_temp=j-i+1
            if maxlen < max_temp:
                maxlen=max_temp
            if k_left>-1:
                break
            
        return maxlen



nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

test = Solution()
print(test.longestOnes(nums,k)) #6