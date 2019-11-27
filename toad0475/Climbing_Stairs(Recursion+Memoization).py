# submission: https://leetcode.com/submissions/detail/282063386/

class Solution:
    def __init__(self):
        self.memo={}
    def climbStairs(self, n: int) -> int:
        if n in self.memo: return self.memo[n]
        if n==1: f=1
        elif n==2: f=2
        else: 
            f=self.climbStairs(n-1)+self.climbStairs(n-2)
        self.memo[n]=f
        return f
