'''
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.

1 <= s.length <= 105
s contains only lowercase English letters.
'''
class Solution:
    def longestPrefix(self, s: str) -> str:
        pattern = [-1 for _ in s]
        i, j = 1, 0
        while i < len(s):
            if s[i] == s[j]:
                pattern[i] = j
                i += 1
                j += 1
            elif j > 0:
                j = pattern[j - 1] + 1
            else:
                i += 1
        return s[0:pattern[-1] + 1]
a = Solution()
print(a.longestPrefix("abcdabcdbcabcd"))