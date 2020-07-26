from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        排列，回溯算法
        :param nums: 
        :return: 
        """
        # from itertools import permutations
        # res = []
        # for i in permutations(nums,len(nums)):
        #     res.append(i)
        # return res

        def backtrack(nums,track,res):
            # print(track,res)
            # print(nums,track)
            # def isvalid(nums,i):
            #     if i in nums:
            #         return False
            #     return True
            if len(track) == len(nums):
                res.append(track[:])
                return
            for i in range(len(nums)):
                if nums[i] in track:
                    continue
                track.append(nums[i])
                backtrack(nums, track, res)
                track.pop()
            return res
        track = []
        a = []
        res = backtrack(nums, track, a)
        return res