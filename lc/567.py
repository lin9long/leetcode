class Soluation:

    def checkInclusion(self, t: str, s: str):

        # def contain(t, s):
        #     # print(t.items()[0],t.items()[1])
        #     f = True
        #     for i in t.items():
        #         if s.get(i[0], 0) < i[1]:
        #             # print(s[i[0]],i[1],i)
        #             f = False
        #     return f

        from collections import Counter, defaultdict
        left = 0
        right = 0
        a_d = defaultdict(int)
        t_c = Counter(t)
        valid_windows = 0
        valid = len(t_c)
        s_len = float('inf')
        while right < len(s):
            r_c = s[right]
            tmp_s = s[left:right]
            right += 1
            if valid_windows < valid and r_c in t_c:
                a_d[r_c] += 1
                if a_d[r_c] == t_c[r_c]:
                    valid_windows += 1
            while valid_windows == valid:
                # print(tmp_s,a_d,valid_windows)
                if right - left < s_len:
                    start = left
                    s_len = right - left
                if left < right:
                    l_c = s[left]
                    left += 1
                    tmp_s = s[left:right]
                    if l_c in t_c:
                        if a_d[l_c] == t_c[l_c]:
                            valid_windows -= 1
                        a_d[l_c] -= 1
        return -1 if s_len == float('inf') else s[start:start+s_len]

            # if contain(t_c, a_d):

            # while left < right:
            #     c_s = s[left]
            #     tmp_s = s[left:right]
            #     tmp_s_c = Counter(tmp_s)
            #     tmp_s_c[c_s] = tmp_s_c[c_s] - 1
            #     if not contain(t_c, tmp_s_c):
            #         print(tmp_s)
            #     left += 1

            # print(tmp_s)


if __name__ == '__main__':
    s = Soluation()
    res = s.checkInclusion('abe', 'asdaddebsasdwre')
    print(res)
