#!/usr/bin/python
# -*-coding:utf-8 -*-


from typing import List


def query(s: str, queries: List[List[int]]):

    r_l = []
    for i in queries:
        count = 0
        start, end, n = i[0], i[1], i[2]
        if start == end:
            # s_q = s[start + 1:end + 1]
            r_l.append(True)
            continue
        s_q = s[start:end + 1]
        s_l = len(s_q)
        # print(int(s_l / 2))
        if s_l % 2 == 0:
            for p in range(int(s_l / 2)):
                # print(int(s_l / 2))
                if s_q[p] == s_q[s_l - p - 1]:
                    count += 1
        else:
            cnt = int((s_l - 1) / 2)
            if cnt == 0:
                cnt = cnt + 1
            for p in range(cnt):
                if s_q[p] == s_q[s_l - 1 - p]:
                    count += 1
        print(count,n,s_l)
        r_l.append(True if (count + n) >= s_l else False)
    return r_l


if __name__ == '__main__':
    s = query("abcda", [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]])
    print(s)
    # [true, false, false, true, true]
