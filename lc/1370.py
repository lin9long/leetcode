

class Solution:
    """
    上升下降字符串
    """
    def sortString(self, s: str) -> str:
        from collections import Counter
        tmp_s = ''
        tmp_list = [ord(i) for i in s]
        c_list = Counter(tmp_list)
        c_list = sorted(c_list.items(), key=lambda d: d[0])
        c_list = {i[0]:i[1] for i in c_list}
        print(c_list)
        range_n = max(c_list.values())
        for _ in range(range_n):
            for i in c_list.keys():
                if c_list[i]>0:
                    tmp_s+=chr(i)
                c_list[i] = c_list[i]-1
            for i in reversed(c_list.keys()):
                if c_list[i]>0:
                    tmp_s+=chr(i)
                c_list[i] = c_list[i]-1
        return tmp_s