"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        data_all = [(len(i),i) for i in strs]
        data_all = sorted(data_all,key = lambda x:x[0])
        # print(data_all)
        res = ''
        try:
            for i,j in data_all[:1]:
                for p in range(i):
                    tar = j[p]
                    for _,t in data_all[1:]:
                        tmp = t[p]
                        if tmp == tar:
                            continue
                        else:
                            raise Getoutofloop()
                    res += tar
        except:
            pass
        return res