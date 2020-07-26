class Solution:
    def decodeString(self, s: str) -> str:
        """
        字符串解码
        :param s:
        :return:
        """

        def dfs(i,s):
            res,num = '',0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    num = num * 10 + int(s[i])
                    # print(num)
                elif s[i] == '[':
                    i,tmp = dfs(i+1,s)
                    res = res + num*tmp
                    num = 0
                elif s[i] == ']':
                    # res = num * res
                    return i, res
                else:
                    res += s[i]
                i+=1
            return res
        return dfs(0,s)