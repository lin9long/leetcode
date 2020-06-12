from typing import List

class Solution:
    """
    有效回旋镖问题
    """
    def isBoomerang(self, points: List[List[int]]) -> bool:
        s_p_0 = set([i[0] for i in points])
        s_p_1 = set([i[1] for i in points])
        s_p = set([(i[0],i[1]) for i in points])
        s_r = set()
        s_points = sorted(points,key=lambda x:x[0])
        for i in range(1,len(points)):
            s_r.add((s_points[i][0] - s_points[i-1][0],s_points[i][1] - s_points[i-1][1]))
        return False if len(s_p_0) ==1 or len(s_p_1) == 1 or len(s_p) < 3 or len(s_r) == 1 else True