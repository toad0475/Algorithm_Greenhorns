# submissionL: https://leetcode.com/submissions/detail/292284842/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False # 수정할 Element가 이미 존재하는지 여부
        pos = 0          # 수정할 Element의 위치
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if modified:
                    return False
                modified = True
                pos = i
           
        if not modified:
            # 수정할 Element가 없음
            return True
        else:
            if pos==0 or pos==len(nums)-2:
                # 수정할 Element가 맨처음 또는 맨끝
                return True
            elif nums[pos-1]<=nums[pos+1] or nums[pos+2]>=nums[pos]:
                '''
                수정할 Element가
                  
                     *(pos)
                          *(pos+1) 형태이거나
                  *(pos-1)

                          *(pos+1) 형태일 때
                  *(pos-1)
                      *(pos) 
                '''  
                return True
