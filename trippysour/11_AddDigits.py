class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            dr_n = 0
        elif num % 9 == 0:
            dr_n = 9
        else:
            dr_n = 1 + ((num - 1) % 9)
        return dr_n

# 자릿수근 공식을 그대로 코드에 적용
# https://leetcode.com/submissions/detail/286113898/
# 28ms, 12.7MB 
