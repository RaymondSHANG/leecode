from typing import List

#Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen=0
        left = 0
        right = 0
        k_left=k
        #extend to right, that nums[right]==0 or end of num
        while k_left>-1 and right < len(nums):
            if nums[right]==0:
                #flip
                k_left = k_left-1
                if k_left < 0:
                    break
            right = right +1
        if k_left >=0:
            return right-left
        else:
            maxlen = right-left
        #nums[right]==0
        for left in range(1,len(nums)):
            #change only when nums[left-1]==0
            if nums[left-1]==0:
                #release one flip position
                right=right+1
                while right < len(nums):
                    if nums[right]==0:
                        break
                    right = right +1
            
            len_temp = right-left
            if maxlen < len_temp:
                maxlen = len_temp
            if right>=len(nums):
                return maxlen
            
        return maxlen



nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

test = Solution()
print(test.longestOnes(nums,k)) #6
assert(6==test.longestOnes(nums,k))