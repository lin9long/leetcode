from typing import List

class Solution:
    """
    划分数组为连续数字的集合
    """
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        from collections import Counter
        c = Counter(nums)
        d_l = []
        d_l_n = []
        import heapq
        for i in c.items():
            # print(i)
            heapq.heappush(d_l, i)
        tmp_k = 0
        l_c = 0
        # r_l = []
        while d_l:
            data = heapq.heappop(d_l)
            d, v = data[0], data[1]
            print(tmp_k, d, v, l_c)
            if d - tmp_k == 1 or tmp_k == 0:
                # d_l.append(d_l)
                tmp_k = d
                l_c += 1
                if v > 1:
                    v = v - 1
                    heapq.heappush(d_l_n, (d, v))
                if l_c == k:
                    l_c = 0
                    tmp_k = 0
                    while d_l_n:
                        heapq.heappush(d_l, heapq.heappop(d_l_n))
            else:
                break
            # return False
        if l_c != 0:
            return False
        else:
            return True


