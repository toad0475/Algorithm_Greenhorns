from collections import deque
def maxAreaOfIsland(lst):
    visit = []
    area = 0
    i = 0
    j = 0
    queue = deque([i, j])

    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append([i, j])
            if lst[i][j] == 1:
                area += 1
            queue.append([i + 1, j])
            queue.append([i - 1, j])
            queue.append([i, j + 1])
            queue.append([i, j - 1])
            i += 1
            j += 1
            if i > len(lst) and j > len(lst[0]): break

    return

test = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxAreaOfIsland(test))