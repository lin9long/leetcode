class Solution:
    """
    缺失的第一个正数
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums : return 1
        if max(nums) <= 0: return 1
        s_nums = sorted(nums)
        positive = 0
        pos= 0
        for i in s_nums:
            # print(i,pos)
            if i < 0:
                continue
            if i > 1 and pos == 0:
                return 1
            if i > 0 and pos == 0:
                pos += 1
                positive = i
                continue
            if i > 0 and pos > 0:
                # print(i,positive)
                diff = i - positive
                if diff > 1 :
                    return positive + 1
                else:
                    positive = i
        return positive + 1