from typing import List

class Solution:
    """
    三数累加最接近目标
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # first = 0
        # last = 0
        if not nums: return 0
        if len(nums) <= 3: return sum(nums)
        res = 0
        tar_num = float('inf')
        num_l = len(nums)
        nums = sorted(nums)
        for i in range(num_l):
            bg_num = nums[i]
            first = i + 1
            last = num_l - 1
            tmp = target - bg_num

            while first < last:
                print(bg_num, nums[first], nums[last])
                if nums[first] + nums[last] == tmp:
                    return nums[first] + nums[last] + bg_num
                if abs(tmp - nums[first] - nums[last]) < abs(target - tar_num):
                    res = tmp - nums[first] - nums[last]
                    tar_num = nums[first] + nums[last] + bg_num
                if nums[first] + nums[last] < tmp:
                    first += 1
                else:
                    last -= 1

        return tar_num