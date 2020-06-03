#!/usr/bin/python
# -*-coding:utf-8 -*-
from typing import List


class Soluation:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = flowerbed + [0]
        flowerbed = [0] + flowerbed
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                n -= 1
        return n <= 0


if __name__ == '__main__':
    s = Soluation()
    print(s.canPlaceFlowers([0],1))