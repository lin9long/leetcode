from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        不同路径，动态规划
        :param obstacleGrid:
        :return:
        """
        row = len(obstacleGrid)
        column = len(obstacleGrid[0])
        tmp_path = [[0 for i in range(column)] for j in range(row)]
        for i in range(row):
            for j in range(column):
                if obstacleGrid[i][j] == 0 :
                    if i ==0 and j == 0:
                        tmp_path[i][j] =1
                    else:
                        a = tmp_path[i-1][j] if i != 0 else 0
                        b = tmp_path[i][j-1] if j != 0 else 0
                        tmp_path[i][j] = a+b
        return tmp_path[-1][-1]