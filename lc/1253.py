from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        c_len = len(colsum)
        valid_list = [upper, lower]

        matrix = [[0 for _ in range(c_len)] for _ in range(2)]

        min_upper, min_lower = upper, lower

        for p, i in enumerate(colsum):
            if i == 2:
                matrix[0][p] = 1
                matrix[1][p] = 1
                min_upper -= 1
                min_lower -= 1
            if i == 1:
                if min_upper > min_lower:
                    matrix[0][p] = 1
                    min_upper -= 1
                elif min_upper <= min_lower:
                    matrix[1][p] = 1
                    min_lower -= 1
            if min_upper == 0 and min_lower == 0:
                return matrix

            # def isValid(matrix):
        #     upper = 0
        #     lower = 0
        #     # if sum(matrix[0]) == 0 and sum(matrix[1]) == 0:
        #     #     return True
        #     for p, i in enumerate(zip(matrix[0], matrix[1])):
        #         upper += i[0]
        #         lower += i[0]
        #         if i[0] + i[1] < colsum[p]:
        #             return False
        #
        #     return True if lower in valid_list and upper in valid_list else False
        #
        # for i in range(c_len*2):
        #     if isValid(matrix):
        #         return matrix
        #
        #
        #
        #
        # # def backtract(matrix, row):
        # #
        # #     # print(matrix, row)
        # #
        # #     def isValid(matrix):
        # #         upper = 0
        # #         lower = 0
        # #         if sum(matrix[0]) == 0 and sum(matrix[1]) == 0:
        # #             return True
        # #         for p, i in enumerate(zip(matrix[0], matrix[1])):
        # #             upper += i[0]
        # #             lower += i[0]
        # #             if i[0] + i[1] < colsum[p]:
        # #                 return False
        # #
        # #         return True if lower in valid_list and upper in valid_list else False
        # #
        # #     # if isValid(matrix):
        # #     #     return matrix
        # #     if row == 2:
        # #         return matrix
        # #
        # #     for j in range(len(matrix[0])):
        # #         print(isValid(matrix),matrix)
        # #         if not isValid(matrix):
        # #             continue
        # #         matrix[row][j] = 1
        # #         backtract(matrix, row + 1)
        # #         matrix[row][j] = 0
        #
        # return backtract(matrix, 0)


if __name__ == '__main__':
    s = Solution()
    res = s.reconstructMatrix(2, 1, [1, 1, 1])
    print(res)
