class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newarray = []
        for i in range(n):
            newarray.append(nums[i])
            newarray.append(nums[i+n])
	return newarray
