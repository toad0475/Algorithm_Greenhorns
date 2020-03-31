def maxAreaOfIsland(lst):
    visit_1 = []
    area = 0

    i = 0
    while i < len(lst):
        j = 0
        while j < len(lst[i]):
            if lst[i][j] == 1:
                visit_1.append([i, j])
            j += 1
        i += 1

    return area, visit_1


test = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxAreaOfIsland(test))