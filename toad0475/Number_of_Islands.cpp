// submission : https://leetcode.com/submissions/detail/366532722/
/*
dfs 접근법
처음부터 돌면서 '1'을 발견하면 해당 인덱스를 다른 문자로 마킹한다. (나는 여기서 'p'로 마킹했음),
4 방향을 모두 순회하면서 결국 1 이 없을때까지 재귀를 돌아야 한다.

한번 돌고 오면, 그것은 하나의 섬을 모두 탐색했다는 의미가 되고, 돌고 온 섬은 이미 모두 'p'로 마킹되어 있다. 
몇번 돌고 오는지 가 섬의 개수가 된다.
*/

class Solution {
public:
    bool validLand(vector<vector<char>>& grid, int x, int y) {
        if (x < 0 || y < 0 || x >= grid.size() || y >= grid[0].size()) {
            return true;
        }
        return false;
    }
    
    void dfs(vector<vector<char>>& grid, int x, int y) {
        if (validLand(grid, x, y) || grid[x][y] != '1') {
            return;
	}
        grid[x][y] = 'p';
        dfs(grid, x + 1, y);
        dfs(grid, x - 1, y);
        dfs(grid, x, y + 1);
        dfs(grid, x, y - 1);
    }
    
    int numIslands(vector<vector<char>>& grid) {
        int island = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    island += 1;
                }
            }
        }
        return island;
    }
};
