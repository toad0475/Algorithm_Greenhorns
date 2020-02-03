# 재귀로 풀었고, 돌아가긴 하는데 통과가 왜 안되는지 모르겠음ㅜ

def recursion(scoville,K,ans):
    if len(scoville)>1:
        if scoville[0]>=K:
            return ans
        else:
            scoville[1]=scoville[0]+(scoville[1]*2)
            return recursion(scoville[1:],K,ans+1)
    else:
        return ans if scoville[0]>=K else -1
def solution(scoville,K):
    answer=0
    return recursion(sorted(scoville),K,answer)

print(solution([10,1,1,1,0,12,5,4],7))
