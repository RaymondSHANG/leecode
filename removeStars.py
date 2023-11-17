from typing import List
class Solution:
    def removeStars(self, s: str) -> str:
        pass


s = "leet**cod*e"

test = Solution()
print(test.removeStars(s)) #"lecoe"
assert("lecoe"==test.removeStars(s))