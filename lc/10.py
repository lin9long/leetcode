class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        实现正则表达式
        :param s:
        :param p:
        :return:
        """
        if not p:
            return not s
        print(p)
        # is_match = False
        # s_l = len(s)
        # p_l = len(p)
        # p_p = 0
        # s_p = 0
        # for i in range(p_l):
        #     if p[i] == s[s_p]:
        #         is_match = True
        is_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or is_match and self.isMatch(s[1:], p))
        else:
            return is_match and self.isMatch(s[1:], p[1:])


if __name__ == '__main__':
    s = Solution()
    is_match = s.isMatch('aabbb','a*.*')
    print(is_match)
