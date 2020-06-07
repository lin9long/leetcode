from typing import List


class Soluation:
    def findMaxSubString(self, nums: List[int]):
        max_ = nums[0]
        tmp = max_
        for i in nums:
            if tmp + i >= i:
                max_ = max(max_, tmp + i)
                tmp = tmp + i
            else:
                max_ = max(max_, tmp, tmp + i, i)
                tmp = i
        return max_


if __name__ == '__main__':
    s = Soluation()
    res = s.findMaxSubString([-2,1,-3,4,-1,2,1,-5,4])
    print(res)
