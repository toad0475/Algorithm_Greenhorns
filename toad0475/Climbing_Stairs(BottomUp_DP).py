# submission: https://leetcode.com/submissions/detail/282059830/

class Solution:
    def climbStairs(self, n: int) -> int:
        f={}
        for i in range(1, n+1):
            if i==1: f[i]=1
            elif i==2: f[i]=2
            else:
                f[i]=f[i-1]+f[i-2]
        return f[n]
        
