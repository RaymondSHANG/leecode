'''
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.

1 <= s.length <= 105
s contains only lowercase English letters.
'''
class mykmp:
    def __mykmp__(self,pattern:str):
        self.pattern = pattern
        self.len = len(pattern)
        self.lps = [-1 for _ in range(len(pattern))]
        self.lps()

    def lps(self):
        #return lps array where each position records the happyPrefix location
        i, j = 0, 1
        while j < self.len:
            if self.pattern[i] == self.pattern[j]:
                self.lps[j] = i
                i += 1
                j += 1
            elif i > 0:
                i = self.lps[i-1]+1
            else:
                j += 1

    def search(self,s:str):
        i 


a = mykmp("aab")
print(a.longestPrefix("aaabaaa"))