'''
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.

1 <= s.length <= 105
s contains only lowercase English letters.
'''
class Solution:
    def longestPrefix(self, s: str) -> str:
        