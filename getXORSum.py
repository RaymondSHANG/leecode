'''
what is XOR:
a ^ b = (a & nb) or (na & b)
given (a&b1)^(a&b2), what can we get?

(a&b1)^(a&b2)
= (a&b1) & (na or nb2) or ((na or nb1) & (a&b2))
= (a&b1&nb2) or (a & nb1 & b2)
= a & (b1^b2)
'''
class Solution:
    def getXORSum(self, arr1: list, arr2: list) -> int:
        xorA = 0
        xorB = 0
        for a in arr1:
        	xorA = xorA ^ a 
        for b in arr2:
        	xorB = xorB ^ b 
        return xorA & xorB

'''
Input: arr1 = [1,2,3], arr2 = [6,5]
Output: 0
Explanation: The list = [1 AND 6, 1 AND 5, 2 AND 6, 2 AND 5, 3 AND 6, 3 AND 5] = [0,1,2,0,2,1].
The XOR sum = 0 XOR 1 XOR 2 XOR 0 XOR 2 XOR 1 = 0.
Example 2:

Input: arr1 = [12], arr2 = [4]
Output: 4
Explanation: The list = [12 AND 4] = [4]. The XOR sum = 4.
'''
a = Solution()
arr1=[1,2,3]
arr2=[6,5]
print(0==a.getXORSum(arr1,arr2))
arr1=[12]
arr2=[4]
print(4==a.getXORSum(arr1,arr2))