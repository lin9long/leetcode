class Solution:
    """
    字典序的第K小叔子
    """

    def findKthNumber(self, n: int, k: int) -> int:
        def calc(n, n1, n2):
            step = 0
            while n1 <= n:
                step += min(n + 1, n2) - n1
                n1 *= 10
                n2 *= 10
            return step

        k -= 1
        cur = 1
        while k > 0:
            step = calc(n, cur, cur + 1)
            if step <= k:
                k -= step
                cur += 1
            else:
                k -= 1
                cur *= 10
                # cur+1) *= 10
        return cur
