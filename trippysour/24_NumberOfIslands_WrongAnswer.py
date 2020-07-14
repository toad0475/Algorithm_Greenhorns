grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def numIslands1(grid):

    count = 0
    visited = []
    island = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if [i, j] in visited: pass
            elif grid[i][j] == '1' and [i, j] not in island: # 이것 뿐만 아니라 상하좌우도 체크
                count += 1
                island.append([i, j])
            visited.append([i, j])

    return count

def numIsland2(grid):
    x = 0
    y = 0
    q = [[x,y]]
    visited = []
    island = []
    count = 0

    while q:
        vertex = q.pop(0)
        if vertex in visited: pass

        elif grid[vertex[0]][vertex[1]] == '1' and vertex not in island:
            count += 1
            island.append([x,y])

            q.append([x + 1, y])

            q.append([x, y + 1])

        visited.append([x,y])
        return count



# 하나씩 방문하면서 값이 1인지 체크
# 값이 1이고 visited에 속하지 않으면서 visited의 상하좌우에 속하지 않으면 count + 1


print(numIslands1(grid))
print(numIsland2(grid))

