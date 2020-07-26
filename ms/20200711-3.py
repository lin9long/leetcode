from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        auxiliary = intervals
        auxiliary = sorted(auxiliary,key = lambda x : x[0])
        index = 1
        while index < len(auxiliary):
            # print(auxiliary,index)
            if auxiliary[index][0] <= auxiliary[index-1][1]:
                auxiliary[index-1][1] = max(auxiliary[index-1][1],auxiliary[index][1])
                del auxiliary[index]
            else:
                index+=1
        return auxiliary