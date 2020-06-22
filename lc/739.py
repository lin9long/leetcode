class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        data = []
        # for p,i in enumerate(T):
        #     if p < len(T) - 1:
        #         tmp_t = T[p]
        #         # print(T[p+1:])
        #         tmp_max = max(T[p+1:])
        #         if tmp_max <= tmp_t:
        #             data.append(0)
        #             continue
        #         count = 0
        #         for j in T[p+1:]:
        #             count +=1
        #             if j > tmp_t:
        #                 data.append(count)
        #                 break
        # data.append(0)
        length_t = len(T)
        data = [0 for _ in range(length_t)]
        stack = []
        for i in range(length_t):
            tmp = T[i]
            while stack and tmp > T[stack[-1]]:
                pos = stack.pop()
                data[pos] = i - pos
            stack.append(i)
        return data