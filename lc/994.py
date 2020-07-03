#!/usr/bin/python
# -*-coding:utf-8 -*-

from typing import List


class Soluation:
    """
    广度优先算法，计算腐烂的橘子
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        nor_dic = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        unnor_dic = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        time = 0
        while nor_dic:
            # print(i)
            if not unnor_dic: return -1
            unnor_dic = {(i + l, j + r) for i, j in unnor_dic for l, r in pos if (i + l, j + r) in nor_dic}
            nor_dic -= unnor_dic
            time += 1
        return time


if __name__ == '__main__':
    data = [[2, 1, 1], [1, 1, 0], [0, 0, 1]]
    s = Soluation()
    t = s.orangesRotting(data)
    print(t)
