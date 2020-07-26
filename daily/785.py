import collections
from typing import List

class Solution:
    """
    判断二分图
    """
    def isBipartite(self, graph: List[List[int]]) -> bool:
        u,r,g = 0,1,2
        g_len = len(graph)
        status = [u] * g_len
        res = True
        for i,c in enumerate(status):
            if c == u:
                c = r
                q = collections.deque()
                q.append((i,c))
            while q:
                i,c = q.popleft()
                pos_c = g if c == r else r
                for j in graph[i]:
                    if status[j] == u:
                        status[j] = pos_c
                        q.append((j,pos_c))
                    else:
                        if status[j] != pos_c:
                            return False
        return res