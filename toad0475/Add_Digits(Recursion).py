# submission: https://leetcode.com/submissions/detail/286392880/

class Solution:
    def addDigits(self, num: int) -> int: 
        if num < 10: return num
        else:
            res=0
            num_list = list(map(int, str(num)))
            num_map = {x:num_list.count(x) for x in num_list}
            for n in num_map:
                res += n*num_map[n]
            return self.addDigits(res)
