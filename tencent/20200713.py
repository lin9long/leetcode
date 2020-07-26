class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
        :param grid:
        :return:
        """
        path = [(-1,0),(1,0),(0,-1),(0,1)]
        res = 0
        row = len(grid)
        column = len(grid[0])
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    # print(i,j,res)
                    for c,r in path:
                        # print(i+r,j+c,i+r<=row-1,j+c<=column-1)
                        if i+r < 0 or j+c < 0 or j+c >= column or i+r >= row:
                            # print(i,j)
                            res +=1
                        elif i+r >= 0 and j+c >= 0 and  i+r<=row-1 and j+c<=column-1 :
                            # print(i+r,j+c)
                            if grid[i+r][j+c] == 0:
                                res+=1
        return res