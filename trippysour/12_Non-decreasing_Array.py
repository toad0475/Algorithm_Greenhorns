def checkPossibility(nums):
    if len(nums) < 3: return True # 3 미만이면 무조건 True
    elif len(nums) == 3:
        count = 0
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i] : count += 1
        return count < 2
    else:
        def findfalse(nums):
            count = 0
            isTrue = False
            for i in range(len(nums)-1):
                if nums[i+1]<nums[i] : 
                    count += 1
                    if nums[i-1] > nums[i+1]:
                        if i+1 == len(nums)-1: isTrue = True
                        else:
                            if nums[i-1]!=nums[i] or nums[i+1] == nums[i+2]: isTrue = False
                    else: 
                        isTrue = True
                        continue
            return {'count':count, 'isTrue' : isTrue}
        if findfalse(nums)['count'] < 2: return findfalse(nums)['isTrue']
        else: return findfalse(nums)['count'] < 2

#print(checkPossibility([3,4,2,3]))
#1일때 false 조건 명확히해야함
