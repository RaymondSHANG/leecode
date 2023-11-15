from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        ch0=chars[0]
        newlen=0
        i=1
        for ch in chars[1:]:
            if ch == ch0:
                i=i+1
            else:
                chars[newlen]=ch0
                newlen = newlen + 1
                if i>1:
                    i_str=str(int(i))
                    for j in i_str:
                        chars[newlen]=j
                        newlen = newlen +1
                ch0=ch
                i=1
        
        chars[newlen]=ch0
        newlen = newlen + 1
        if i>1:
            i_str=str(int(i))
            for j in i_str:
                chars[newlen]=j
                newlen = newlen +1
        return newlen
    
    
chars = ["a","a","b","b","c","c","c"]

test = Solution()
print(test.compress(chars))