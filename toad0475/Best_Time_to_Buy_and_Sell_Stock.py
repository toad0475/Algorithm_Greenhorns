# leetcode submissions link : https://leetcode.com/submissions/detail/267898427/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices:
            minprice = prices[0]
        else:
            return 0
        profit = 0
    
        for i in range(1, len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > profit:
                profit = prices[i] - minprice
        return profit
