class Solution:
    def climbStairs(self, n: int) -> int:
        steps = {0:0, 1:1, 2:2}
        key = 3
        while key < n+1:
            steps[key] = steps[key - 2] + steps[key - 1]
            if key == n:
                break
            key = key + 1
        return (steps[n])

# https://leetcode.com/submissions/detail/283192822/