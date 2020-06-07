class Solution:
    # def superEggDrop(self, K: int, N: int) -> int:
    #     matrix = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
    #     # if N ==2:return 1
    #     m = 0
    #     while matrix[K][m] < N:
    #         m += 1
    #         # print(matrix[K][m])
    #         for k in range(1, K + 1):
    #             print(m,k)
    #             matrix[k][m] = matrix[k][m - 1] + matrix[k - 1][m - 1] + 1
    #     return m
    def superEggDrop(self, K: int, N: int) -> int:
        if K == 1: return N
        if K == 0: return 0
        d = set()

        def dp(K: int, N: int):
            res = float('inf')
            d.add((K, N))
            if (K, N) not in d:
                for i in range(N + 1):
                    res = min(res, max(dp(K - 1, i - 1), dp(K, N - i)))
                return res

        return dp(K, N)


if __name__ == '__main__':
    s = Solution()
    m = s.superEggDrop(3, 14)
    print(m)
