class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 3: return True # 3 미만이면 무조건 True
        else:
            count = 0
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]: # i+1이 i보다 클때
                    count += 1 # count + 1씩
                    if i == 0: nums[i] = nums[i+1] # i가 0 이라면 i를 i+1로 바꾸기
                    elif i == len(nums)-2: nums[i+1] = nums[i] # i가 마지막 index-1(len(nums)-2)라면 i+1을 i로 바꾸기
                    else: # 그 사이의 수들 이라면
                        if nums[i-1] > nums[i+1]: nums[i+1] = nums[i] # i-1이 i+1보다 크면 i+1을 i로 바꾸기
                        else: nums[i] = nums[i-1] # 아니라면 i를 i-1로 바꾸기
                if count == 2: break # count가 2가 되면 반복문 정지
        return count < 2 
    
# 192 ms	13.8 MB
# https://leetcode.com/submissions/detail/293815905/
# 3322 = F / 3323 = T / 3423 = F 
