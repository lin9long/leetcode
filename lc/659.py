import collections
from typing import List


def isPossible(nums: List[int]) -> bool:
    """
    分割数组为连续子序列
    :param nums:
    :return:
    """
    d = collections.defaultdict(list)
    l = list()
    for n in nums:
        if len(d[n - 1]) == 0:
            first = 1
        else:
            first = d[n - 1][0]
            d[n - 1].pop(0)
            first += 1

        d[n].append(first)
        d[n] = sorted(d[n])

        print(d)
    for k in d.keys():
        if any(c < 3 for c in d[k]): return False

    return True


if __name__ == '__main__':
    res = isPossible([1, 2, 2, 3, 4, 5])
    print(res)
