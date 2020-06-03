#!/usr/bin/python
# -*-coding:utf-8 -*-
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        from collections import Counter
        c_a = Counter(answers)
        return sum(-v % (k + 1) + v for k, v in c_a.items())
