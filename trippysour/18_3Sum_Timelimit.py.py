from itertools import combinations

def threeSum(nums):
    sums = []
    combi = list(combinations(nums, 3))
    for i in combi:
        if sum(i) == 0:
            sums.append(list(i))
    for i in sums:
        i.sort()
    answer = list(set(map(tuple, sums)))
    return answer

print(threeSum([-1, 0, 1, 2, -1, -4]))
timelimit = [-15,6,7,0,-14,-5,-3,-10,-14,1,-14,-1,-11,-11,-15,-1,3,-12,7,14,1,6,-6,7,1,1,0,-4,8,7,2,1,-2,-6,-14,-9,-3,-1,-12,-2,7,11,4,12,-14,-4,-4,4,-1,10,3,-14,1,12,0,10,-9,8,-9,14,-8,8,0,-3,10,-6,4,-8,0,-1,-3,-8,-4,8,11,-3,-11,-8,8,3,10,-3,-4,-4,-14,12,13,-8,-3,12,-8,4,5,-1,-14,-8,8,-3,-9,-15,12,-5,-7,-15,-12,11,-11,14,11,12,3,6,-6]
print(len(timelimit)) #113개의 리스트요소일때 time리밋