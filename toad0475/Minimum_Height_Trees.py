# https://leetcode.com/problems/minimum-height-trees/submissions/
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1: return [0]
        link = [set() for x in range(n)]
        for i, j in edges:
            link[i].add(j)
            link[j].add(i)

        ends = [i for i in range(n) if len(link[i]) == 1]

        while n > 2: # 이유는 2가 넘으면 반드시 또 다른 MHT가 1개 존재할 것이다. 
            newends = []
            n -= len(ends)
            for i in ends:
                poped = link[i].pop()
                link[poped].remove(i)
                if len(link[poped]) == 1: newends.append(poped)
            ends = newends
        return ends

#print(findMinHeightTrees(7,[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4],[0, 6]]))

