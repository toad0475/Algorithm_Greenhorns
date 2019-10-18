    
def greedy(count,name_len,notA_idxs):
    # 현재 idx에서 가장 가까운 A가 아닌 문자 찾기
    curr_idx = 0
    while notA_idxs:
        dists = []
            # 현재 idx에서 가장 가까운 A가 아닌 문자 찾기
        for idx in notA_idxs: # 요 부분이 아직 Brute force임!!
            dists.append(min(abs(idx-curr_idx),name_len-abs(idx-curr_idx)))
        min_dist = min(dists)
        count+= min_dist
        curr_idx = notA_idxs[dists.index(min_dist)]
        notA_idxs.pop(dists.index(min_dist))
    return count

def solution(name):
    alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 0 # 아웃풋
    alpha_len = len(alpha)
    name_len = len(name)
    notA_idxs = [] # name 중 A가 아닌 element의 index 리스트

    for i in range(name_len):
        if name[i] =='A':
            pass
        else:
            count += min(alpha.index(name[i]), alpha_len - alpha.index(name[i]))
            notA_idxs.append(i)    
    if len(notA_idxs) == name_len: # A가 없다면
        return count+(name_len-1)
    else: # A가 하나라도 포함되어 있다면
        return greedy(count, name_len, notA_idxs)        

    
# 테스트케이스
print(solution("AAABAAAAAABA"))
