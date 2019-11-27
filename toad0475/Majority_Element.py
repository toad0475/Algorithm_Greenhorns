# submission: https://leetcode.com/submissions/detail/282069903/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numset=set(nums)
        countdict = {i:nums.count(i) for i in numset}
        return max(countdict, key=countdict.get)
        
