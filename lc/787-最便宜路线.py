import _heapq
from collections import defaultdict

class Solution:

    def findCheapestPrice(self, n, flights, src, dst, K):
        best = {}
        graph = defaultdict(list)
        for f ,d ,cost in flights:
            graph[f].append([d ,cost])

        pq = [[0 ,0 ,src]]

        while pq:
            cost ,k ,d = _heapq.heappop(pq)
            if k> K + 1 or cost > best.get((d, k), float('inf')):
                continue
            if d == dst: return cost

            for loc, cost_c in graph[d]:
                n_cost = cost + cost_c
                if n_cost < best.get((loc, k + 1), float('inf')):
                    best[(loc, k + 1)] = n_cost
                    _heapq.heappush(pq, [n_cost, k + 1, loc])
        return -1

if __name__ == '__main__':
    s = Solution
    s.findCheapestPrice()