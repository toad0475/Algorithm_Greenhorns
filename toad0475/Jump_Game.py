# submission: https://leetcode.com/submissions/detail/289481517/

# nums를 top-down으로 수행하여 nums의 끝에 도달할 수 있는지 판단하는 알고리즘. 
# nums 끝에 도달 가능하다고 판단되면 그 인덱스 값(lastpos)을 갱신한다. 
# nums의 0번째 인덱스까지 연산을 마친 후 lastpos가이 0이면 True 그렇지 않으면 False를 반환.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        lastpos=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=lastpos:
                lastpos=i
        return lastpos==0
