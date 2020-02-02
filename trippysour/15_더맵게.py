import heapq

def solution(scoville, K):
    answer = 0

    if min(scoville) >= K: return answer
    # min이 k보다 크거나 같으면 그냥 바로 리턴

    else:
        heapq.heapify(scoville)
        # 오름차로 정렬

        while scoville[0]<K:
            if len(scoville)<2: return -1
            # 더이상 min과 next_min을 넣어서 계산 할 수 없을 때 리턴 -1
            else:
                min_scoville = heapq.heappop(scoville)
                # 변수 지정하면서 제일 작은 수 pop
                nextmin_scoville = heapq.heappop(scoville)
                # 그 다음 작은 수가 이제 제일 작은 수가 되었으므로 그걸 다시 pop
                heapq.heappush(scoville, min_scoville+nextmin_scoville*2)
                # 두 변수들로 계산 한 걸 스코빌에 push
                answer += 1

    return answer

#print(solution([9, 2, 3, 1, 10, 12], 7))
