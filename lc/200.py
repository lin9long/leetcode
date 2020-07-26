class Solution:
    """
    岛屿数量
    """
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid : return 0

        row = len(grid) +2
        col = len(grid[0]) +2
        grid = [[0]*(col)]+[['0'] +i +['0'] for i in grid]+[[0]*(col)]
        # print(grid)
        res = 0

        def dfs(i,j):
            if i >= row-1 or j >= col-1 or i == 0 or j == 0 or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        for i in range(1,row-1):
            for j in range(1,col-1):
                # print(i,j)
                if grid[i][j] == '1':
                    dfs(i,j)
                    res+=1
        return res