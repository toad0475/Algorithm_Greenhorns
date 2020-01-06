class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] >= len(nums)-1: return True # 첫 인덱스 0의 value가 이미 마지막 인덱스 보다 같거나 크면 True
        elif nums[0] == 0: return False# 첫인덱스의 value가 0이라면 무조건 False
        else:
            maxjump = 0
            for i, v in enumerate(nums):
                #print('maxjump :', maxjump, ',', 'i :',i , ',', 'v :', v, ',', 'i+v :',i+v)
                if i <= maxjump: # 현재 i값이 maxjump보다 작거나 같으면 도달할 수 있는 곳이니까
                    maxjump = max(maxjump, i+v) # 그곳에서 현재 maxjump와 현재 i+v 값 충에 큰 값으로 maxjump 바꿈
             return maxjump >= len(nums) - 1

            
# https://leetcode.com/submissions/detail/291741798/
# Runtime: 80 ms, Memory Usage: 14.9 MB
