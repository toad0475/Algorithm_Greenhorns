# submission: https://leetcode.com/submissions/detail/282070214/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countdict = {i:nums.count(i) for i in set(nums)}
        return max(countdict, key=countdict.get)
        
