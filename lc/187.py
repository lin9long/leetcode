#!/usr/bin/python
# -*-coding:utf-8 -*-

from typing import List


class Solution:
    """
    所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。

    """
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        n = len(s)
        a = 4
        al = pow(a, L)
        a_d = {'A': 0, "C": 1, "G": 2, "T": 3}
        s_n = [a_d[i] for i in s]
        h = 0
        h_l = set()
        out_put = set()
        for i in range(n - L + 1):
            if i != 0:
                h = h * a - s_n[i - 1] * al + s_n[i + L - 1]
                print(i, h)
            else:
                for j in range(L):
                    h = h * a + s_n[j]
                print(i, h)
            if h in h_l:
                out_put.add(s[i:i + L])
            h_l.add(h)

        return out_put




if __name__ == '__main__':
    s = Solution()
    o = s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    print(o)
