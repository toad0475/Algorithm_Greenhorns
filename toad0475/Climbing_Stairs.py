# submission: https://leetcode.com/submissions/detail/282036526/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0]*n
        return self.fibo_dp(0,n,memo)

    def fibo_dp(self,i, n, memo):
        if i>n:
            return 0
        if i == n: 
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.fibo_dp(i+1,n,memo) + self.fibo_dp(i+2,n,memo)
        return memo[i]
