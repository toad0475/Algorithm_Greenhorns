# submission: https://leetcode.com/submissions/detail/286392880/

class Solution:
    def addDigits(self, num: int) -> int: 
        # num이 10보다 작으면 그대로 리턴
        if num < 10: return num
        
        else:
            res=0
            # num을 리스트로 변환 (Ex.2019 -> [2,0,1,9]) 
            num_list = list(map(int, str(num)))
            # 리스트를 digit:count 형식의 dict로 변환 (Ex. [1,3,3,9] -> {1:1 , 3:2, 9:1} ) 
            num_map = {x:num_list.count(x) for x in num_list} 
            
            # dict의 요소들을 digit * count 해서 총합을 구함
            for n in num_map:
                res += n*num_map[n]
            
            # 총합을 재귀로 넘김
            return self.addDigits(res)
