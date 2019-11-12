n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
n_index = 0
from collections import defaultdict # 유사 딕셔너리 임포트
tree = defaultdict(int) # 밑에 leaf들을 검사할 때 key가 아닌 leaf 돌 때 에러나지 말라고 유사 딕셔너리
import itertools # itertools 임포트
leaf = list(itertools.chain(*edges)) # 2차원 리스트를 1차원 리스트로 바꾸기 sum(edges, []) 방법도 있지만 이 방법이 더 효율적이라고 함
for i in edges:
# bfs를 돌리기 위해 key가 tree의 index 이고 edge가 value인 유사 딕셔너리 생성
    tree[n_index] = set(edges[n_index])
    n_index = n_index + 1
# 출력값 {0: [0, 3], 1: [1, 3], 2: [2, 3], 3: [4, 3], 4: [5, 4]}
def bfs_path(tree, start, goal):
# 넓이 우선 탐색, start 와 goal을 넣어줘서 경로 찾기 함수, 이해는 완벽히 못함
    stack = [(start, [start])]
    result = []
    while stack:
        x, path = stack.pop()
        if x == goal:
            result.append(path)
        else:
            for m in tree[x] - set(path):
                stack.append((m, path + [m]))
    return print(result)
bfs_path(tree, 1, 5)
# 출력값 [[1, 3, 4, 5]]
bfs_path(tree, 2, 4)
# 출력값 [[2, 3, 4]]

# 이제부턴 한글
# 위에서 구한 edges의 1차원 리스트인 leaf 중에 count가 1인 애들을 리스트 = leaf_isolate
# leaf의 count가 1인 아이들은 한번만 연결 됐다는 뜻이니 인접해서 많이 붙어있는 아이들은 제거해서 계산량 줄임
# for 문으로 bfs_path 함수를 돌려서 leaf_isolate의 인덱스간의 가장 가까운 패스를 찾고
# 가장 많은 index를 가진 리스트가 이 tree의 가장 minimum height이 될 것
# 이까지는 했는데 다음은 모르겠다.. 어떻게 root를 찾을까