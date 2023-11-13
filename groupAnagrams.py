'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
'''
class Solution:
    def groupAnagrams(self, strs: list):
    	hashvalue = dict()
    	res = []
    	for currentstr in strs:
    		tmp = ''.join(sorted(currentstr))
    		#print(currentstr,":",tmp)
    		if tmp not in hashvalue.keys():
    			hashvalue[tmp] = list()
    		hashvalue[tmp].append(currentstr)
    		
    	for key,value in hashvalue.items():
    		print(key,":",value)
    		res.append(value)
    	return res

#test
a = Solution()
print(a.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

