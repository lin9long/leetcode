#!/usr/bin/python

from typing import List
from collections import Counter


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        t_f = Counter([(T, F) for _, T, F in orders])
        ts = sorted([T for _, T, _ in orders],key=int)
        fs = sorted([F for _, _, F in orders])

        return [['Table'] + fs ]+[[t]+[str(t_f[t,f]) for f in fs] for t in ts]


if __name__ == '__main__':
    s = Solution()
    orders = [["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
              ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]
    print(s.displayTable(orders))
