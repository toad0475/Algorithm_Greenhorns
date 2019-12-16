# submission: https://leetcode.com/submissions/detail/286393224/

class Solution:
    def addDigits(self, num: int) -> int: 
        return 0 if num==0 else (num-1)%9+1
