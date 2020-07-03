from typing import List

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        """
        最长的重复子树
        :param A:
        :param B:
        :return:
        """
        # idx_a = 0
        # idx_b = 0
        # tmp_idx = 0
        # res_l = []
        # tmp_l = []
        # for a in A:
        #     tmp_idx = B.index(a) if a in B else 100
        #     if tmp_idx - idx_b == 1:
        #         idx_b = tmp_idx
        #         tmp_l.append(a)
        #         if len(tmp_l) > len(res_l):
        #             res_l = tmp_l
        # return len(res_l)+1
        a = len(A)
        b = len(B)
        res = 0
        tmp_l = []

        if a > b:
            A,B = B,A
        b_s = ',' + ','.join([str(i) for i in B]) + ','
        for i in A:
            tmp_l.append(str(i))
            if ',' + ','.join(tmp_l) + ',' in b_s:
                res = max(res,len(tmp_l))
            else:
                tmp_l = tmp_l[1:]
        return res