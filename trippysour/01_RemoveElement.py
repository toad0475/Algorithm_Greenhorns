class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = nums.count(val) 
        for i in range(count): 
            nums.remove(val) 
        return len(nums)
