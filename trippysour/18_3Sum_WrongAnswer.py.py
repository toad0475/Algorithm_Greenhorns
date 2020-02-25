def threeSum(nums):
    def twoSum(nums,target):
        h = {} #중복제거를 위해 딕셔너리
        for i, num in enumerate(nums):
            n = target - num #target넘버를 만들기 위한 num의 다른 요소인 n 지정
            if n not in h: #n이 이미 h에 없으면 h에 key를 num과 value를 index로 넣어주기
                h[num] = i
            else: return [nums[h[n]], nums[i]] #있으면 return
    hash = {}
    answer = []
    for num in nums:
        if num == 0: pass
        else: 
            x = twoSum(nums, num)[0]
            y = twoSum(nums, num)[1]
            z = (x+y) * -1
            if z in nums:
                if x not in hash:
                    hash[x] = [x,y,z]
                    answer.append(hash[x])
                else: pass
    return answer

print(threeSum([-1, 0, 1, 2, -1, -4])) # [-1,0,1], [-1,-1,2]

#2sum을 구하고 2sum결과와 더해서 0을 만들 수 있는 제3의 숫자 찾기(-2sum)
#-1,-1,2일 때 조건도 해줘야함