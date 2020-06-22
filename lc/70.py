class Solution:
    """
    爬楼梯，
    n阶楼梯的解法为，n-1解法+ n-2解法，
    n-1、n-2到n的解法均为1
    """
    def climbStairs(self, n: int) -> int:
        p, q, r = 1, 2, 0
        for i in range(2, n, 1):
            r = p + q
            p = q
            q = r

        return max(r, n)