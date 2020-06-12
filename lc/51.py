from typing import List


class Solution:

    """
    N皇后
    """

    def solveNQueens(self, n: int) -> List[List[str]]:

        def backTrack(matrix, row, d_l):

            def isValid(matrix, row, col):

                #当前列
                size = len(matrix)
                for i in range(size):
                    if matrix[i][col] == 'Q':
                        return False
                # 右上方
                pos_a = row - 1
                pos_b = col + 1
                while pos_a >= 0 and pos_b < size:
                    if matrix[pos_a][pos_b] == 'Q':
                        return False
                    pos_a -= 1
                    pos_b += 1

                # 左上方
                pos_a = row - 1
                pos_b = col - 1
                while pos_a >= 0 and pos_b >= 0:
                    if matrix[pos_a][pos_b] == 'Q':
                        return False
                    pos_a -= 1
                    pos_b -= 1
                return True

            print(row,len(matrix))
            if row == len(matrix):
                d_l.append([''.join(matrix[i]) for i in range(len(matrix))])
                return
            d_len = len(matrix[row])
            for i in range(d_len):
                # print(row)
                if not isValid(matrix, row, i):
                    continue
                matrix[row][i] = 'Q'
                # self.d_l.append((''.join[matrix[i] for i in len(matrix)]))

                backTrack(matrix, row + 1, d_l)
                matrix[row][i] = '.'

            return d_l

        d_l = []
        matrix = [['.' for _ in range(n)] for _ in range(n)]
        # print(matrix)

        return backTrack(matrix, 0 ,d_l)


if __name__ == '__main__':
    s = Solution()
    res = s.solveNQueens(8)
    print(res)

# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         res = []
#         track = []
#
#         def isValid(track, row, col):
#             if not track:
#                 return True
#             for i in range(row):
#                 if track[i][col] == 'Q':  # 本列
#                     return False
#             i = row - 1
#             j = col - 1
#             while i >= 0 and j >= 0:  # 左上
#                 if track[i][j] == 'Q':
#                     return False
#                 i -= 1
#                 j -= 1
#             i = row - 1
#             j = col + 1
#             while i >= 0 and j < n:  # 右上
#                 if track[i][j] == 'Q':
#                     return False
#                 i -= 1
#                 j += 1
#             return True
#
#         def backtrack(track, row):
#             # ans = [.]*n 容易出错, 循环中,需要改回来
#             # print(track)
#             if len(track) == n:
#                 res.append(track[:])
#                 return
#             for i in range(n):  # n:col
#                 ans = ['.'] * n  # 改在这里,就不需要回退时处理了不然会出现[Q,Q]
#                 if isValid(track, row, i):
#                     ans[i] = 'Q'
#                     track.append(list(ans))
#                     backtrack(track, row + 1)
#                     track.pop()  # 这里除了需要还
#
#         backtrack([], 0)
#         res2 = [[] for _ in range(len(res))]
#         for index, re in enumerate(res):
#             for r in re:
#                 r_str = "".join(r)
#                 res2[index].append(r_str)
#
#         return res2
