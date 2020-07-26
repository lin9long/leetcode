

class Solution:
    """
    410。 分割数组的最大数值，指定分割为m个数组，取分割后能各组的总和最小
    """
    def splitArray(self, nums: List[int], m: int) -> int:
        def isValid(mid:int):
            tar,cnt = 0,1
            for num in nums:
                if tar+ num > mid:
                    cnt += 1
                    tar = num
                else:
                    tar += num
            return cnt <= m

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left+right)//2
            if isValid(mid):
                right = mid
            else:
                left = mid+1
        return left