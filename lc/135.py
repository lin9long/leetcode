class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        135. 分发糖果，相邻两个学生，分数高的糖果多
        :param ratings:
        :return:
        """
        c = 0
        left = [1 for _ in range(len(ratings))]
        right = left[:]
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                left[i] = left[i - 1] + 1
        c = left[-1]
        ratings = ratings[::-1]
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                right[i] = right[i - 1] + 1
                # print(left[len(ratings)-i-1],right[i])
            c += max(left[len(ratings) - i - 1], right[i])
        # print(left,right)
        return c